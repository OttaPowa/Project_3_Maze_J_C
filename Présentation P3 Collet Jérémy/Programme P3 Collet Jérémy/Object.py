# -*-coding:UTF-8-*

import random
import pygame

from pygame.locals import *

from Variables import *

pygame.init()


class Object:

    # class properties
    full_object_list = []
    backpack = []   # list of objects in backpack
    NUMBER_OF_OBJECT_FOR_VICTORY = 3  # number of useful objects needed to victory
    is_ready_for_victory = False # if objects in backpack are sufficient for victory
    
    i = 0  # variable to modify the object display coordinates

    def __init__(self,
        name,
        picture,
        position_X=int,
        position_Y=int,
        symbol="",
        is_pickable=bool(),
        usefull_for_victory=False,
        ):
        """
            Constructor

            :param arg1: name of the object
            :type arg1: string
            :param arg2: picture of the object
            :type arg2: string
            :param arg3: Position X of the object
            :type arg3: int
            :param arg4: Position Y of the object
            :type arg4: int
            :param arg5: Display symbol for the object
            :type arg5: string
            :param arg6: If the object is pickable
            :type arg6: bool
            :param arg7: If the object is useful for victory
            :type arg7: bool
        """

        self.name = name
        self.picture = picture
        self.position_X = position_X
        self.position_Y = position_Y
        self.symbol = symbol
        self.is_pickable = is_pickable
        self.usefull_for_victory = usefull_for_victory  
        self.full_object_list.append(self)
        
    @staticmethod
    def put_objects_in_maze(maze_map, full_object_list):
        """ 
            Put Display Symbols of the objects randomly inside the maze
        """	
        
        for current_object in OBJECTS_LIST:

            # create object instance
            my_object = Object(
                current_object[0],
                current_object[1],
                current_object[2],
                current_object[3],
                current_object[4],
                current_object[5],
                current_object[6])

            object_abs = random.randint(0,len(maze_map)-1)
            object_ord = random.randint(0,len(maze_map[0])-1)

            while maze_map[object_abs][object_ord] != " ":
                object_abs = random.randint(0,len(maze_map)-1)
                object_ord = random.randint(0,len(maze_map[0])-1)

            # Define the coordinates
            my_object.position_Y = object_abs
            my_object.positionX = object_ord

            # Scale the pictures for display
            my_object.picture = pygame.image.load(IMAGE_PATH + my_object.picture).convert_alpha()
            my_object.picture = pygame.transform.scale(my_object.picture, (SIZE_OF_SPRITE, SIZE_OF_SPRITE))
                              
            # put in maze
            if my_object.is_pickable != False:
                maze_map[object_abs][object_ord] = my_object.symbol
            
        return maze_map

    def put_in_backpack(self):
        """
            Put object in backpack
        """ 

        object_name = self.name
        object_picture = self.picture

        # display the object name in a sentence inside the message rect
        WINDOW.blit(TEXT_FONT.render(object_name, True, (255,255,255)), ERROR_MESSAGE)
        Object.backpack.append(self)

        # display the object picture at defined coordinates inside the backpack rect
        WINDOW.blit(object_picture, (BACKPACK_CONTENT[Object.i])) 
        Object.i += 1
    
    @classmethod
    def check_if_ready_for_victory(cls, Game, BACKPACK_RECT):
        """
            Check if objects in backpack can lead to victory
        """
        
        number_of_usefull_objects = 0
        GET_SERINGE = "Vous fabriquez une seringue de fortune!"

        for Obj in cls.backpack:
            if Obj.usefull_for_victory == True:
                number_of_usefull_objects += 1
                
        if number_of_usefull_objects == cls.NUMBER_OF_OBJECT_FOR_VICTORY:
            cls.is_ready_for_victory = True

            # print a sentence when you obtain the seringe
            Game.write_message(WINDOW, GET_SERINGE)

            # hide the object picture with a black rect and display the seringe picture
            pygame.draw.rect(WINDOW, Color("Black"), BACKPACK_RECT)
            WINDOW.blit(Object.full_object_list[9].picture, (BACKPACK_CONTENT[0]))