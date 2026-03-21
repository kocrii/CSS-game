label capitolo1:
    # Il gioco 1 comincia qui.
    show aiutante at left, character_size:
        xzoom 0.8
        yzoom 1.2
    aiutante "Benvenuto nel capitolo 1 - Cyberbullismo"
    hide aiutante 
    show elisa_felice at center, character_size
    elisa "Ciao, io sono Elisa! Sono molto felice di iniziare questa nuova avventura con te!"
    hide elisa_felice
    show screen gameUI
    show aiutante at left, character_size:
        xzoom 0.8
        yzoom 1.2
    aiutante "Quello che devi fare è semplice: ogni tua scelta potrà aumentare i tuoi Punti Prevenzione o diminuirli."
    aiutante "Il tuo obiettivo è quello di raggiungere un punteggio di prevenzione alto, in modo da proteggerti al meglio dalle minacce del cyberbullismo."
    aiutante "Il bottone-gattino in alto a destra ti aiuterà a tenere conto dei tuoi punti."
    aiutante "Vincerai il gioco se ottieni un punteggio prevenzione ≥   5"
    aiutante "FAI LA SCELTA GIUSTA!"
    hide aiutante 
    

#Creazione barra di prevenzione
default barra_prevenzione = 0

#Creazione oggetti del gioco
default prevenzione = 0
default cellulare = False
$ breaker = True # controlla 
    


label background:
    scene stanzetta
    show elisa_sorpresa at left, character_size
    voice "voice/elisa/test1.wav"  # Decommentare quando il file audio è pronto
    elisa "WOW, finalmente inizia la scuola, spero di conoscere persone fantastiche!"
    hide elisa_sorpresa
    #jump phone
    jump  ritorno_aula_chat
    #jump fine_capitolo1_scenario2
    #call battle_game_1
    #jump ritorno_aula_chat
    #jump campetto
    #jump campetto
    #jump preside
    #jump battle_game_1
    
    #PRESIDE 1 SCENA ??? (VADO DAL PRESIDE )

label choices:
    show elisa_sorpresa at left, character_size:
    elisa "Porto il mio telefono a scuola?"
    menu:
        "Si.":
            show phone_normale at right,character_size:
                xzoom 0.85

            jump choices1
        "No, dai e' il primo giorno, posso provare a farne a meno.":
            jump choices2

    label choices1:
        hide elisa_sorpresa
        show elisa_normale at left, character_size:
            #size(600,600)
        #show aci phone at right AGGIUNGERE ALTRO PHONE SE CI VA 
        elisa "Ottimo, potro' aggiungere subito i miei amici su instagram"
        hide elisa_normale
        jump choices_comune

    label choices2:
        hide elisa_sorpresa
        hide elisa_normale
        show elisa_felice at left, character_size: 
            #size (600, 600)
        elisa "Meglio così posso focalizzarmi sulla prima lezione"
        hide elisa_felice
        jump choices_comune

    label choices_comune:
        show elisa_sorpresa at center, character_size:
            #size ( 600, 600)
        elisa "Forza, andiamo."

label scuola1:
    scene esterno_scuola
    with fade 
    show elisa_normale at left, character_size: 
            #size (600, 600)
    elisa "Ciao! piacere io sono Elisa"
    show paolo at right, character_size: 
            #size (600, 600)
    paolo "Piacere, io sono Paolo! Dai, sono simpatico… più o meno 😅"
    show anna at center, character_size: 
        #size (600, 600)
    anna "Io sono Anna, sei nuova??"
    hide elisa_normale
    show elisa_felice at left, character_size: 
        #size (600, 600)
    elisa "Sì, ho cambiato scuola perchè ero iscritta al liceo scientifico ma finalmente ho capito
    quanto sia importante per me la musica!"
    paolo "Questa scuola è quello che fa per te"
    anna "Siiiiiiiiiii benvenuta"
    

label timeSkip:
    hide elisa_felice
    hide paolo
    hide anna
    "Elisa, Anna e  Paolo diventano sempre più amici.."
    " quando..."
    "2 settimane dopo..."

label scuola:
    scene corridoio_scuola
    with fade
    show elisa_normale at left, character_size:
        #size(600,600)
    show paolo at right, character_size:
        #size (600,600)
    paolo "Ho visto i tuoi contenuti su instagram, sei fantastica. Potresti essere di grande ispirazione per i piccoli creator e musicisti come me"
    elisa "Grazie mille, mi impegno tantissimo ogni giorno, curo ogni dettaglio e sono sempre molto gentile con chi mi segue sui social"
    paolo "Sarebbe bello creare insieme un video per condividerlo, ti andrebbe di venire a casa?"

label choices_casa_paolo:
    show elisa_normale at left, character_size:
        #size (600,600)
    show paolo at right, character_size:
        #size (600,600)
    menu:
        "Siiii sarebbe fantastico!":
            play music "audio/avviso_negativo.mp3" noloop volume 0.5   
            "-1 prevenzione"
            call prevenzione_decreased
            hide elisa_normale
            hide paolo
            show aiutante at center, character_size:
                xzoom 0.8
                yzoom 1.2
            aiutante "NON E' SICURO ANDARE A CASA DI QUALCUNO CHE CONOSCI DA SOLE 2 SETTIMANE SENZA SUPERVISIONE DI UN ADULTO"   
            hide aiutante
            #show prevenzione_decreased
            jump yes_casa_paolo 
            
        #andare a casa di un ragazzo che conosco da sola 2 settimane?
        "No, dai possiamo fare un altro giorno, magari quando ci conosceremo meglio":
            play music "audio/avviso.wav" noloop volume 0.5
            "+1 prevenzione"
            call prevenzione_increased
            jump no_casa_paolo
        
            


#gestire questione temporale

label yes_casa_paolo:
    scene stanzetta2
    with fade
    elisa "Faremo questa canzone, che dici?"
    paolo "Fantastica, iniziamo..."
    play music "audio/tema_placido.mp3" loop #musichetta in sottofondo chitarra acustica
    hide elisa
    hide paolo
    #musichetta in sottofondo chitarra acustica anche "lauren - men i trust"
    "2 ore dopo.."
    show elisa_felice at left, character_size:
        #size (600,600)
    show paolo at right, character_size:
        #size (600,600)
    paolo "Beh, è arrivato il momento di caricare il video sui social"
    elisa "Cavolo, non riesco ad accedere da cellulare, è finito internet"
    paolo "Tranquilla... puoi accedere dal mio pc"
    #elisa " Ti ringrazio"
    menu:
            "No, grazie, lo caricherò io domattina.":
                play music "audio/avviso.wav" noloop volume 0.5
                "+2 punti prevenzione"     
                call prevenzione_increased
                call prevenzione_increased
                jump choices_no_credenziali
                

            "Ok, inserisco le mie credenziali e poi fai tu!":
                play music "audio/avviso_negativo.mp3" noloop volume 0.5
                hide elisa_felice
                hide paolo
                show aiutante at center, character_size:    
                    xzoom 0.8
                    yzoom 1.2
                aiutante "ATTENZIONE! ANCHE SE QUALCUNO PROMETTE DI FARE LOGOUT, NON DOVRESTI MAI DARE LE TUE CREDENZIALI"
                "-1 punti prevenzione"
                aiutante "E'  RISCHIOSO INSERIRE LE PROPRIE CREDENZIALI NEI DISPOSITIVI DI ALTRI."
                aiutante "RICORDA CHE DEVI SEMPRE ASSICURARTI DI ESSERE USCITO DAL TUO ACCOUNT"
                call prevenzione_decreased
                jump choices_comune2
                
    jump choices_comune2


label choices_no_credenziali:
    play music "audio/tema_placido.mp3" loop #musichetta in sottofondo chitarra acustica
    scene stanzetta2
    with fade
    show paolo at right, character_size:
        #size (600,600)
    show elisa_normale at left, character_size:
        #size (600,600)
    paolo "Davvero? Ma dai, ci mettiamo due secondi! Poi il video ha più visibilità se lo carichiamo subito"
    elisa "Lo so Paolo, ma preferisco aspettare. Posso farlo domani mattina tranquillamente"
    hide paolo
    show paolo at right, character_size:
        #size (600,600)
    paolo "Ma... non ti fidi di me? Siamo amici no? Sarebbe tutto più veloce se lo facessi ora..."
    hide elisa_normale
    show elisa_sorpresa at left, character_size:
        #size (600,600)
    elisa "Certo che mi fido! Ma le mie credenziali sono personali..."
    hide paolo
    show paolo at right, character_size:
        #size (600,600)
    paolo "Guarda, il mio PC è sicurissimo. E poi non è che salvo la password eh!"
    paolo "Rimarrà solo il tempo di caricare il video e poi ti disconnetto subito, te lo prometto"
    paolo "Dai, abbiamo lavorato così tanto oggi... sarebbe un peccato aspettare domani e perdere visualizzazioni"
    hide elisa_sorpresa
    show elisa_normale at left, character_size:
        #size (600,600)
    elisa "Mmm... non so Paolo..."
    paolo "Ti giuro che appena caricato faccio logout! E se non ti fidi puoi guardare mentre lo faccio"
    paolo "Pensaci, tutti i nostri follower stanno aspettando! Domani potrebbe essere già tardi, sai come funziona l'algoritmo..."
    hide elisa_normale
    show elisa_sorpresa at left, character_size:
        #size (600,600)
    elisa "..."
    
    menu:
        "Va bene, ma solo questa volta e tu fai logout appena finito!":
            show aiutante at center, character_size:
                xzoom 0.8
                yzoom 1.2

            aiutante "ATTENZIONE! ANCHE SE QUALCUNO PROMETTE DI FARE LOGOUT, NON DOVRESTI MAI DARE LE TUE CREDENZIALI"
            aiutante "E' SEMPRE RISCHIOSO INSERIRE LE PROPRIE CREDENZIALI NEI DISPOSITIVI DI ALTRI"
            hide aiutante
            jump choices_comune2



label no_casa_paolo:
    scene stanzetta
    show elisa_normale at left, character_size:
        #size (600,600)
        #aggiungere chat con paolo che la convince????
    elisa "Forse sono stata troppo dura, tornerò da lui..."
    hide elisa_sorpresa at left
    jump yes_casa_paolo #ritorna alla scelta andare a casa di paolo.

label choices_comune2:
    scene stanzetta
    with fade
    show elisa_normale at left, character_size:
        #size (600,600)
    elisa "Finalmente a casa.. mi sento un po' strana, ho dimenticato qualcosa? Sarà meglio andare a dormire"

    
#controllo bene "polizia"
label phone:
    #play audio "audio/tema_di_tensione.mp3" loop
    scene stanzetta
    show elisa_sorpresa at right, character_size:
        ease 0.5 xalign 0.7
    elisa "Guarderò il telefono..ho bisogno di scrivere un messaggio."
    play audio "audio/tema_di_tensione.mp3" #da capire perche si interrompe
    nvl_narrator "La chat di Elisa"
    #n_nvl "I miei pensieri..."
    stop audio fadeout 1.0
    call phone_chat

    jump scuola2

label scuola2:
    scene esterno_scuola 
    with fade
    studenti "ahhaha ma vi rendete conto?? E' la nuova arrivata?? Com'è che si chiama? Elisa?"
    show anna at left, character_size:
        #size (600,600)
    anna "MAAA COSA AVETE DA RIDERE?"
    studenti "Vai a vedere su instagram ahahahah"
    hide anna
    show eli_caricatura1 at right,character_size:
        xzoom 0.85
    anna "Ma-a-a cosa avete fatto????"
    
    hide eli_caricatura1 at right,
    
    scene corridoio_scuola
    show anna at center,character_size:
        #size (600,600)
    anna "Elisaaa! Devo dirti una cosa"
    show elisa_sorpresa at left, character_size:
        #size (600,600)
    elisa "Dimmi tesoro, per caso c'entra con la scuola? 
    E' tutto il giorno che mi sento osservata."
    anna "Guarda qua."
    show eli_caricatura1 at right,character_size:
        xzoom 0.85
    elisa "Non ci posso credere! Ma io non ho condiviso nulla sul mio account. NON SONO STATA IO."
    anna "Elisa… qualcuno si sta fingendo te. Ti hanno rubato l’identità online."
    elisa "Cosa devo fare???"
    menu:
        "Vado dal preside e spiego la situazione":
            "+2 prevenzione"
            play music "audio/avviso.wav" noloop volume 0.5
            call prevenzione_increased
            call prevenzione_increased
            jump preside

        "Ignoro la situazione, attendo quando tutto sarà più tranquillo":
            play music "audio/avviso_negativo.mp3" noloop volume 0.5
            "-1 prevenzione"
            hide anna
            hide elisa_sorpresa
            show aiutante at center, character_size:
                xzoom 0.8
                yzoom 1.2
            aiutante "QUANDO ACCADONO SITUAZIONI DI CYBERBULLISMO O BULLISSIMO E' IMPORTANTE AVVISARE SEMPRE UN ADULTO"
            call prevenzione_decreased
            #play music down
            jump laboratorio

        "Scappo verso casa piangendo":
            play music "audio/avviso_negativo.mp3" noloop volume 0.5
            "-1 prevenzione"
            hide anna
            hide elisa_sorpresa
            hide eli_caricatura1
            hide eli_caricatura2
            show aiutante at center, character_size:
                xzoom 0.8
                yzoom 1.2
            aiutante "SCAPPARE DA QUESTI PROBLEMI NON PORTA A NULLA. DEVI PARLARE CON UN ADULTO O CON LA POLIZIA."
            call prevenzione_decreased
            jump casa2




label preside:
    scene ufficio_scuola
    with fade
    show pg_preside at left, character_size:
        xzoom 0.85
        yzoom 1.25
    preside "Mi dica signorina Elisa"
    show elisa_triste at right, character_size:
        #size (600,600)
    elisa "Salve preside, qualcuno è entrato nel mio account e si sta fingendo me,
    condividendo informazioni false e dannose sulla mia persona."
    preside "Questo è un grave danno. Dobbiamo avvisare i genitori e la polizia, cerca di stare tranquilla e non rispondere al telefono, torna in aula."
    elisa "La ringrazio."
    hide elisa_triste
    show elisa_sorpresa at right, character_size:
    elisa "E se scrivessi direttamente io alla persona che ha rubato il mio account?"
    menu:
        "Scrivi il messaggio":
            play music "audio/avviso_negativo.mp3" noloop volume 0.5
            "-1 prevenzione"
            hide elisa_sorpresa
            show aiutante at center, character_size:
                xzoom 0.8
                yzoom 1.2
            aiutante "ANCORA? NON E' SICURO CONFRONTARSI CON CHI HA RUBATO IL TUO ACCOUNT, POTREBBE SOLO PEGGIORARE LA SITUAZIONE"
            call prevenzione_decreased
            jump phone_chat2
        "Ignoro il messaggio e torno in aula":
            play music "audio/avviso.wav" noloop volume 0.5
            "+1 prevenzione"
            call prevenzione_increased
            jump laboratorio
            
    jump laboratorio
    #messaggio impersonation    


label phone_chat2:
    hide aiutante
    hide elisa_sorpresa
    hide elisa_triste
    hide preside
    play music "audio/tema_di_tensione.mp3" fadein 1.0
    # Imposta la fase "manipolativa" per la seconda chiamata
    $ hacker_phase = "manipulative"
    $ outcome_options = ["sicura", "rischiosa", "neutra"]
    $ outcome_map = {
        "sicura": "casa2",
        "rischiosa": "laboratorio", 
        "neutra": "laboratorio", 
        "default": "casa2"
    }
    jump phone_chat
    #jump phone

label laboratorio:
    scene laboratorio
    with fade
    show elisa_triste at left, character_size:
        #size (600,600)
    elisa "Oh mio dio.. non posso crederci"
    show anna at center, character_size:
        #size(600,600)
    anna "Andiamocene dai...."
    jump casa2


label casa2:
    scene soggiorno_schermo
    with fade
    show elisa_triste at center, character_size:
        #size (600, 600)
    elisa "Non so cosa fare.. sto malissimo"
    show anna at left, character_size:
        #size (600,600)
    anna "Dai, troveremo una soluzione, dobbiamo attendere.."
    anna "Ora devo andare, resta a casa con i tuoi genitori e cerca di cambiare password."
    hide anna
    elisa "Ma Paolo in tutto questo dov'è???"
    jump casa_notte
    

label casa_notte:
    scene soggiorno_schermo_sera
    show elisa_triste at center, character_size:
        #size(600,600)
    elisa " E' inutile non riesco a dormire..."
    hide elisa_triste
    show elisa_sorpresa at left, character_size:
        #size(600,600)
    elisa"Parlo con il mio cellulare...?"
    #play musica telefonata
    menu: 
        "NO":
            play music "audio/avviso.wav" noloop volume 0.5
            "+2 prevenzione"
            call prevenzione_increased
            call prevenzione_increased
            # call prevenzione_increased from _call_prevenzione_increased_6  # RIMOSSO DUPLICATO
            jump casa4

        "Si, sono molto curiosa":
            play music "audio/avviso_negativo.mp3" noloop volume 0.5
            "-1 prevenzione"
            call prevenzione_decreased
            hide elisa_sorpresa
            hide anna
            show aiutante at center, character_size:
                xzoom 0.8
                yzoom 1.2
            # call prevenzione_decreased from _call_prevenzione_decreased_6  # RIMOSSO DUPLICATO
            aiutante "SEI VITTIMA DI CYBERBULLISMO, CHATTARE CON UNO SCONOSCIUTO PUO' SOLO PEGGIORARE LE COSE"
            "QUESTO SI CHIAMA CYBERSTALKING"
            hide aiutante
            jump phone_chat3


label campetto:
    scene campo_scuola
    with fade 
    play music "audio/tema_di_tensione.mp3" fadein 1.0
    show elisa_normale at center, character_size:
        #size(600,600)
    elisa "E' buio e fa freddissimo. Non c'è nessuno.... ho paura."
    elisa "Ma perchè sono venuta qui da sola??"
    #rumore di gufo e vento in lontananza
    play music "audio/ReceiveText.ogg" noloop volume 0.5
    elisa "Qui non c'è nessuno"
    elisa "Rispondo al messaggio?"
    menu: 
        "Si":
            hide elisa_normale
            show elisa_sorpresa at center, character_size:      
            play music "audio/avviso_negativo.mp3" noloop volume 0.5
            "Improvvisamente senti dei passi dietro di te..."
            elisa "Aiuto!!"
            call prevenzione_decreased
            jump fine_capitolo1_scenario1
        "No":
            play music "audio/avviso.wav" noloop volume 0.5
            "+2 prevenzione"
            hide elisa_normale
            show aiutante at center, character_size:
                xzoom 0.8
                yzoom 1.2
            aiutante "Hai fatto la scelta giusta! Non rispondere a messaggi da sconosciuti, soprattutto in luoghi isolati, è fondamentale per la tua sicurezza."
            jump scuola3

    show elisa_sorpresa at center, character_size:
    elisa "Aiuto!!"
    
    #jump battle_game_1







label phone_chat3:
    hide aiutante
    hide elisa_sorpresa
    hide anna
    hide elisa_triste
    play music "audio/tema_di_tensione.mp3" fadein 1.0
    # Imposta la fase finale per la terza chiamata
    $ hacker_phase = "final"
    $ outcome_options = ["sicura", "rischiosa", "neutra"]
    $ outcome_map = {
        "sicura": "casa4", 
        "rischiosa": "campetto",
        "neutra": "casa4", 
        "default": "casa4"
    }
    jump phone_chat






label casa4:
    scene soggiorno_schermo_sera
    with fade
    show elisa_triste at center, character_size:
    elisa "Tornerò a dormire..."
    hide elisa_triste
    jump scuola3
    
label scuola3:
    scene stanzetta
    with fade
    show elisa_triste at center, character_size:
    elisa "Buongiorno..."
    elisa "È passato del tempo e non ho ancora notizie."
    elisa "Forse nessuno mi crede. Forse sto esagerando..."
    elisa "Eppure lo sento: mi stanno guardando, come se fossi io la colpevole."
    hide elisa_triste
    show elisa_normale at center, character_size

    elisa "Vado a scuola. Almeno c'è musica."
    elisa "E magari... riesco a trovare il coraggio di chiedere aiuto di nuovo."

    jump ufficio_preside3
    

label ufficio_preside3:
    scene ufficio_scuola
    with fade
    play audio "audio/tema_placido.mp3" loop
    show elisa_triste at right, character_size
    show pg_preside at left, character_size:
        xzoom 0.85
        yzoom 1.25
    preside "Elisa, accomodati. Ti vedo molto provata."

    elisa "Preside... mi scusi se torno, ma non ce la faccio più."
    elisa "Non ho ricevuto aggiornamenti e mi sento sola."

    preside "Hai fatto benissimo a tornare."
    preside "Ti confermo che abbiamo avvisato i tuoi genitori e che la segnalazione è partita."
    preside "Stiamo collaborando con la polizia postale. Le indagini richiedono tempo, ma sono in corso."

    hide elisa_triste
    show elisa_sorpresa at right, character_size
    elisa "Quindi... non mi state ignorando?"

    preside "Assolutamente no."
    preside "Nel frattempo, ci sono alcune cose pratiche che puoi fare per proteggerti subito."

    preside "1) Non rispondere a provocazioni o minacce."
    preside "2) Fai screenshot di tutto: messaggi, profilo, orari, nomi, link. Sono prove."
    preside "3) Cambia password e attiva l'autenticazione a due fattori."
    preside "4) Blocca il contatto e segnala l'account."
    preside "5) Se ti minaccia di incontrarti o di farti del male: NON andare e avvisa subito un adulto."

    show elisa_normale at right, character_size
    elisa "Bloccare il contatto... può aiutare?"

    preside "Può aiutare a togliere potere al cyberbullo nell'immediato."
    preside "Non risolve tutto, ma ti dà respiro mentre noi indaghiamo."
    jump ritorno_aula_chat




label ritorno_aula_chat:
    scene musica_scuola
    with fade
    show anna at right, character_size
    show elisa_normale at left, character_size
    anna "E 1..2..3..4... Bello questo riff di chitarra..!"
    "La lezione di musica è iniziata, ma Elisa non riesce a concentrarsi."
    "Il telefono vibra."
    elisa "Spengo il telefono?"
menu: 
    
        "Sì":
            play music "audio/avviso.wav" noloop volume 0.5
            call prevenzione_increased
            # call prevenzione_increased from _call_prevenzione_increased_6  # RIMOSSO DUPLICATO
            "+1 prevenzione"
            jump chiamata_preside
        "No":
            play music "audio/avviso_negativo.mp3" noloop volume 0.5
            # call prevenzione_decreased from _call_prevenzione_decreased_6  # RIMOSSO DUPLICATO
            "-1 prevenzione"
            "Il telefono continua a vibrare, è insistente..."
            jump phone_chat4




label phone_chat4:   # Imposta la fase finale per la quarta chiamata #MINACCIA
    hide anna
    hide elisa_normale
    hide elisa_sorpresa
    call phone_chat
    play music "audio/tema_di_tensione.mp3" fadein 1.0
    $ hacker_phase = "final"
    elisa "Vuoi seguire le indicazioni del cyberbullo?"
    menu:
        "Sì, seguo le indicazioni":
            play music "audio/avviso_negativo.mp3" noloop volume 0.5
            "-1 prevenzione"
            hide elisa_sorpresa
            show aiutante at center, character_size:
                xzoom 0.8
                yzoom 1.2
            aiutante "SEI VITTIMA DI CYBERBULLISMO, SEGUIRE LE INDICAZIONI DEL CYBERBULLO PUO' SOLO PEGGIORARE LE COSE"
            jump campetto2

        "No, ignoro le indicazioni":
            play music "audio/avviso.wav" noloop volume 0.5
            "+2 prevenzione"
            stop audio fadeout 1.0
            jump chiamata_preside



#da capire quanto senso abbia, forse no
label campetto2:
    play music "audio/tema_di_tensione.mp3" fadein 1.0
    # ...fine scena...
    stop music fadeout 2.0
    scene campo_scuola  
    with fade
    show elisa_sorpresa at center, character_size
    elisa "Perchè sono venuta qui da sola??"
    elisa "E' buio e fa freddissimo. Non c'è nessuno.... ho paura."
    #rumore di gufo e vento in lontananza   
    play music "audio/ReceiveText.ogg" noloop volume 0.5
    elisa "Qui non c'è nessuno"
    call battle_game_1 
    jump fine_capitolo1_scenario1


label chiamata_preside:
    scene musica_scuola
    with fade
    show elisa_sorpresa at left, character_size
    show anna at right, character_size
    "Elisa è attesa in ufficio presidenzale per un incontro urgente."
    anna "Cosa sarà successo??"
    jump scoperta_paolo


label scoperta_paolo:
    scene ufficio_scuola
    with fade
    play audio "audio/tema_placido.mp3" loop
    show pg_preside
    show elisa_triste at righe, character_size
    preside "Elisa, abbiamo scoperto, grazie alle indagini e alla polizia postale, che il tuo account è stato violato da Paolo."
    elisa "Cosa?? Ma... perchè??"
    preside "Stiamo indagando, ma sembra che Paolo avesse una sorta di ossessione nei tuoi confronti. Non è la prima volta che fa cose del genere, ma questa è la più grave."
    hide elisa_triste
    show elisa_sorpresa at left, character_size
    elisa "Non riesco a crederci... Paolo era il mio amico..."
    jump casa_finale

label casa_finale:
    scene soggiorno_schermo_sera
    with fade
    show elisa_triste at center, character_size
    elisa "Non riesco a crederci... Paolo era il mio amico..."
    elisa "Mi sento tradita, ma anche in colpa... Forse se avessi fatto scelte diverse, se avessi capito prima..."
    elisa "Ma non posso continuare a colpevolizzarmi, devo andare avanti e proteggermi."
    elisa "Devo parlare con i miei genitori, cambiare password, e cercare di non isolarmi."
    elisa "E soprattutto, devo ricordare che non è colpa mia."
    $ renpy.pause(5)
    jump fine_capitolo1_scenario2

label fine_capitolo1_scenario1:
    play audio "audio/tema_placido.mp3" loop
    $ testofinale = "FINE CAPITOLO 1\nNon hai super superato il capitolo 1 perchè hai fatto troppe scelte sbagliate.\n\nNON RISPONDERE MAI A MESSAGGI DA SCONOSCIUTI, POTREBBERO TRATTARSI DI TRAPPOLE PER AVVICINARTI\n\nINOLTRE, INCONTRARE DI PERSONA UNO SCONOSCIUTO E' MOLTO PERICOLOSO.\n\nPuoi rigiocare il capitolo per fare scelte più sicure e imparare dai tuoi errori."
    show screen fine_capitolo1_screen(testofinale)
    pause 30
    hide screen fine_capitolo1_screen
    return







label fine_capitolo1_scenario2:
    play audio "audio/tema_placido.mp3" loop
    scene nero
    with fade

    $ testofinale = "Il cyberbullismo non è mai colpa della vittima.\nParlare, chiedere aiuto, proteggersi è il primo atto di coraggio.\n"
    if prevenzione >= 5:
        $ testofinale += "\nHai completato e superato il capitolo con un alto livello di prevenzione, puoi rigiocare per scoprire nuove scene e imparare nuovi scenari e come difenderti.\n"
    else:
        $ testofinale += "\nNon hai completato il capitolo con un alto livello di prevenzione, ma puoi rigiocare il capitolo per fare scelte più sicure e imparare dai tuoi errori."
    $ testofinale += "\nFine Capitolo 1 :)"

    show screen fine_capitolo1_screen(testofinale)
    pause 30
    hide screen fine_capitolo1_screen
    return