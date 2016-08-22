# this exists to make the keyboard layout system less cluttered
from pygame import *

def matchKey(key,pressedkeys):
    if key == "'":
        return pressedkeys[K_QUOTE]
    if key == ",":
        return pressedkeys[K_COMMA]
    if key == ".":
        return pressedkeys[K_PERIOD]
    if key == "p":
        return pressedkeys[K_p]
    if key == "y":
        return pressedkeys[K_y]
    if key == "f":
        return pressedkeys[K_f]
    if key == "g":
        return pressedkeys[K_g]
    if key == "c":
        return pressedkeys[K_c]
    if key == "r":
        return pressedkeys[K_r]
    if key == "l":
        return pressedkeys[K_l]
    if key == "/":
        return pressedkeys[K_SLASH]
    if key == "=":
        return pressedkeys[K_EQUALS]

    if key == "a":
        return pressedkeys[K_a]
    if key == "o":
        return pressedkeys[K_o]
    if key == "e":
        return pressedkeys[K_e]
    if key == "u":
        return pressedkeys[K_u]
    if key == "i":
        return pressedkeys[K_i]
    if key == "d":
        return pressedkeys[K_d]
    if key == "h":
        return pressedkeys[K_h]
    if key == "t":
        return pressedkeys[K_t]
    if key == "n":
        return pressedkeys[K_n]
    if key == "s":
        return pressedkeys[K_s]

    if key == ";":
        return pressedkeys[K_COLON]
    if key == "q":
        return pressedkeys[K_q]
    if key == "j":
        return pressedkeys[K_j]
    if key == "k":
        return pressedkeys[K_k]
    if key == "x":
        return pressedkeys[K_x]
    if key == "b":
        return pressedkeys[K_b]
    if key == "m":
        return pressedkeys[K_m]
    if key == "w":
        return pressedkeys[K_w]
    if key == "v":
        return pressedkeys[K_v]
    if key == "z":
        return pressedkeys[K_z]

    if key == "left":
        return pressedkeys[K_LEFT]
    if key == "right":
        return pressedkeys[K_RIGHT]
    if key == "up":
        return pressedkeys[K_UP]
    if key == "down":
        return pressedkeys[K_DOWN]