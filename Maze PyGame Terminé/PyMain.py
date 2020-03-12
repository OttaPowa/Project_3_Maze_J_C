#-*-coding:UTF-8-*

import time
import pygame
from Maze import Maze
from Game import Game
from Object import Object
from Variables import *
from pygame.locals import *
pygame.init()

#Diplay the title of the game window:
pygame.display.set_caption(WindowTitle)

#Main variables:
Continue = True
UserName = ""
MazeMap = list()
Command = ""

#Main loop:
while Continue:
    
    BackImage = pygame.image.load(ImagePath + "Forest.jpg").convert()
    Window.blit(BackImage, (8, 170))

    pygame.display.flip()

    ContinueWelcome = True
    ContinueGame = True
    #Welcome loop:
    while ContinueWelcome:

        pygame.time.Clock().tick(30)
        TextRect = Rect(15,15,WindowSize,SizeOfSprite*4)
        X,Y = TextRect.topleft
        
        #print the greeting sentence on screen
        for Sentense in GameRules.splitlines():
            X,Y = Window.blit(TextFont.render(Sentense,True,(255, 255, 255)),(X,Y)).bottomleft

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                ContinueWelcome = False
                ContinueGame = False
                Continue = False

            if event.type == KEYDOWN and event.key == K_RETURN:
                ContinueWelcome = False

                
    #Loading of the maze from text file:
    Maze.LoadFromTextFile(MazeMap)

    #Display objects inside the maze:
    Object.PutObjectsInMaze(MazeMap, ObjectsList)

    #Maze display:
    Maze.DisplayMazeWithPyGame(MazeMap, Window, Object.FullObjectList)

    #Game loop:
    while ContinueGame:

        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                ContinueGame = False
                Continue = False
                pygame.quit()

            if event.type == KEYDOWN:
                
                if event.key == K_KP6 or event.key == K_RIGHT:
                    Command = "Right"
                    
                if event.key == K_KP4 or event.key == K_LEFT:
                    Command = "Left"

                if event.key == K_KP2 or event.key == K_DOWN:
                    Command = "Down"
                    
                if event.key == K_KP8 or event.key == K_UP:
                    Command = "Up"

                ContinueGame = Game.ExecuteCommands(MazeMap, Command, Object.FullObjectList, Window)
     
        pygame.display.update()

    Continue = False

time.sleep(4)
