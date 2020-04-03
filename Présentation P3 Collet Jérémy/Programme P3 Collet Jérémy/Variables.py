# -*-coding:UTF-8-*

import pygame

from pygame.locals import *

pygame.init()

# PyGame variables:
WINDOW_TITLE = "La fuite de Mac Gyver"
NBR_OF_SPRITE = 15
SIZE_OF_SPRITE = 42
WINDOW_SIZE = (NBR_OF_SPRITE * SIZE_OF_SPRITE)
TEXT_FONT = pygame.font.SysFont("Calibri", 18)
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + SIZE_OF_SPRITE))

# list of tuples \
# (Name, Picture file name, X, Y, Symbol in maze_map, Is pickable object, Is needed for victory)
OBJECTS_LIST = [
    ("Sol", "Floor.png", 0, 0, " ", False, False),
    ("Murs", "Walls.png", 0, 0, ".", False, False),
    ("Garde", "Guardian.png", 0, 0, "O", False, False),
    ("Bouteille d'Ether", "Ether-Bottle.png", 0, 0, "E", True, True),
    ("Banane", "Banana-Peel.png", 0, 0, "B", True, False),
    ("Tube en plastique", "Fire-Pipe.png", 0, 0, "P", True, True),
    ("Aiguille", "Needle.png", 0, 0, "N", True, True),
    ("Feuille", "Leaf.png", 0, 0, "S", True, False),
    ("MacGyver", "MacGyver.png", 0, 0, "X", False, False),
    ("Seringue", "Seringe.png", 0, 0, "W", False, False),
    ("Backpack", "Backpack.png", 0, 0, "Z", False, False)]
IMAGE_PATH = "Images/"

# Display constants:
BACKPACK_COORDINATES = (5, WINDOW_SIZE)
BACKPACK_CONTENT = [
    (55, WINDOW_SIZE), 
    (115, WINDOW_SIZE), 
    (175, WINDOW_SIZE), 
    (235, WINDOW_SIZE), 
    (295, WINDOW_SIZE)]
MESSAGE_COORDINATES = (WINDOW_SIZE // 2, WINDOW_SIZE)
MESSAGE_SIZE = (WINDOW_SIZE // 2, SIZE_OF_SPRITE)
ERROR_MESSAGE = Rect(MESSAGE_COORDINATES[0], MESSAGE_COORDINATES[1], MESSAGE_SIZE[0], MESSAGE_SIZE[1])
BACKPACK_RECT = Rect(45, MESSAGE_COORDINATES[1], MESSAGE_SIZE[0]-45, MESSAGE_SIZE[1])
# greeting message:
GAME_RULES = "Vous incarnez le fameux MacGyver.\
            \nVous avez été capturé alors que vous exploriez la jungle. \
            \nVous êtes actuellement retenu enfermé dans un vieux batiment...\
            \nPour en sortir vous devez ramasser 3 objets distinct en vue de bricoler une seringue.\
            \nElle vous permettra d'endormir le garde et de vous enfuir. \
            \nVous présenter devant le garde sans la seringue vous menera a votre perte. \
            \nPour vous déplacer utilisez les touches directionnelles du clavier numérique. \
            \nVous pouvez quitter le jeu a tout moment en tappant ESC ou en cliquant sur la croix.\n \
            \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n   \
            \nAppuyez sur ENTRER pour commencer à jouer."