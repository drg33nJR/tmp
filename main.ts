basic.forever(function on_forever() {
    music.play(music.stringPlayable("C5 E C5 D D F", 120), music.PlaybackMode.UntilDone)
})
basic.showLeds(`
# # # # #
# . #  . #
. . # . .
. . # . .
. . # . .
`)

