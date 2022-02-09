import os
import random
# import pygame
# import json
from re import split


def getImage(n):
    return (girl_link[n])


# ist schlecht gecodet, sollte eigentlich (a-b) in der Klammer sein
def ew(a, b):
    return 1 / (1 + 10 ** ((b - a) / 400))


# pygame.init()

# screen = pygame.display.set_mode((600, 300))
f = open("stars.txt", "r")
gils = f.readlines()
f.close()

girl_link = os.listdir('website\static\img')
data = []

for i in range(len(girl_link)):
    data.append(1400)
    girl_link[i] = "static/img/" + girl_link[i]
    print(girl_link[i])


def girlToNumber(girl):
    for i in range(len(girl_link)):
        if girl == girl_link[i]:
            return i


def getName(girl):
    s1 = girl.split("/")
    s2 = s1[2].split(".")
    return s2[0]


check = False

# dieser Wert gibt an, um wie viel man maximal an elo dazu gewinnen kann.
# kann man variabel je nach bewertungen anpassen
k_val = 40  # ein Wert von 15 ist im schweizer Tischtennis einheitlich geltend. lol

pic1 = random.randrange(0, len(data))

while check == False:
    pic2 = random.randrange(0, len(data))
    if pic2 != pic1:
        check = True

check = False

pic1_save = pic1
pic2_save = pic2


# while True:
# events = pygame.event.get()

def rateGirlAndReturn(linkToGirl1, linkToGirl2, decision):
    elo1 = 0
    elo2 = 0

    for i in range(len(girl_link)):
        if girl_link[i] == linkToGirl1:
            elo1 = i

        if girl_link[i] == linkToGirl2:
            elo2 = i

    ew_right = ew(data[elo2], data[elo1])
    ew_left = ew(data[elo1], data[elo2])

    if decision == "left":
        data[elo1] = data[elo1] + k_val * (1 - ew_left)
        data[elo2] = data[elo2] + k_val * (0 - ew_right)

    if decision == "right":
        data[elo2] = data[elo2] + k_val * (1 - ew_right)
        data[elo1] = data[elo1] + k_val * (0 - ew_left)

    newGirlLink = linkToGirl1

    while newGirlLink == linkToGirl1 or newGirlLink == linkToGirl2:
        newGirlLink = girl_link[random.randrange(0, len(girl_link))]

    for i in range(len(girl_link)):
        if girl_link[i] == linkToGirl1:
            elo1 = i

        if girl_link[i] == linkToGirl2:
            elo2 = i

    for i in range(len(data)):
        print(gils[i] + ": " + str(data[i]))

    print()
    print()

    # print("Erwartungswert für rechts:" + str(ew(data[elo2], data[elo1])))
    # print("Erwartungswert für links:" + str(ew(data[elo1], data[elo2])))

    return newGirlLink


def rateGirl(pic1, pic2, decision):
    pic1_save = pic1
    pic2_save = pic2

    ew_right = ew(data[pic2], data[pic1])
    ew_left = ew(data[pic1], data[pic2])

    if decision == "1":
        data[pic1] = data[pic1] + k_val * (1 - ew_left)
        data[pic2] = data[pic2] + k_val * (0 - ew_right)
        while check == False:
            pic2 = random.randrange(0, len(data))
            if pic2 != pic1 and pic2 != pic2_save:
                check = True
        pic2_save = pic2
        check = False

    if decision == "2":
        data[pic2] = data[pic2] + k_val * (1 - ew_right)
        data[pic1] = data[pic1] + k_val * (0 - ew_left)
        while check == False:
            pic1 = random.randrange(0, len(data))
            if pic1 != pic2 and pic1 != pic1_save:
                check = True

        pic1_save = pic1
        check = False

    # if event.key == pygame.K_DOWN:
    #    for i in range(len(data)):
    #        print(gils[i] + ": " + str(data[i]))

    #    print()
    #    print()

    print("Erwartungswert für rechts:" + str(ew(data[pic2], data[pic1])))
    print("Erwartungswert für links:" + str(ew(data[pic1], data[pic2])))
    print()
    print()

# screen.fill((0, 0, 0))
# screen.blit(getImage(pic1), (0, 0))
# screen.blit(getImage(pic2), (300, 0))
# pygame.display.flip()
