#-*-coding:UTF-8-*

class Maze:

	@staticmethod
	def LoadFromTextFile(MazeMap):
		"""
			loading the maze from a text file and display it items by items without the jump of line symbol.
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
