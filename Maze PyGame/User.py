#-*-coding:UTF-8-*

class User:

	@staticmethod
	def GetName():
		"""
			Get the user's name
		"""
	
		return input("\nEntrez votre nom: ")


	@staticmethod
	def Greetings(UserName):
		"""
			Check if a name has been written by the user.
			If this is the case it prints the welcome sentence using the name.
		"""
		
		print("\nBonjour", UserName,"c'est à vous de jouer!")