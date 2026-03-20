label capitolo2:
    "Benvenuto nel capitolo 2 - Revenge Porn"
    # -> qui la storia del capitolo
    jump end_chapter



label end_chapter:
    show anna at left, character_size
    a "Questo è un serious game basato su..."
    hide anna
    menu:
        "Vuoi continuare a giocare?"

        "Torna al menu dei capitoli":
            jump main_menu_game

        "Esci dal gioco":
            $ renpy.quit()
        
