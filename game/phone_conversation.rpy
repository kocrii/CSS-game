## Phone conversation module
## This file contains the reusable `phone_chat` label used by the game.

label phone_chat:
    

    # Variabili per tenere traccia della conversazione
    $ turn = 0
    $ MAX_TURNS_CHAT = 6  # Numero di scambi prima dell'analisi (ridotto per test)
    $ toni_conversazione = []  # Lista per tenere traccia dei toni usati
    $ tono_prevalente = "neutra"  # Valore predefinito

    # Ricevi subito il primo messaggio dall'hacker (LLM) prima che l'utente possa scrivere
    $ hacker_prompt = prompt_hacker("", hacker_phase)
    python:
        import threading
        llm_result = {'text': None, 'error': None}
        def _call_llm():
            try:
                llm_result['text'] = query_llm(hacker_prompt)
            except Exception as e:
                llm_result['error'] = str(e)
        _thread = threading.Thread(target=_call_llm)
        _thread.daemon = True
        _thread.start()
        while _thread.is_alive():
            renpy.pause(0.1)
        primo_messaggio = llm_result.get('text') or "(Nessuna risposta)"
    n_nvl "{i}Da (mio account):{/i} [primo_messaggio]"
    $ append_history("hacker", primo_messaggio)

    while turn < MAX_TURNS_CHAT:
        $ user_text = renpy.input("Scrivi un messaggio:", length=300)
        $ user_text = user_text.strip()

        if user_text == "":
            n_nvl "..."
            # Nessun jump: la conversazione prosegue e il LLM risponde comunque

        # Mostra messaggio utente e registra nella cronologia
        n_nvl "{i}Tu:{/i} [user_text]"
        $ append_history("user", user_text)

        # Controlla comandi di uscita (usa check_exit_command invece di analizza_risposta)
        $ tipo = analizza_risposta(user_text)
        if check_exit_command(user_text):
            nvl_narrator "Conversazione terminata."
            jump choices_comune2
        
        # Registra il tono del messaggio per l'analisi finale
        $ toni_conversazione.append(tipo)

        # Costruisci prompt per l'LLM (l'hacker risponde) usando la fase corrente
        $ hacker_prompt = prompt_hacker(user_text, hacker_phase)

        # Esegui la chiamata all'LLM in un thread separato in modo che l'interfaccia rimanga reattiva.
        python:
            import threading
            llm_result = {'text': None, 'error': None}

            def _call_llm():
                try:
                    llm_result['text'] = query_llm(hacker_prompt)
                except Exception as e:
                    # Salva l'errore per gestirlo più avanti senza mostrarlo ai giocatori
                    llm_result['error'] = str(e)

            _thread = threading.Thread(target=_call_llm)
            _thread.daemon = True
            _thread.start()

        # Mostra un indicatore nell'interfaccia del telefono che l'LLM sta scrivendo
        nvl_narrator "Sta scrivendo..."

        # Attendi il completamento del thread in modo non bloccante (aggiorna l'interfaccia)
        python:
            while _thread.is_alive():
                renpy.pause(0.1)

        # Recupera risultato/errore
        python:
            response = llm_result.get('text')
            error = llm_result.get('error')

        # Sanitizza e gestisci errori dell'LLM prima di mostrare il testo
        python:
            display_response = None
            if error:
                # Non mostrare messaggi di errore ai giocatori: usa il comportamento di 'nessuna risposta'
                append_history("system", "LLM error: service unavailable")
            elif not response:
                display_response = None
            else:
                low = response.lower()
                if "429" in low or "too many requests" in low or "resource exhausted" in low or "errore api" in low or "error" in low:
                    # Tratta come assenza di risposta
                    append_history("system", "LLM error: service unavailable")
                    display_response = None
                else:
                    # Escape delle parentesi graffe per evitare che Ren'Py interpreti text tags
                    display_response = response.replace("{", "{{").replace("}", "}}")
                    append_history("hacker", display_response)

        if not display_response:
            #n_nvl 
            elisa "Silenzio. Nessuna risposta... ma sento un brivido."
        else:
            n_nvl "{i}Da (mio account):{/i} [display_response]"

        $ turn += 1
        
    # Dopo 5 turni, analizza il tono prevalente della conversazione
    python:
        # Prepara l'elenco opzioni: usa outcome_options se definito dal chiamante, altrimenti default a 3 esiti
        options = ["sicura", "rischiosa", "neutra"]
        if 'outcome_options' in globals() and isinstance(outcome_options, list) and len(outcome_options) > 0:
            options = outcome_options

        # Analisi locale dei toni raccolti (parole chiave) per forzare precedenza a 'sicura' se presente.
        safe_count = toni_conversazione.count("sicura")
        risky_count = toni_conversazione.count("rischiosa")

        # Regola di precedenza:
        # - Se c'è almeno una risposta sicura e nessuna rischiosa -> esito direttamente 'sicura'
        # - Se safe_count >= risky_count + 1 (più risposte difensive che rischiose) -> forziamo 'sicura'
        # (Questo previene casi in cui l'LLM classifica male singole parole di protezione.)
        forced_sicura = False
        if "sicura" in options:  # Solo se l'opzione esiste nel set corrente
            if safe_count > 0 and risky_count == 0:
                tono_prevalente = "sicura"
                forced_sicura = True
                append_history("system", "Override locale: sicura (nessuna risposta rischiosa)")
            elif safe_count >= risky_count + 1 and safe_count > 0:
                tono_prevalente = "sicura"
                forced_sicura = True
                append_history("system", f"Override locale: sicura (safe_count={safe_count} risky_count={risky_count})")

        # 1. Prova classificazione tramite LLM (opzioni dinamiche)
        llm_choice = None
        if not forced_sicura:  # Se non è stato forzato localmente, interroga l'LLM
            # Forniamo istruzione arricchita con conteggi locali come hint
            istruzione_llm = (
                "Stai decidendo il ramo narrativo più coerente."
                f"Conteggi locali: sicura={safe_count}, rischiosa={risky_count}. Se il giocatore ha menzionato autorità o rifiuto, propendi per 'sicura'."
            )
            llm_choice = llm_classify(options, instruction=istruzione_llm)
        classification_source = "fallback"

        if forced_sicura:
            classification_source = "override_locale"
        elif llm_choice in options:
            tono_prevalente = llm_choice
            classification_source = "llm"
            append_history("system", f"Classificazione LLM: {llm_choice}")
        else:
            # 2. Fallback locale
            if set(options) == set(["sicura", "rischiosa", "neutra"]):
                # Se siamo sulle 3 opzioni standard, usa majority + priorità sui toni registrati
                counts = {
                    "rischiosa": toni_conversazione.count("rischiosa"),
                    "sicura": toni_conversazione.count("sicura"),
                    "neutra": toni_conversazione.count("neutra"),
                }
                non_zero = {k: v for k, v in counts.items() if v > 0}
                if non_zero:
                    priority = {"sicura": 3, "rischiosa": 2, "neutra": 1}
                    tono_prevalente = sorted(non_zero.items(), key=lambda kv: (-kv[1], -priority[kv[0]]))[0][0]
                else:
                    tono_prevalente = "neutra"
            else:
                # Se l'elenco opzioni è personalizzato, scegli un fallback ragionevole tra le opzioni
                # Preferisci "neutra" se presente, altrimenti la prima opzione definita
                tono_prevalente = "neutra" if "neutra" in options else options[0]
            append_history("system", f"Classificazione fallback: {tono_prevalente}")

    # Messaggio diagnostico opzionale per il giocatore (controllato da DEBUG_CHAT)
    if DEBUG_CHAT:
        $ classificazione_msg = "Classificazione: LLM" if classification_source == "llm" else "Classificazione: fallback locale"
        n_nvl "[classificazione_msg]"
    
    # Mostra un messaggio di transizione
    "La conversazione si conclude..."

    # Strategia di branching flessibile:
    # 1. Salva l'esito in una variabile globale per uso successivo.
    $ chat_outcome = tono_prevalente

    # 2. Se esiste una mappa dinamica (outcome_map) definita dal chiamante, usala.
    #    outcome_map può contenere chiavi corrispondenti alle opzioni in `options` e opzionalmente "default".
    #    Esempio da impostare prima di jump phone_chat:
    #    $ outcome_options = ["chiedi_aiuto", "rifiuto", "accondiscende", "evasiva"]
    #    $ outcome_map = {"chiedi_aiuto": "cap2_aiuto", "rifiuto": "cap2_rifiuto", "accondiscende": "cap2_corda", "evasiva": "cap2_evasiva", "default": "cap2_evasiva"}
    # 3. Se non c'è outcome_map o non trova una mappatura valida, salta al label con il nome dell'outcome.
    python:
        target_label = None
        if 'outcome_map' in dir(store):
            target_label = outcome_map.get(chat_outcome, outcome_map.get("default", None))
        
        # Se non c'è mappatura, prova a cercare un label con il nome dell'outcome
        if not target_label:
            # Controlla se esiste un label con quel nome
            if renpy.has_label(chat_outcome):
                target_label = chat_outcome
            elif renpy.has_label("default"):
                target_label = "default"
            else:
                # Ultimo fallback: continua allo statement successivo nel contesto chiamante
                # Questo richiede che phone_chat sia chiamato con 'call' invece di 'jump'
                renpy.notify("Conversazione conclusa")
                target_label = None
    
    if target_label:
        jump expression target_label
    
    return


    # altro personaggio2
    # n_nvl e2m1_b "oddio chi sei?"
    # n_nvl "nessuno."
    # n_nvl e2m2_b "ci sei?"
    # n_nvl e1m2 "prova"
    # show elisa_sorpresa at right, character_size
    # #n_nvl e2m1_b "prova"
    # show elisa_normale at right, character_size
    # n_nvl "ciao"

    # show anna at right, character_size:
    #     ease 0.5 xalign 0.5 

    # elisa_normale  "That's it for the demo!"
    # elisa_normale e1m2 "Do you have any question?"

    
