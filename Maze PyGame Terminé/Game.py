#-*-coding:UTF-8-*

import pygame
from Maze import Maze
from Variables import *
from Object import Object
from pygame.locals import *

class Game:

	Absciss = 0
	Ordonate = 0
	DisplayAbs = Absciss * SizeOfSprite
	DisplayOrd = Ordonate * SizeOfSprite
	WarningSentense = "Vous ne pouvez pas aller par là!"
	LooseSentense = "Malheureusement vous avez échoué! Le jeu va se fermer automatiquement..."
	LoosePicture = pygame.image.load(ImagePath + "LoosePicture.jpg").convert()
	WinSentense = "Vous prennez la fuite! BRAVO! Le jeu va maintenant se fermer automatiquement..."
	WinPicture = pygame.image.load(ImagePath + "OPEN.jpg").convert()

	@classmethod
	def ExecuteCommands(cls, 
		MazeMap, 
		Command,
		FullObjectList, 
		Window):
		"""
			Get the user's interactions and modify the maze in consequence.
		"""

		NewOrdonate = cls.Ordonate
		NewAbsciss = cls.Absciss
		
		#mooving commands:
		if Command == "Down":
			NewOrdonate += 1
		elif Command == "Up":
			NewOrdonate -= 1	
		elif Command == "Right":
			NewAbsciss += 1		
		elif Command == "Left":
			NewAbsciss -= 1
		
		#Allowed playing area:
		try: 
			MazeMap[NewOrdonate][NewAbsciss] != MazeMap[cls.Ordonate][cls.Absciss]
		
		except IndexError:
			cls.WriteMessage(Window, cls.WarningSentense)
			return True			

		if MazeMap[NewOrdonate][NewAbsciss] == ".":
			cls.WriteMessage(Window, cls.WarningSentense)
			return True


		#conditions to win or loose:
		#win:
		if MazeMap[NewOrdonate][NewAbsciss] == "O" and Object.IsReadyForVictory == True:
			cls.WriteMessage(Window, cls.WinSentense)
			Window.fill((0,0,0))
			Window.blit(cls.WinPicture, (0,0))
			Window.blit(TextFont.render(cls.WinSentense,True,(255, 255, 255)),(30,450))
			return False

		#loose:
		if MazeMap[NewOrdonate][NewAbsciss] == "O" and Object.IsReadyForVictory == False:
			cls.WriteMessage(Window, cls.LooseSentense)
			Window.fill((0,0,0))
			Window.blit(cls.LoosePicture, (0,0))
			Window.blit(TextFont.render(cls.LooseSentense,True,(255, 255, 255)),(30,450))
			return False


		#Management of the objects:
		if (MazeMap[NewOrdonate][NewAbsciss] != " "):
			
			for FoundObject in Object.FullObjectList:
				if (FoundObject.Symbol == MazeMap[NewOrdonate][NewAbsciss]):
					Object.PutInBackpack(FoundObject)
					cls.WriteMessage(Window, "Vous trouvez un(e) " + FoundObject.Name)

			Object.CheckIfReadyForVictory(Game, BackpackRect)
			
		#Delating the old position for display:
		MazeMap[cls.Ordonate][cls.Absciss] = " "
		Window.blit(FullObjectList[0].Picture, (cls.DisplayOrd,cls.DisplayAbs))
		

		#Define the new player's location:
		cls.Absciss = NewAbsciss
		cls.Ordonate = NewOrdonate

		#Define coordonates for display:
		cls.DisplayOrd = NewAbsciss * SizeOfSprite
		cls.DisplayAbs = NewOrdonate * SizeOfSprite
		
		#Display the new player's location:
		MazeMap[cls.Ordonate][cls.Absciss] = "X"
		Window.blit(FullObjectList[8].Picture, (cls.DisplayOrd,cls.DisplayAbs))
		
		return True	

	@classmethod
	def WriteMessage(cls, Window, Message):
		"""
			write a message in the message rect (ErrorMessage)
		"""

		TextFont = pygame.font.SysFont("Book Antiqua", 15)
		pygame.draw.rect(Window, Color("Black"), ErrorMessage)
		Window.blit(TextFont.render(Message, True, (250,250,250)), ErrorMessage) 
			