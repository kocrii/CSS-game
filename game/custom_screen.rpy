# Bottone Statistiche e Oggetti
screen gameUI():
    frame:
        background "#2228"
        xalign 0.95
        yalign 0.05
        padding (20, 10)
        hbox:
            spacing 15
            add "pulcino_stats_idle.png" yalign 0.5 xysize (60, 60)
            vbox:
                spacing 5
                text "Scudo Digitale: [prevenzione]/5" size 25 color "#00ff00"
                bar value prevenzione range 5 xsize 200

screen StatsUI:
    frame:
        #add "bg pink.png"
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "STATISTICHE:" size 30
                #text "{image=handshake.png}{alt}Amicizia{/alt}  Amicizia: [amicizia]" size 20 color "#99ff99"
                #text "{image=heart.png}{alt}Amore{/alt}  Amore: [amore]" size 20 color "#ffccff"
                text "{image=ungry.png}{alt}ungry{/alt}  Punti Prevenzione: [prevenzione]" size 30 color "#66ccff"
                #text "__________________" size 15
                #text "RISORSE:" size 10
                #text "{image=money.png}{alt}money{/alt}  Soldi: € [soldi]" size 20 color "#ffff99"
                #text "{image=essePoints.png}{alt}esse{/alt}  Punti Esse: [puntiEsse]" size 20 color "#cc66ff"

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -50
        yoffset 15
        idle "pulcino_stats_idle.png"
        hover "pulcino_stats_hover.png"
        action Return()

screen fine_capitolo1_screen(testofinale):
    add Solid("#ffe4fa")  # rosa pastello
    add Solid("#aee9f8") xpos 0 ypos 0 alpha 0.5
    add Solid("#fff9c4") xpos 0 ypos 0 alpha 0.3
    frame:
        background None
        xalign 0.5
        yalign 0.5
        padding (100, 100)
        vbox:
            spacing 40
            text testofinale color "#4b4b7a" size 50 xalign 0.5 yalign 0.5

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -50
        yoffset 15
        idle "pulcino_stats_idle.png"
        hover "pulcino_stats_hover.png"
        action Return()
