#-*-coding:UTF-8-*

import random
from Variables import *
import pygame
from pygame.locals import *

class Object:

    # class properties
    FullObjectList = []
    Backpack = []   # list of objects in backpack
    NumberOfObjectsForVictory = 3  # number of usefull objects needed to achieve victory
    IsReadyForVictory = False # if objects in backpack are sufficient for victory
    
    i = 0 # variable for modify the object display coodonates

    def __init__(self,
        Name,
        Picture,
        PositionX=int,
        PositionY=int,
        Symbol="",
        IsPickable=bool(),
        UsefullForVictory=False,
        ):
        """
            Constructor

            :param arg1: Name of the object
            :type arg1: string
            :param arg2: Picture of the object
            :type arg2: string
            :param arg3: Position X of the object
            :type arg3: int
            :param arg4: Position Y of the object
            :type arg4: int
            :param arg5: Display symbol for the object
            :type arg5: string
            :param arg6: If the object is pickable
            :type arg6: bool
            :param arg7: If the object is usefull for victory
            :type arg7: bool
        """

        self.Name = Name
        self.Picture = Picture
        self.PositionX = PositionX
        self.PositionY = PositionY
        self.Symbol = Symbol
        self.IsPickable = IsPickable
        self.UsefullForVictory = UsefullForVictory  
        self.FullObjectList.append(self)
        

    @staticmethod
    def PutObjectsInMaze(MazeMap, FullObjectList):
        """ 
            Put Display Symbols of the objects randomly inside the maze
        """	
        
        for CurrentObject in ObjectsList:

            # create object instance
            MyObject = Object(
                CurrentObject[0],
                CurrentObject[1],
                CurrentObject[2],
                CurrentObject[3],
                CurrentObject[4],
                CurrentObject[5],
                CurrentObject[6])

            ObjectAbs = random.randint(0,len(MazeMap)-1)
            ObjectOrd = random.randint(0,len(MazeMap[0])-1)

            while MazeMap[ObjectAbs][ObjectOrd] != " ":
                ObjectAbs = random.randint(0,len(MazeMap)-1)
                ObjectOrd = random.randint(0,len(MazeMap[0])-1)

            #Define the coordinates
            MyObject.PositionY = ObjectAbs
            MyObject.PostionX = ObjectOrd

            #Scalle the pictures for display
            MyObject.Picture = pygame.image.load(ImagePath + MyObject.Picture).convert_alpha()
            MyObject.Picture = pygame.transform.scale(MyObject.Picture, (SizeOfSprite, SizeOfSprite))
                              
            # put in maze
            if MyObject.IsPickable != False:               
                MazeMap[ObjectAbs][ObjectOrd] = MyObject.Symbol
            
        return MazeMap


    def PutInBackpack(self):
        """
            Put object in backpack
        """ 

        ObjectName = self.Name
        ObjectPicture = self.Picture

        #display the object name in a sentence inside the message rect
        Window.blit(TextFont.render(ObjectName, True, (255,255,255)), ErrorMessage)
        Object.Backpack.append(self)

        #display the object picture at defined coordonates inside the backpack rect
        Window.blit(ObjectPicture, (BackpackContent[Object.i])) 
        Object.i += 1

    
    @classmethod
    def CheckIfReadyForVictory(cls, Game, BackpackRect):
        """
            Check if objects in backpack can lead to victory
        """
        
        NumberOfUsefullObjects = 0
        GetSeringe = "Vous fabriquez une seringue de fortune!"

        for Obj in cls.Backpack:
            if Obj.UsefullForVictory == True:
                NumberOfUsefullObjects += 1
                
        if NumberOfUsefullObjects == cls.NumberOfObjectsForVictory:
            cls.IsReadyForVictory = True

            #print a sentence when you obtain the seringue
            Game.WriteMessage(Window, GetSeringe)

            #hide the object picture with a black rect and display the seringue picture
            pygame.draw.rect(Window, Color("Black"), BackpackRect)
            Window.blit(Object.FullObjectList[9].Picture, (BackpackContent[0]))