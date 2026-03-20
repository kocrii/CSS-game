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
        if phase == "initial":
                phase_instructions = "Rispondi in tono provocatorio, fai capire che hai il controllo del suo account. Rispondi sempre con massimo due frasi, rivolgendoti a lei stessa."
        if phase == "manipulative":
                phase_instructions = """Inizia a manipolare la vittima, ad esempio dicendo che hai informazioni su di lei, o che puoi fare cose al suo account. 
                Sfrutta le informazioni che hai su di lei per renderlo più credibile. L'obiettivo è farla sentire confusa, isolata e dipendente da te, in modo da poterla manipolare più facilmente. Rispondi sempre con massimo due frasi, rivolgendoti a lei stessa."""
        elif phase == "threatening":
                phase_instructions = "Ora devi minacciare la protagonista: chiedigli di fare qualcosa di specifico (es. portare soldi, venire in un posto), altrimenti pubblicherai foto imbarazzanti. Mantieni la pressione, ma senza esagerare. Mantieni la minaccia credibile e vicina alla realtà, senza sembrare troppo estrema o irreale. Devi mantenere la coerenza con quello che dici nelle fasi precedenti, e sfruttare le informazioni che hai su di lei per rendere la minaccia più efficace. Rispondi sempre con massimo due frasi."
            #cerca di essere conciso
            #richiamo label parco e riappare telefono? o sfida con l'hacker minigioco
            #ne faccio massimo altre 2 di chiamate al phone 
        elif phase == "final":
                phase_instructions = """Devi minacciare la protagonista in modo più diretto e aggressivo, sempre manipolatorio, 
                e dirgli di venire al campetto stasera alle 20 altrimenti continuerai a divertirti con il suo account e 
                a rovinargli la reputazione. Rispondi sempre con massimo due frasi.
                Sfrutta tutte le informazioni che hai su di lei per rendere la minaccia più efficace e personale possibile. 
                Se nelle fasi precedenti hai fatto promesse o minacce, richiamale ora per aumentare la pressione.
                Dai un ultimatum con una scadenza precisa."""
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
