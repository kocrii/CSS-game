# Main script for the demo!

define anna = Character("Anna", image="anna.png",color="#f44")
define elisa = Character ("Elisa", image= "elisa_felice", color = "#02d502")
define paolo = Character("Paolo", image= "paolo.png", color = "#ba1084")
define studenti = Character("Studenti", color = "#0ec4d466")
define preside = Character("Preside", color = "#1b0ba766")
define sconosciuto = Character("Sconosciuto", color = "#2e49d066")
define aiutante = Character("Miao", image="aiutante.png", color="#9d06ab")

# transform scale_bg:
#     zoom 0.8  # riduce all'80% (puoi aumentare o diminuire)
#     xalign 0.5
#     yalign 0.5

transform character_size:
    size (900, 900)

# NVL characters are used for the phone texting
define n_nvl = Character("Io", kind=nvl, image="nighten", callback=Phone_SendSound)
#define e_nvl = Character("Caio", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# NOTE: Ren'Py's default main menu screen is provided by `screens.rpy`.
# The project previously defined a `label main_menu`, which overrides the
# engine's normal main menu. Rename this label to preserve the default
# main menu and keep an entry point that jumps into the game's chapter
# selection when desired.

# Entry point used by the game to show the chapter selection (was `main_menu`).
label start:
    show aiutante at left, character_size:
        xzoom 0.85 
        yzoom 1.25
    aiutante "Ciao, benvenuto! Io sono Miao e ti aiuterò a navigare attraverso questo Serious Game sulla Cyber Social Security."
    aiutante "Il gioco inizia con il primo capitolo, che tratta una tematica legata al mondo della sicurezza, in particolare al cyberbullismo."
    "Il videogioco è suddiviso in varie scene interattive, in cui potrai prendere delle decisioni che influenzeranno lo svolgimento della storia."
    "Buon divertimento!"

    
    #jump phone_chat
    "Vuoi iniziare?"
    hide aiutante with dissolve
    menu:
        "Capitolo 1: cyberbullismo":
            jump capitolo1

    jump game


label game:
    scene bg village with dissolve
    pause 1.0

    show anna at left, character_size:
        yoffset 1080
        ease 0.7 yoffset 0
    anna "sono kocri"
    hide anna with dissolve

    show anna at left, character_size:
    anna e1m2 "prova 2"
    anna phone e1m1 "prova 3"
    hide anna with dissolve

    # Phone conversation start: jump to reusable conversation module
    #jump phone_chat

label question:
    menu:
        "Nothing, have a good day!":
            jump end

label end:
    anna e2m2 "CIAO DIO"
    #a e1m2 "If you still have some questions, don't hesitate to message me on Discord {i}(Nighten#3081){/i}!"
    $ renpy.quit()

    