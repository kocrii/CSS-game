init python:
    # ===== FUNZIONI PER CHAT E ANALISI =====

    # Chat history (kept in Python variables inside the init block)
    chat_history = []
    MAX_HISTORY = 6 
    hacker_phase = "initial"  # Traccia la fase della conversazione: "initial", "threatening", "final"
    DEBUG_CHAT = False  # Se True, mostra messaggi diagnostici a schermo

    def append_history(role, text):
        global chat_history
        chat_history.append({"role": role, "text": text})
        if len(chat_history) > MAX_HISTORY:
            chat_history = chat_history[-MAX_HISTORY:]

    def check_exit_command(testo):
        """Controlla se il testo contiene un comando di uscita."""
        exit_commands = ["exit"]
        return any(cmd in testo.lower() for cmd in exit_commands)

    def analizza_risposta(testo):
        testo = testo.lower()
        
        # Risposte che fanno perdere punti (accondiscendenti/rischiose)
        if any(p in testo for p in [
            "va bene", "ok ci sono", "arrivo", "dove", "quando", "a che ora",
            "d'accordo", "come vuoi", "farò come dici"
        ]):
            return "rischiosa"
            
        # Risposte che fanno guadagnare punti (difensive/sicure)
        elif any(p in testo for p in [
            "polizia", "denuncia", "aiuto", "adulto", "genitore", "professore",
            "non ci vengo", "mi rifiuto", "non lo farò", "screenshot", "denunciare"
        ]):
            return "sicura"
            
        # Risposte neutre/domande
        elif any(p in testo for p in [
            "perché", "chi sei", "cosa vuoi", "non capisco",
            "cosa hai fatto", "come hai fatto"
        ]):
            return "neutra"
            
        return "altra"

    def prompt_hacker(user_text, phase="initial"):
        """Costruisce il prompt per Gemini che deve rispondere come l'hacker/bullo."""
        # Escludi voci di sistema dal contesto per non inquinare il prompt
        recent_msgs = [m for m in chat_history[-MAX_HISTORY:] if m.get('role') != 'system']
        storia = "\n".join(
            [f"{m['role'].capitalize()}: {m['text']}" for m in recent_msgs]
        )
        
        # Istruzioni base
        base_instructions = """Sei un bullo online che ha rubato l'account social di Elisa.
Ora stai scrivendo nella sua chat rivolgendoti a lei, fingendo di essere lei stessa per confonderla.
Rispondi sempre in italiano, massimo due frasi, in tono provocatorio e manipolativo, e prendendola in giro."""

        # Istruzioni specifiche per fase
        if phase == "initial": #Il Disorientamento
                phase_instructions = """Obiettivo: Disorientamento. Non minacciare ancora, ma fai capire che sei 'dentro' la sua vita. 
                Usa un tono calmo e inquietante. Esempio: 'Che carine le foto che mandi a tua madre, Elisa. Peccato che ora decido io chi può vederle.' Massimo due frasi. Non rispondere a domande su chi sei, di' solo che sei la sua nuova ombra."""
        if phase == "manipulative": #Il Gaslighting
                phase_instructions = """Obiettivo: Isolamento Sociale. Convinci Elisa che i suoi amici la odiano. 
                Usa la tecnica del Gaslighting: 'Ho letto cosa scrive Anna di te nelle chat private... credi davvero che le importi qualcosa? Sei sola, Elisa. Solo io so chi sei veramente.' Devi distruggere la sua fiducia negli altri per renderla dipendente da te. Massimo due frasi."""
        elif phase == "threatening": #Il Ricatto Morale
                phase_instructions = """Obiettivo: Coercizione. Introduci una richiesta assurda ma 'piccola'. Usa la tecnica del 'Piede nella porta'. 
                'Se vuoi che non pubblichi quel tuo video ridicolo, devi scrivermi ogni ora cosa stai facendo. O forse preferisci che lo vedano tutti a scuola domani?' 
                Mantieni una pressione costante, facendole credere che ha ancora una scelta, anche se non è vero. Massimo due frasi."""

        elif phase == "final":
            phase_instructions = """Obiettivo: Terrore e Appuntamento. Diventa aggressivo e diretto. 'Il tempo delle chiacchiere è finito. 
            O vieni al campetto alle 20:00 o premo invio e la tua reputazione sparirà per sempre. 
            Tic toc, Elisa.' Usa i suoi fallimenti precedenti nella chat per schernirla. Non accettare scuse. Massimo due frasi."""
        else:
                phase_instructions = "Rispondi in tono provocatorio. Rispondi sempre con massimo due frasi."
        
        return f"""{base_instructions}
{phase_instructions}

Cronologia chat:
{storia}

Ultimo messaggio ricevuto: "{user_text}"
Rispondi ora come se fossi l'hacker che scrive dal suo account rubato.
"""



    def llm_classify(options, instruction=None):
        """Chiede all'LLM di classificare la conversazione in UNA sola etichetta tra `options`.
        Ritorna una stringa contenente una delle opzioni, altrimenti None in caso di errore o risposta non valida.
        """
        try:
            # Costruisci contesto con ultimi messaggi
            storia = "\n".join(
                [f"{m['role'].capitalize()}: {m['text']}" for m in chat_history[-MAX_HISTORY:]]
            )

            opts_text = ", ".join(options)
            extra = instruction or """Analizza l'andamento della conversazione dal punto di vista delle scelte del giocatore.
Scegli esattamente UNA sola etichetta tra quelle fornite.

CRITERI DI CLASSIFICAZIONE:
- "sicura": il giocatore ha menzionato autorità (polizia, genitori, professori, adulti), si è rifiutato, ha parlato di denuncia o screenshot, o ha mostrato resistenza chiara
- "rischiosa": il giocatore ha accettato richieste, è accondiscendente, ha dato informazioni o ha mostrato disponibilità a seguire le richieste dell'hacker
- "neutra": il giocatore ha fatto solo domande generiche o ha risposto in modo evasivo senza prendere una posizione chiara"""

            prompt = f"""
Sei un assistente che deve classificare una conversazione in base a categorie predefinite.
{extra}

Categorie disponibili: {opts_text}

Regole di output molto importanti:
- Rispondi SOLO con una delle etichette esatte tra: {opts_text}
- Non aggiungere altre parole, spiegazioni o punteggiatura.

Conversazione (ultimi messaggi):
{storia}
Classifica la conversazione ora:
"""

            resp = query_llm(prompt)
            if not resp:
                return None
            choice = resp.strip().lower()
            normalized = [o.lower().strip() for o in options]
            if choice in normalized:
                return options[normalized.index(choice)]
            return None
        except Exception:
            return None

