## Sistema di gestione voci
## Questo file gestisce l'audio vocale dei personaggi

init python:
    # Variabile per abilitare/disabilitare le voci
    # persistent sopravvive tra le sessioni di gioco
    if not hasattr(persistent, 'voice_enabled'):
        persistent.voice_enabled = True
    
    def play_voice(audio_file):
        """Riproduce un file vocale solo se le voci sono abilitate"""
        if persistent.voice_enabled and audio_file:
            renpy.music.play(audio_file, channel="voice")

# Funzione helper per i dialoghi con voce
define narrator_voice = renpy.curry(play_voice)

## Esempi di utilizzo:
## 
## Metodo 1 - Usa il parametro voice direttamente:
##     voice "voice/anna_cap1_001.ogg"
##     anna "Ciao! Come stai?"
##
## Metodo 2 - Inline nel dialogo (solo se supportato dal character):
##     anna "Ciao! Come stai?" voice "voice/anna_cap1_001.ogg"
##
## STRUTTURA CONSIGLIATA PER I FILE VOCALI:
## voice/
##   ├── anna/
##   │   ├── cap1_001.ogg
##   │   ├── cap1_002.ogg
##   │   └── ...
##   ├── paolo/
##   │   ├── cap1_001.ogg
##   │   └── ...
##   ├── elisa/
##   └── altri_personaggi/
##
## FORMATI CONSIGLIATI:
## - OGG: buona compressione, qualità decente (consigliato)
## - WAV: qualità massima ma file più grandi
## - MP3: supportato ma OGG è preferibile
