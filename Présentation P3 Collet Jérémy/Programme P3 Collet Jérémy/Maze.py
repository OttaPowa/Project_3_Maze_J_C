# -*-coding:UTF-8-*

import pygame

from pygame.locals import *

from Object import Object
from Variables import *

pygame.init()


class Maze:		

	@staticmethod
	def load_from_textfile(maze_map):
		"""
			load maze from text file and display it item by item without the jump of line symbol.
		"""
		
		with open("labyrinthe.txt", "r") as my_file:
			for line in my_file:
				my_line = list()
				for character in line:
					if (character != "\n"):
						my_line.append(character)
				maze_map.append(my_line)
		return maze_map
	
	@staticmethod
	def draw_on_screen(maze_map):
		"""
			Draw the maze on screen from the two dimensional list maze_map.
		"""	

		for ordonate in range(len(maze_map)):
			for absciss in range(len(maze_map[ordonate])):
				print(maze_map[ordonate][absciss], end="")
			print()

	@staticmethod
	def display_maze_with_pygame(
		maze_map, 
		WINDOW, 
		full_object_list):
		"""
			Display the game area with pygame.
		"""
		
		for ord_number, line in enumerate(maze_map):
			for abs_number, cell in enumerate(line):
				x = abs_number * SIZE_OF_SPRITE
				y = ord_number * SIZE_OF_SPRITE
				
				maze_element = [element for element in full_object_list if element.symbol == cell][0]		
				WINDOW.blit(full_object_list[0].picture, (x,y))
				WINDOW.blit(maze_element.picture, (x,y))

		WINDOW.blit(full_object_list[10].picture, BACKPACK_COORDINATES)
		pygame.display.update()
