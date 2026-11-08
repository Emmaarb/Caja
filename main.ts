input.onButtonPressed(Button.A, function () {
    Num2[0] = "" + Num2[0] + "1"
    basic.showString("" + (Num2[0]))
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("Cargando")
    basic.pause(1000)
    basic.showLeds(`
        . . # . .
        . # # # .
        # . . . #
        # # # # #
        # . . . #
        `)
    basic.pause(200)
    basic.showLeds(`
        . . . . .
        . # # # .
        . . . . .
        . # # # .
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . # . .
        . # # . .
        . . # . .
        . . # . .
        . # # # .
        `)
    basic.pause(1000)
    basic.showLeds(`
        . # # # .
        . # . . #
        . # # # .
        . # . . #
        . # # # .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . . . .
        . # # # .
        . . . . .
        . # # # .
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . . # . .
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . # . .
        . # # # .
        # . . . #
        # # # # #
        # . . . #
        `)
    basic.pause(200)
    basic.showLeds(`
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . # # # .
        . # . . #
        . # # # .
        . # . . #
        . # # # .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . . . .
        . # # # .
        . . . . .
        . # # # .
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        # # # # .
        # . . . #
        # # # # #
        # . # . .
        # . . # #
        `)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    if (Num2[0] == "0111") {
        basic.showString("Correcto")
        Num2[0] = ""
        basic.showLeds(`
            . # . # .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
        basic.showString("Empezar: Sacude")
    } else {
        basic.showString("Incorrecto")
        Num2[0] = ""
        basic.showString("Empezar: Sacude")
    }
})
input.onButtonPressed(Button.B, function () {
    Num2[0] = "" + Num2[0] + "0"
    basic.showString("" + (Num2[0]))
    basic.pause(1000)
    basic.clearScreen()
})
let Num2: string[] = []
Num2 = [""]
basic.showString("Empezar: Sacude")
