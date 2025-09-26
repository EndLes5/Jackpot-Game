#Code by <\Endless>
#A python jackpot game that utilizes functions, loops(while loop) and python inbuilt modules(random, time & system)

#Modules
import random
import time
import os

#Function for clearing a previous output
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

#Random variable
pick = random.randrange(1, 4)

#Game variables
luckynum = str(pick)
mode = "Easy"
lives = 3
playagain = "b"

#Main game loop
def game():
	while lives > 0:
		def jackpotgame():
			#Global game variables
			global pick
			global luckynum
			global lives
			global mode
			#Loading screen
			def loader():
				print("----- ♤ Loading ♤ -----\nChoosing a random number\n\n(Try to guess the number)")
				time.sleep(2)
				clear()
			loader()
			#Introduction
			intro = "----- ♤ Jack Pot ♤ -----\n Mode: {} --- Lives: {}    \n\n♤ Enter 'm' to select modes ♤\n"
			print(intro.format(mode, lives))
			#Difficulty per selected mode
			if mode == "Easy":
				pick = random.randrange(1, 4)
				luckynum = str(pick)
				guess = input("Pick a lucky number from 1 to 3 : ")
			elif mode == "Mid":
				pick = random.randrange(1, 7)
				luckynum = str(pick)
				guess = input("Pick a lucky number from 1 to 6 : ")
			elif mode == "Hard":
				pick = random.randrange(1, 10)
				luckynum = str(pick)
				guess = input("Pick a lucky number from 1 to 9 : ")		
			#Mode/difficulty selector
			if guess.lower() == "m":
				clear()
				print("1. Easy\n2. Mid\n3. Hard\n\n")
				user = input("Select difficulty : ")
				if user == "1":
					mode = "Easy"
					clear()
					game()
				elif user == "2":
					mode = "Mid"
					clear()
					game()
				elif user == "3":
					mode = "Hard"
					clear()
					game()
				#Invalid mode input
				elif user != "1" or "2" or "3":
					clear()
					game()
			else:
				#Win condition
				if guess == luckynum:
					clear()
					print("----- ♤ YAYYY...Jack Pot ♤ -----")
					time.sleep(1)
					clear()
				else:
					#Loss condition
					lives -= 1
					clear()
					print("----- ♤ OOPS...Try again ♤ -----")
					time.sleep(1)
					clear()
		jackpotgame()
	else:
		#End of game loop
		print("----- ♤ Game Over ♤ -----\n\n ♡ You ran out of lives ♡\n\n")
		global playagain
		playagain = "b"
		#Rematch function
		def rematch():
			global playagain
			playagain = input("Enter 'a' to play again : ")
			if playagain.lower() == "a":
				while playagain == "a":
					clear()
					global lives
					lives = 3
					game()
			#Cancel rematch/end game
			if playagain.lower() != "a":
				playagain = "b"
				clear()
				print("----- ♤ Thanks for playing ♤ -----")
		rematch()
game()