#-*-coding:UTF-8-*

from Object import Object

class Game:

	Absciss = 0
	Ordonate = 0

	@classmethod
	def GetAndExecuteCommands(cls, MazeMap, UserName):
		"""
			Get the user's interactions and modify the maze in consequence.
		"""

		UserInput = input("\nDéplacez le personnage: ")
		NewOrdonate = cls.Ordonate
		NewAbsciss = cls.Absciss
	
		#mooving commands:
		if UserInput == "d":
			NewOrdonate += 1

		elif UserInput == "u":
			NewOrdonate -= 1
		
		elif UserInput == "r":
			NewAbsciss += 1
			
		elif UserInput == "l":
			NewAbsciss -= 1
	
		elif UserInput =="q":
			return False

		else:
			print("\ntouche non fonctionnelle. Les directions sont : r,l,u et d")
			return True
		
		#Allowed playing area:
		try: 
			MazeMap[NewOrdonate][NewAbsciss] != MazeMap[cls.Ordonate][cls.Absciss]
		
		except IndexError:
			print("Vous ne pouvez pas sortir par là!")
			return True

		#Alternative method of dealing with getting out of the playing area:
		#if (NewOrdonate <0 or NewOrdonate > len(MazeMap)) or (NewAbsciss <0 or NewAbsciss > len(MazeMap[0])):
			#print("Vous ne pouvez pas sortir par là!")
			#return

		if MazeMap[NewOrdonate][NewAbsciss] == ".":
			print("\nVous foncez dans un mur! Essayez une autre direction!")
			return True

		#conditions to win or loose:
		if MazeMap[NewOrdonate][NewAbsciss] == "O" and Object.IsReadyForVictory == True: #len(cls.ObjectsTaken) == len(ObjectsList):
			print("\nVous vous faufillez lachement dans le dos du garde et enfoncez la seringue dans sa nuque!\nIl s'effondre et vous en profitez pour fuir!\nVotre ingéniosité vous a permis de triompher",UserName,"! BRAVO!")	
			return False

		if MazeMap[NewOrdonate][NewAbsciss] == "O" and Object.IsReadyForVictory == False: #len(cls.ObjectsTaken) != len(ObjectsList):
			print("\nVotre frèle condition physique ne vous permettais pas d'affronter cette montagne de muscles! Il se retourne vers vous et vous écrabouille sans la moindre lueur de compassion dans le regard. Vous avez échoué!")
			return False

		#Managing of the objects:
		if (MazeMap[NewOrdonate][NewAbsciss] != " "):
			
			for FoundObject in Object.FullObjectList:
				if (FoundObject.DisplaySymbol == MazeMap[NewOrdonate][NewAbsciss]):
					Object.PutInBackpack(FoundObject)

			# FoundObject = (
			# 	Object for Object in Object.FullObjectList 
			# 	if Object.FullObjectList.DisplaySymbol == MazeMap[NewOrdonate][NewAbsciss])		
			# Object.PutInBackpack(FoundObject)

		# if (MazeMap[NewOrdonate][NewAbsciss] == "E" 
		# 	or MazeMap[NewOrdonate][NewAbsciss] == "T" 
		# 	or MazeMap[NewOrdonate][NewAbsciss] =="A"
		# 	or MazeMap[NewOrdonate][NewAbsciss] == "B"
		# 	or MazeMap[NewOrdonate][NewAbsciss] == "b"):

		# 	if MazeMap[NewOrdonate][NewAbsciss] == "E":
		# 		print("\nDe l'{}".format(ObjectsList[0][0]))
		# 		Object.PutInBackpack(ObjectsList[0])
				
		# 	if MazeMap[NewOrdonate][NewAbsciss] == "T":
		# 		print("\nUn {}".format(ObjectsList[1][0]))
		# 		Object.PutInBackpack(ObjectsList[1])
				
		# 	if MazeMap[NewOrdonate][NewAbsciss] == "A":	
		# 		print("\nUne {}".format(ObjectsList[2][0]))
		# 		Object.PutInBackpack(ObjectsList[2])
				
		# 	if MazeMap[NewOrdonate][NewAbsciss] == "B":	
		# 		print("\nUne {}".format(ObjectsList[3][0]))
		# 		Object.PutInBackpack(ObjectsList[3])
				
		# 	if MazeMap[NewOrdonate][NewAbsciss] == "b":	
		# 		print("\nUne {}".format(ObjectsList[4][0]))
		# 		Object.PutInBackpack(ObjectsList[4])
				
			Object.CheckIfReadyForVictory()
			
		#Delating the old position for display:
		MazeMap[cls.Ordonate][cls.Absciss] = " "

		#Define the new player's location:
		cls.Absciss = NewAbsciss
		cls.Ordonate = NewOrdonate

		#Display the new player's location:
		MazeMap[cls.Ordonate][cls.Absciss] = "X"
		
		return True	