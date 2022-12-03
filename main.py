basic.show_number(1)
basic.show_number(2)
basic.show_number(3)

def on_forever():
    basic.show_leds("""
        . . . . .
                . . . . .
                # # . . #
                . # # # .
                . # . # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # . . # .
                # # # . .
                # . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                # # . . .
                . # . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . # . . .
                # . . . .
                # . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . # #
                . . . . #
                . . . . #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # # .
                . . . # #
                . . . # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . # # . .
                . . # # #
                . . # . #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # # . . #
                . # # # .
                . # . # .
    """)
basic.forever(on_forever)
