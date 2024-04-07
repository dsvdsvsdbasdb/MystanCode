"""
File: PotholeFilling.py
Name: ShinRu Yang
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: karel is at the (2, 1)
    Past-condition: karel is at the (2, 7)
    """

    for i in range(3):
        go_in()
        put_99()
        go_out()

def put_99():
    """
    karel will put 99 beepers
    """
    for i in  range(99):
        put_beeper()


def go_out():
    """
    Pre-condition: karel is at the upper left, facing South
    Past-condition: karel is at the upper left, facing East
    """
    turn_around()
    move()
    turn_right()
    move()


def go_in():
    """
    Pre-condition: karel is at the upper left, facing East
    Past-condition: karel is in the potnale, facing South
    """
    move()
    turn_right()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


















# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
