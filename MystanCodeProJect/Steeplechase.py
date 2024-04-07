"""
File: Steeplechase.py
Name: ShinRu Yang
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    Pre-condition: karel is on the left side of the wall, facing East
    Post-conditionL: karel is on the right side of the wall
    """
    up()
    cross()
    down()


def down():
    """
    Pre-condition: karel is at the upper right, facing South
    Post-condition: karel is facing South
    """
    while front_is_clear():
        move()


def cross():
    """
    Pre-condition: karel is facing North
    Post-condition: karel is at the upper right, facing South
    """
    turn_right()
    move()
    turn_right()


def up():
    """
    Pre-condition: karel is on the left side of the wall, facing East
    Post-condition: karel is facing North
    """
    turn_left()
    # Facing North
    while not right_is_clear():
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()








    
    


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
