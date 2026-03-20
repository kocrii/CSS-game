## ESEMPIO DI UTILIZZO VOCI
## Questo è un esempio di come usare le voci registrate nei tuoi capitoli

label esempio_voci:
    
    # Scena con voci multiple
    scene corridoio_scuola
    
    # Primo dialogo con voce
    voice "voice/anna/cap1_001.ogg"
    anna "Ehi! Ti stavo cercando!"
    
    # Risposta del protagonista
    voice "voice/protagonista/cap1_001.ogg"
    "Davvero? Che succede?"
    
    # Altro personaggio
    voice "voice/paolo/cap1_001.ogg"
    paolo "Anna ha ragione, dobbiamo parlarti."
    
    # Dialogo senza voce (opzionale)
    anna "..." # Nessuna voce per pause o pensieri
    
    # Continua con voci
    voice "voice/anna/cap1_002.ogg"
    anna "È una cosa seria, riguarda Elisa."
    
    menu:
        "Cosa volete dirmi?"
        
        "Dimmi tutto":
            voice "voice/anna/cap1_003.ogg"
            anna "Ok, ascolta bene..."
            
        "Non ho tempo":
            voice "voice/paolo/cap1_002.ogg"
            paolo "Ma è importante!"
    
    return

## TIPS:
## 1. Il comando voice va SEMPRE prima del dialogo
## 2. Se non specifichi voice, il dialogo sarà silenzioso
## 3. Le voci si fermano automaticamente al dialogo successivo
## 4. Il giocatore può saltare la voce cliccando (come il testo)
