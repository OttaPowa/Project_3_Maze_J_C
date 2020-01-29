#-*-coding:UTF-8-*

import random

class Object:

    # class properties
    FullObjectList = []
    Backpack = []   # list of objects in backpack
    NumberOfObjectsForVictory = 3  # number of usefull objects needed to achieve victory
    IsReadyForVictory = False # if objects in backpack are sufficient for victory

    def __init__(self,
        Name, 
        PositionX,
        PositionY,
        DisplaySymbol="", 
        UsefullForVictory=False):
        """
            Constructor

            :param arg1: Name of the object
            :type arg1: string
            :param arg2: Display symbol for the object
            :type arg2: string
            :param arg3: If the object is usefull for victory
            :type arg3: bool
        """

        self.Name = Name
        self.PositionX = PositionX
        self.PositionY = PositionY
        if DisplaySymbol != "":
            self.DisplaySymbol = DisplaySymbol
        else:
            self.DisplaySymbol = self.Name[:1]
        self.UsefullForVictory = UsefullForVictory
        self.FullObjectList.append(self)


    @staticmethod
    def PutObjectsInMaze(MazeMap, ObjectsList):
        """ 
            Put Display Symbols of the objects randomly inside the maze
        """	
	
        for CurrentObject in ObjectsList:
            ObjectOrd = random.randint(0,len(MazeMap)-1)
            ObjectAbs = random.randint(0,len(MazeMap[0])-1)

            while MazeMap[ObjectOrd][ObjectAbs] != " ":
                ObjectOrd = random.randint(0,len(MazeMap)-1)
                ObjectAbs = random.randint(0,len(MazeMap[0])-1)

            # create object instance
            MyObject = Object(
                CurrentObject[0],
                ObjectAbs,
                ObjectOrd,
                CurrentObject[1],
                CurrentObject[2])
                
            # put in maze
            MazeMap[ObjectOrd][ObjectAbs] = MyObject.DisplaySymbol
            
        return MazeMap

    
    def PutInBackpack(self):
        """
            Put object in backpack
        """
        print("\nUn(e) {}".format(self.Name))
        Object.Backpack.append(self)
    
    
    @classmethod
    def CheckIfReadyForVictory(cls):
        """
            Check if objects in backpack can lead to victory
        """
        NumberOfUsefullObjects = 0
        
        for Obj in cls.Backpack:
            if Obj.UsefullForVictory == True:
                NumberOfUsefullObjects += 1
                

        if NumberOfUsefullObjects == cls.NumberOfObjectsForVictory:
            cls.IsReadyForVictory = True
            print("\nVous fabriquez une seringue de fortune pour endormir le garde!!\n")
          