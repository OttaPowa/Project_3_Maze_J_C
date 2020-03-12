#-*-coding:UTF-8-*

import pygame
from Object import Object
from Variables import *
from pygame.locals import *
# pygame.init()

class Maze:
		

	@staticmethod
	def LoadFromTextFile(MazeMap):
		"""
			load the maze from a text file and display it item by item without the jump of line symbol.
		"""
		
		with open("labyrinthe.txt", "r") as MyFile:

			for Line in MyFile:
				MyLine = list()

				for Character in Line:
					if (Character != "\n"):
						MyLine.append(Character)

				MazeMap.append(MyLine)

		return MazeMap
	
	@staticmethod
	def DrawOnScreen(MazeMap):
		"""
			Draw the maze on screen from the two dimentional list MazeMap.
		"""	

		for Ordonate in range(len(MazeMap)):
			for Absciss in range(len(MazeMap[Ordonate])):
				print(MazeMap[Ordonate][Absciss], end="")
			print()


	@staticmethod
	def DisplayMazeWithPyGame(
		MazeMap, 
		Window, 
		FullObjectList):
		"""
			Display the game area with pygame.
		"""
		
		for OrdNumber, line in enumerate(MazeMap):

			for AbsNumber, Cell in enumerate(line):

				x = AbsNumber * SizeOfSprite
				y = OrdNumber * SizeOfSprite

				MazeElement = [Element for Element in FullObjectList if Element.Symbol == Cell][0]
		
				Window.blit(FullObjectList[0].Picture, (x,y))
				Window.blit(MazeElement.Picture, (x,y))
        
		Window.blit(FullObjectList[10].Picture, BackpackCoordinates)
		pygame.display.update()
