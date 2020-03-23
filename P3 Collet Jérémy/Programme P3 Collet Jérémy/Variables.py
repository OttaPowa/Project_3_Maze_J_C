#-*-coding:UTF-8-*

import pygame
from pygame.locals import *
pygame.init()

#PyGame variables:
WindowTitle = "La fuite de Mac Gyver"
NbrOfSprite = 15
SizeOfSprite = 42
WindowSize = (NbrOfSprite * SizeOfSprite)
TextFont = pygame.font.SysFont("Calibri", 18)
Window = pygame.display.set_mode((WindowSize, WindowSize + SizeOfSprite))

# list of tuples (Name, Picture file name, X, Y, Symbol in Mazemap, Is pickable object, Is needed for victory)
ObjectsList = [
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
ImagePath = "Images/"

# Display constantes:
BackpackCoordinates = (5, WindowSize)
BackpackContent = [
    (55, WindowSize), 
    (115, WindowSize), 
    (175, WindowSize), 
    (235, WindowSize), 
    (295, WindowSize)]
MessageCoordinates = (WindowSize // 2, WindowSize)
MessageSize = (WindowSize // 2, SizeOfSprite)
ErrorMessage = Rect(MessageCoordinates[0], MessageCoordinates[1], MessageSize[0], MessageSize[1])
BackpackRect = Rect(45, MessageCoordinates[1], MessageSize[0]-45, MessageSize[1])
# greeting message:
GameRules = "Vous incarnez le fameux MacGyver.\
            \nVous avez été capturé alors que vous exploriez la jungle. \
            \nVous êtes actuellement retenu enfermé dans un vieux batiment...\
            \nPour en sortir vous devez ramasser trois objets distinct en vue de bricoler une seringue.\
            \nElle vous permettra d'endormir le garde et de vous enfuir. \
            \nVous présenter devant le garde sans la seringue vous menera a votre perte. \
            \nPour vous déplacer utilisez les touches directionnelles du clavier numérique. \
            \nVous pouvez quitter le jeu a tout moment en tappant ESC ou en cliquant sur la croix.\n \
            \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n   \
            \nAppuyez sur ENTRER pour commencer à jouer."