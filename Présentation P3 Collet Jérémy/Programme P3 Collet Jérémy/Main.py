# -*-coding:UTF-8-*

import pygame
import time
from pygame.locals import *

from Maze import Maze
from Game import Game
from Object import Object
from Variables import *

pygame.init()


def main():
    # Display the title of the game window:
    pygame.display.set_caption(WINDOW_TITLE)

    # Main variables:
    continue_prog = True
    maze_map = list()
    command = ""

    # Main loop:
    while continue_prog:
    
        BACK_IMAGE = pygame.image.load(IMAGE_PATH + "Forest.jpg").convert()
        WINDOW.blit(BACK_IMAGE, (8, 170))

        pygame.display.flip()

        continue_welcome = True
        continue_game = True
        # Welcome loop:
        while continue_welcome:

            pygame.time.Clock().tick(30)
            TEXT_RECT = Rect(15,15,WINDOW_SIZE,SIZE_OF_SPRITE*4)
            X,Y = TEXT_RECT.topleft
        
            # print the greeting sentence on screen
            for sentence in GAME_RULES.splitlines():
                X,Y = WINDOW.blit(TEXT_FONT.render(sentence,True,(255, 255, 255)),(X,Y)).bottomleft

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    continue_welcome = False
                    continue_game = False
                    continue_prog = False

                if event.type == KEYDOWN and event.key == K_RETURN:
                    continue_welcome = False

        # Loading of the maze from text file:
        Maze.load_from_textfile(maze_map)

        # Display objects inside the maze:
        Object.put_objects_in_maze(maze_map, OBJECTS_LIST)

        # Maze display:
        Maze.display_maze_with_pygame(maze_map, WINDOW, Object.full_object_list)

        # Game loop:
        while continue_game:

            pygame.time.Clock().tick(30)

            for event in pygame.event.get():

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    continue_game = False
                    continue_prog = False
                    pygame.quit()

                if event.type == KEYDOWN:
                
                    if event.key == K_KP6 or event.key == K_RIGHT:
                        command = "Right"
                    
                    if event.key == K_KP4 or event.key == K_LEFT:
                        command = "Left"

                    if event.key == K_KP2 or event.key == K_DOWN:
                        command = "Down"
                    
                    if event.key == K_KP8 or event.key == K_UP:
                        command = "Up"

                    continue_game = Game.execute_commands(maze_map, command, Object.full_object_list, WINDOW)
     
            pygame.display.update()

        continue_prog = False

    time.sleep(4)


if __name__ == '__main__':
    main()
else:
    pass

