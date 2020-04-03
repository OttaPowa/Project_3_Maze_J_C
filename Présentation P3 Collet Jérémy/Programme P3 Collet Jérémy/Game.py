# -*-coding:UTF-8-*

import pygame

from pygame.locals import *

from Maze import Maze
from Variables import *
from Object import Object

pygame.init()


class Game:

	absciss = 0
	ordonate = 0
	DISPLAY_ABS = absciss * SIZE_OF_SPRITE
	DISPLAY_ORD = ordonate * SIZE_OF_SPRITE
	WARNING_SENTENCE = "Vous ne pouvez pas aller par là!"
	LOOSE_SENTENSE = "Malheureusement vous avez échoué! Le jeu va se fermer automatiquement..."
	LOOSE_PICTURE = pygame.image.load(IMAGE_PATH + "LoosePicture.jpg").convert()
	WIN_SENTENSE = "Vous prennez la fuite! BRAVO! Le jeu va maintenant se fermer automatiquement..."
	WIN_PICTURE = pygame.image.load(IMAGE_PATH + "OPEN.jpg").convert()

	@classmethod
	def execute_commands(cls, 
		maze_map, 
		command,
		full_object_list, 
		WINDOW):
		"""
			Get the user's interactions and modify the maze in consequence.
		"""

		new_ordonate = cls.ordonate
		new_absciss = cls.absciss
		
		# moving commands:
		if command == "Down":
			new_ordonate += 1
		elif command == "Up":
			new_ordonate -= 1	
		elif command == "Right":
			new_absciss += 1		
		elif command == "Left":
			new_absciss -= 1
		
		# Allowed playing area:
		try: 
			maze_map[new_ordonate][new_absciss] != maze_map[cls.ordonate][cls.absciss]
		
		except IndexError:
			cls.write_message(WINDOW, cls.WARNING_SENTENCE)
			return True			

		if maze_map[new_ordonate][new_absciss] == ".":
			cls.write_message(WINDOW, cls.WARNING_SENTENCE)
			return True

		# conditions to win or loose:
		# win:
		if maze_map[new_ordonate][new_absciss] == "O" and Object.is_ready_for_victory == True:
			cls.write_message(WINDOW, cls.WIN_SENTENSE)
			WINDOW.fill((0,0,0))
			WINDOW.blit(cls.WIN_PICTURE, (0,0))
			WINDOW.blit(TEXT_FONT.render(cls.WIN_SENTENSE,True,(255, 255, 255)),(30,450))
			return False

		# loose:
		if maze_map[new_ordonate][new_absciss] == "O" and Object.is_ready_for_victory == False:
			cls.write_message(WINDOW, cls.LOOSE_SENTENSE)
			WINDOW.fill((0,0,0))
			WINDOW.blit(cls.LOOSE_PICTURE, (0,0))
			WINDOW.blit(TEXT_FONT.render(cls.LOOSE_SENTENSE,True,(255, 255, 255)),(30,450))
			return False

		# Management of the objects:
		if (maze_map[new_ordonate][new_absciss] != " "):
			
			for found_object in Object.full_object_list:
				if (found_object.symbol == maze_map[new_ordonate][new_absciss]):
					Object.put_in_backpack(found_object)
					cls.write_message(WINDOW, "Vous trouvez un(e) " + found_object.name)

			Object.check_if_ready_for_victory(Game, BACKPACK_RECT)
			
		# Deleting the old position for display:
		maze_map[cls.ordonate][cls.absciss] = " "
		WINDOW.blit(full_object_list[0].picture, (cls.DISPLAY_ORD,cls.DISPLAY_ABS))

		# Define the new player's location:
		cls.ordonate = new_ordonate
		cls.absciss = new_absciss

		# Define coordinates for display:
		cls.DISPLAY_ABS = new_ordonate * SIZE_OF_SPRITE
		cls.DISPLAY_ORD = new_absciss * SIZE_OF_SPRITE
		
		# Display the new player's location:
		maze_map[cls.ordonate][cls.absciss] = "X"
		WINDOW.blit(full_object_list[8].picture, (cls.DISPLAY_ORD,cls.DISPLAY_ABS))
		
		return True	

	@classmethod
	def write_message(cls, WINDOW, message):
		"""
			write a message in the message rect (ERROR_MESSAGE)
		"""

		TEXT_FONT = pygame.font.SysFont("Book Antiqua", 15)
		pygame.draw.rect(WINDOW, Color("Black"), ERROR_MESSAGE)
		WINDOW.blit(TEXT_FONT.render(message, True, (250,250,250)), ERROR_MESSAGE)