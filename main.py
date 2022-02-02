import sys
import random
import pygame

from pip._vendor.progress.colors import black


def getImage(n):
    if n == 0:
        return pygame.image.load("emma.png").convert()
    if n == 1:
        return pygame.image.load("emma_w.png").convert()
    if n == 2:
        return pygame.image.load("gal.png").convert()
    if n == 3:
        return pygame.image.load("jen.png").convert()
    if n == 4:
        return pygame.image.load("mila.png").convert()
    if n == 5:
        return pygame.image.load("nat.png").convert()
    if n == 6:
        return pygame.image.load("nat2.png").convert()
    if n == 7:
        return pygame.image.load("scar.png").convert()
    if n == 8:
        return pygame.image.load("mila2.png").convert()

# ist schlecht gecodet, sollte eigentlich (a-b) in der Klammer sein
def ew(a, b):
    return 1 / (1 + 10 ** ((b - a) / 400))


pygame.init()

screen = pygame.display.set_mode((600, 300))

gils = ["emma stone", "emma watson", "gal gadot", "jennifer lawrence",
        "mila kunis", "natalie portman", "natalie portman in besser", "scarlett johansson",
        "mila kunis in heiß"]

data = [1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400]

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

while True:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.KEYDOWN:

            ew_right = ew(data[pic2], data[pic1])
            ew_left = ew(data[pic1], data[pic2])

            if event.key == pygame.K_LEFT:
                data[pic1] = data[pic1] + k_val * (1 - ew_left)
                data[pic2] = data[pic2] + k_val * (0 - ew_right)
                while check == False:
                    pic2 = random.randrange(0, len(data))
                    if pic2 != pic1 and pic2 != pic2_save:
                        check = True
                pic2_save = pic2
                check = False

            if event.key == pygame.K_RIGHT:
                data[pic2] = data[pic2] + k_val * (1 - ew_right)
                data[pic1] = data[pic1] + k_val * (0 - ew_left)
                while check == False:
                    pic1 = random.randrange(0, len(data))
                    if pic1 != pic2 and pic1 != pic1_save:
                        check = True

                pic1_save = pic1
                check = False

            if event.key == pygame.K_DOWN:
                for i in range(len(data)):
                    print(gils[i] + ": " + str(data[i]))

                print()
                print()

            print("Erwartungswert für rechts:" + str(ew(data[pic2], data[pic1])))
            print("Erwartungswert für links:" + str(ew(data[pic1], data[pic2])))
            print()
            print()

    screen.fill((0, 0, 0))
    screen.blit(getImage(pic1), (0, 0))
    screen.blit(getImage(pic2), (300, 0))
    pygame.display.flip()
