define Elisa = Character('Elisa', color="#00cc00")
define cyberbullo = Character('Cyberbullo', image= "cyberbullo1.png", color="#CD0000")

screen simple_stats_screen:
    frame:
        xalign 0.01 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Elisa" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value elisa_hp
                    range elisa_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[elisa_hp] / [elisa_max_hp]" size 16


    frame:
        xalign 0.99 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Cyberbullo" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value cyberbullo_hp
                    range cyberbullo_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[cyberbullo_hp] / [cyberbullo_max_hp]" size 16

    text "Elisa vs. Cyberbullo" xalign 0.5 yalign 0.05 size 30

# The game starts here.
label battle_game_1:
    hide screen gameUI
    hide screen bagUI
    stop music fadeout 1.0
    #play music "audio/Battle Theme.mp3" fadein 1.0 volume 0.4
    #### Some variables that describes the game state.
    $ cyberbullo_max_hp = 30
    $ elisa_max_hp = 40
    $ cyberbullo_hp = cyberbullo_max_hp
    $ elisa_hp = elisa_max_hp
    #$ cyberbullo_left = 13
    $ cookies_left = 13
    scene fight

    "Ciao piccola Elisa. Questo e' un piccolo virus all'interno del tuo cellulare."
    "Per vincere devi distruggere il cyberbullo e attaccarlo ripetutamente"
    "Puoi aiutarti con dei biscotti ma non so quanto possano rigenerarti."
    "Il cyberbullo decide di attaccarti, {w}e a quel punto..."
    jump battle_1_loop


label battle_1_loop:

    #### Let's show the game screen.
    #
    show screen simple_stats_screen

    #### The game loop.
    # It will exist till both enemies have more than 0 hp.
    #
    while (cyberbullo_hp > 0) and (elisa_hp > 0):

        menu:
            "Attacca":
                $ cyberbullo_hp -= 2
                #play audio "audio/frog punch.ogg" volume 1.0
                elisa "K-y-aaa!!! (Danno Inflitto: 2)"

            "Mangia un biscotto (biscotti rimasti: [cookies_left])" if cookies_left > 0:
                if prevenzione >= 5:
                    $ elisa_hp = min(elisa_hp+5, elisa_max_hp)
                    $ cookies_left -= 1
                    #play audio "audio/munch sound.ogg" volume 1.0
                    elisa "Mmm, squisiti!... (hp Rigenerati: 5)"
                else:
                    elisa "Non hai abbastanza punti prevenzione per rigenerarti con i biscotti!"

        $ cyberbullo_damage = renpy.random.randint(1, 6)
        #play audio "audio/sword sound.mp3" volume 1.0

        $ elisa_hp -= cyberbullo_damage

        cyberbullo "RrrrrRRrrrr! {i}Prendi questooo!{/i} (Danno inflitto: [cyberbullo_damage])"
    #
    ####

    hide screen simple_stats_screen


    if cyberbullo_hp <= 0:
        if elisa_hp <= 0:
            "* Prima di morire il nemico lancia la sua spada... *"
            "Doppio KO"
        else:
            if prevenzione >= 5:
                #play audio "audio/win sound.ogg" volume 1.0
                elisa "Ho vinto!"
                elisa "Sparisci adesso!!!"
                elisa "Mi sono rimasti solo [cookies_left] biscotti"
                jump fine_capitolo1_scenario2
            else:
                elisa "Non hai abbastanza punti prevenzione per vincere!"
                elisa "I biscotti non sono bastati... Riprova ad aumentare i tuoi punti prevenzione."
                jump fine_capitolo1_scenario1
    else:
        cyberbullo "Ah-Ah-Ah {i}Cosa credevi di fare?{/i}"
        jump fine_capitolo1_scenario1

#label battle_1_ending:
#   "Fine"
#    stop music fadeout 1.0
#    jump afterGame
    #return
