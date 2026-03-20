# CARTELLA VOCI - Istruzioni

## Organizzazione File

Organizza i file audio vocali in sottocartelle per personaggio:

```
voice/
├── anna/
│   ├── cap1_001.ogg
│   ├── cap1_002.ogg
│   └── ...
├── paolo/
│   ├── cap1_001.ogg
│   └── ...
├── elisa/
│   ├── cap1_001.ogg
│   └── ...
└── altri_personaggi/
```

## Convenzione Nomi File

Usa questo formato: `[personaggio]/cap[numero]_[sequenza].ogg`

Esempi:
- anna/cap1_001.ogg
- paolo/cap2_015.ogg
- elisa/cap1_003.ogg

## Come Usare le Voci nei Dialoghi

Nel tuo file .rpy, aggiungi il comando `voice` prima del dialogo:

```renpy
# Esempio 1 - Dialogo singolo
voice "voice/anna/cap1_001.ogg"
anna "Ciao! Come stai?"

# Esempio 2 - Più dialoghi consecutivi
voice "voice/paolo/cap1_001.ogg"
paolo "Ehi, aspetta!"

voice "voice/paolo/cap1_002.ogg"
paolo "Ti devo dire una cosa importante."
```

## Formati Audio Consigliati

1. **OGG Vorbis** (CONSIGLIATO)
   - Buona compressione
   - Qualità decente
   - Ottimo supporto Ren'Py
   
2. **WAV**
   - Qualità massima
   - File molto grandi
   - Usa solo se necessario

3. **MP3**
   - Supportato ma OGG è meglio

## Consigli per la Registrazione

- Registra in un ambiente silenzioso
- Usa un microfono decente (anche smartphone va bene)
- Mantieni la stessa distanza dal microfono
- Fai più take e scegli la migliore
- Normalizza l'audio per volume consistente

## Software Gratuiti per Editing Audio

- **Audacity** (gratuito, open source) - per editing e normalizzazione
- **OBS Studio** - per registrazione
- Converti in OGG con Audacity: File > Export > Export as OGG Vorbis

## Toggle Voci nel Gioco

Il giocatore può abilitare/disabilitare le voci nelle Preferenze > Audio > "Voci Personaggi"
Il volume delle voci si controlla con lo slider "Voice Volume" nelle preferenze.
