#-*-coding:UTF-8-*

import os
from User import User
from Maze import Maze
from Game import Game
from Object import Object

#Start variables:

ContinueGame = True
UserName = ""
MazeMap = list()
ObjectsList = [
	("Bouteille d'Ether", "E", True),
	("Tube en plastique", "T", True),
	("Aiguille", "A", True),
	("Banane", "B", False),
	("Table", "b", False)]

#APPLICATION:

print("Bienvenue! \nVous allez devoir atteindre la sortie du labyrinthe! Votre personnage est symbolisé par (X) et la sortie par (O).\nVous devez ramasser les trois objets pour endormir le garde et vous enfuir.\nVous pouvez quitter le jeu a tout moment en tappant q.")

while UserName == "":
	#loop of name demand, if nothing is written it asks name again
	UserName = User.GetName()

User.Greetings(UserName)

print("\nPour vous déplacer utilisez les touches: \n(u) pour aller en haut, (d) pour aller en bas, (l) pour aller à gauche et (r) pour aller à droite.\n")

#Loading of the maze from text file:
Maze.LoadFromTextFile(MazeMap)
#Display objects inside the maze:
Object.PutObjectsInMaze(MazeMap, ObjectsList)
#Maze display:
Maze.DrawOnScreen(MazeMap)

while ContinueGame == True:
	#Game loop, while the user don't get out, don't win or loose it asks him/her to enter commands and it redraw the maze on screen.
	ContinueGame = Game.GetAndExecuteCommands(MazeMap, UserName)
	Maze.DrawOnScreen(MazeMap)

os.system("pause")
