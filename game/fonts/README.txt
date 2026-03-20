Add a custom font (Brindan Write)

1) Obtain the Brindan Write TTF file (e.g. "BrindanWrite.ttf"). Ensure you have the right to use/distribute it.

2) Place the TTF file in this folder:
   game/fonts/BrindanWrite.ttf

3) The project `gui.rpy` is already configured to use this file as the
   main UI font (variable `gui.text_font`). If the file is missing,
   Ren'Py will try to fall back to a default font but you may see a
   warning in the launcher console.

4) If you want to use a different font filename, edit `game/gui.rpy` and
   change the three lines that set `gui.text_font`, `gui.name_text_font`,
   and `gui.interface_text_font`.

5) Restart Ren'Py / relaunch the game to see the new font applied.

If you'd like, upload the TTF here (or tell me the exact filename) and I
can check/update the project to ensure the font is applied consistently.