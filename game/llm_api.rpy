init python:
    import ssl, certifi
    ssl._create_default_https_context = lambda *a, **kw: ssl.create_default_context(cafile=certifi.where())

    import os
    import json
    import urllib.request
    import urllib.error

    def load_env_var(var_name):
        """Carica una variabile d'ambiente dal file .env"""
        # Prova diversi percorsi possibili
        possible_paths = [
            os.path.join(renpy.config.gamedir, ".env"),  # Percorso game directory
            os.path.join(os.getcwd(), "game", ".env"),    # Percorso relativo dalla root
            os.path.join(os.path.dirname(__file__), ".env")  # Percorso relativo dal file
        ]
        
        for env_path in possible_paths:
            if os.path.exists(env_path):
                try:
                    with open(env_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            line = line.strip()
                            if line and not line.startswith("#"):
                                if "=" in line:
                                    key, value = line.split("=", 1)
                                    if key.strip() == var_name:
                                        return value.strip()
                except Exception as e:
                    print(f"Errore lettura .env da {env_path}: {e}")
                    continue
        
        print(f"File .env non trovato in: {possible_paths}")
        return None

    def query_llm(prompt):
        """
        Interroga Gemini 2.0 Flash via API REST.
        La chiave API viene caricata dal file .env
        """
        # Carica la chiave dal file .env
        GG_API_KEY = load_env_var("GOOGLE_API_KEY")
        #print("--- DEBUG CHIAVE ---")
        #print(f"La chiave letta è: {GG_API_KEY}")
        GG_MODEL_ENDPOINT = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"

        if not GG_API_KEY:
            return "Chiave API mancante. Assicurati che il file .env contenga GOOGLE_API_KEY."

        try:
            # Corpo della richiesta (nuovo formato Gemini v1beta)
            body = {
                "contents": [
                    {"parts": [{"text": prompt}]}
                ],
                "generationConfig": {
                    "maxOutputTokens": 1024,  # Aumentato per risposte più lunghe
                    "temperature": 0.7
                }
            }

            data = json.dumps(body).encode("utf-8")
            url = f"{GG_MODEL_ENDPOINT}?key={GG_API_KEY}"
            print(f"[LLM-API] URL: {url}")
            print(f"[LLM-API] BODY: {json.dumps(body, ensure_ascii=False)}")
            req = urllib.request.Request(
                url,
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST"
            )

            # Invio richiesta
            with urllib.request.urlopen(req, timeout=20) as resp:
                resp_text = resp.read().decode("utf-8")
                print(f"[LLM-API] RESPONSE: {resp_text}")
                j = json.loads(resp_text)

                # Estrae il testo generato
                return j["candidates"][0]["content"]["parts"][0]["text"].strip()

        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8") if hasattr(e, "read") else ""
            print(f"[LLM-API] HTTPError: {e.code} {e.reason}\n{err_body}")
            # Prova a estrarre solo il messaggio leggibile
            try:
                err_json = json.loads(err_body)
                msg = err_json.get("error", {}).get("message", "Errore API generico.")
                return f"Errore API ({e.code}): {msg}"
            except Exception:
                return f"Errore API ({e.code}): {e.reason}"
        except Exception as e:
            print(f"[LLM-API] Exception: {e}")
            return f"Errore di rete o parsing: {e}"
