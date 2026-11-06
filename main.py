def on_button_pressed_a():
    Num2[0] = "" + Num2[0] + "1"
    basic.show_string("" + (Num2[0]))
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("Cargando")
    basic.pause(1000)
    basic.show_leds("""
        . . # . .
        . # # # .
        # . . . #
        # # # # #
        # . . . #
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . . .
        . # # # .
        . . . . .
        . # # # .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . # . .
        . # # . .
        . . # . .
        . . # . .
        . # # # .
        """)
    basic.pause(1000)
    basic.show_leds("""
        . # # # .
        . # . . #
        . # # # .
        . # . . #
        . # # # .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . . .
        . # # # .
        . . . . .
        . # # # .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . # . .
        . # . # .
        . # . # .
        . # . # .
        . . # . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        . . # . .
        . # # # .
        # . . . #
        # # # # #
        # . . . #
        """)
    basic.pause(200)
    basic.show_leds("""
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . # # # .
        . # . . #
        . # # # .
        . # . . #
        . # # # .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . . .
        . # # # .
        . . . . .
        . # # # .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        # # # # .
        # . . . #
        # # # # #
        # . # . .
        # . . # #
        """)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    if Num2[0] == "0111":
        basic.show_string("Correcto")
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
    else:
        basic.show_string("Incorrecto")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Num2[0] = "" + Num2[0] + "0"
    basic.show_string("" + (Num2[0]))
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

Num2: List[str] = []
Num2 = [""]
basic.show_string("Empezar: Sacude")