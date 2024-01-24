def on_forever():
    music.play(music.string_playable("C5 E C5 D D F", 120),
        music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
basic.show_leds("""
# # # # #
# . #  . #
. . # . .
. . # . .
. . # . .
""")
basic.show_leds