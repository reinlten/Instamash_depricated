import os
import random
import json
from re import split
import data_loader
import random


# dieser Wert gibt an, um wie viel man maximal an elo dazu gewinnen kann.
# kann man variabel je nach bewertungen anpassen
k_val = 40  # ein Wert von 15 ist im schweizer Tischtennis einheitlich geltend. lol
k_elo_default_value = 1400


def get_name(image_source):
    s1 = image_source.split("/")
    s2 = s1[2].split(".")
    return s2[0]


# ist schlecht gecodet, sollte eigentlich (a-b) in der Klammer sein
def ew(a, b):
    return 1 / (1 + 10 ** ((b - a) / 400))


def rateGirlAndReturn(linkToGirl1, linkToGirl2, decision):
    stars_dict = data_loader.load_stars()
    girl1_name = get_name(linkToGirl1)
    girl2_name = get_name(linkToGirl2)
    start_elos = data_loader.load_elos([girl1_name, girl2_name])

    ew_right = ew(start_elos[girl2_name], start_elos[girl1_name])
    ew_left = ew(start_elos[girl1_name], start_elos[girl2_name])

    new_elos = {}

    if decision == "left":
        new_elos[girl1_name] = start_elos[girl1_name] + k_val * (1 - ew_left)
        new_elos[girl2_name] = start_elos[girl2_name] + k_val * (0 - ew_right)
    else:
        new_elos[girl1_name] = start_elos[girl1_name] + k_val * (0 - ew_left)
        new_elos[girl2_name] = start_elos[girl2_name] + k_val * (1 - ew_right)

    data_loader.update_stars_elo_json(new_elos)

    newGirlLink = linkToGirl1

    while newGirlLink == linkToGirl1 or newGirlLink == linkToGirl2:

        keys = list(stars_dict)
        name = random.choice(keys)
        newGirlLink = stars_dict[name]["image_source"]

    return newGirlLink
