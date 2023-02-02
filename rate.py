import os
import random
import json
from re import split
import data_loader
import random
from sqlalchemy import func
from website import models, db

# dieser Wert gibt an, um wie viel man maximal an elo dazu gewinnen kann.
# kann man variabel je nach bewertungen anpassen
k_val = 40  # ein Wert von 15 ist im schweizer Tischtennis einheitlich geltend. lol
k_elo_default_value = 1500


def get_name(image_source):
    s1 = image_source.split("/")
    s2 = s1[2].split(".")
    return s2[0]


def return_other_girl(girl):
    newGirlLink = girl
    while newGirlLink == girl:
        keys = models.Girldata.query.order_by(func.random()).first()
        newGirlLink = keys

    return newGirlLink


# ist schlecht gecodet, sollte eigentlich (a-b) in der Klammer sein
def ew(a, b):
    return 1 / (1 + 10 ** ((b - a) / 400))


def rateGirlAndReturn(linkToGirl1, linkToGirl2, decision):
    girl1 = models.Girldata.query.filter_by(image_id=linkToGirl1).first()
    girl2 = models.Girldata.query.filter_by(image_id=linkToGirl2).first()

    girl1_name = girl1.name
    girl2_name = girl2.name
    start_elos = [girl1.elo, girl2.elo]

    ew_right = ew(start_elos[1], start_elos[0])
    ew_left = ew(start_elos[0], start_elos[1])

    new_elos = {}

    if decision == "left":
        new_elos[girl1_name] = start_elos[0] + k_val * (1 - ew_left)
        new_elos[girl2_name] = start_elos[1] + k_val * (0 - ew_right)
    else:
        new_elos[girl1_name] = start_elos[0] + k_val * (0 - ew_left)
        new_elos[girl2_name] = start_elos[1] + k_val * (1 - ew_right)

    girl1.elo = new_elos[girl1_name]
    girl2.elo = new_elos[girl2_name]

    db.session.commit()

    newGirlLink = linkToGirl1

    while newGirlLink == linkToGirl1 or newGirlLink == linkToGirl2:
        keys = models.Girldata.query.order_by(func.random()).first()
        newGirlLink = keys.image_id

    return newGirlLink
