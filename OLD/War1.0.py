import time
import random
cl = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 20] # cl = card_list, with 13 entries (2-10, 11=J 12=Q 13=K 20=Ace)
s = " "
se = s * 3
error = "You messed up somehow. Please try again."
mp = 10  # mp = max_points
# fix printing (j, q, k, a)


class Player:
	def __init__(self, name):
		self.name = name
		self.name = None
		self.score = 0
		self.card = None
	
	def add_point(self):
		self.score += 1
	
	def draw1card(self):
		self.card = random.choice(cl)


def game(one, two):
	game_done = False
	
	while not game_done:
		one.draw1card()
		two.draw1card()

		def print_cards(one, two):
			pl = []
			# checking for j/q/k/a (for one)
			if one.card == 11:
				pl.append("J")
			elif one.card == 12:
				pl.append("Q")
			elif one.card == 13:
				pl.append("K")
			elif one.card == 20:
				pl.append("Ace")
			else:
				pl.append(str(one.card))
			pl.append(se)
			# checking for j/q/k/a (for two)
			if two.card == 11:
				pl.append("J")
			elif two.card == 12:
				pl.append("Q")
			elif two.card == 13:
				pl.append("K")
			elif two.card == 20:
				pl.append("Ace")
			else:
				pl.append(str(two.card))
			print(*pl)

		print_cards(one, two)

		who = input("Who won? Answer: ")
		if who.lower() == "one":
			who = one.name
		elif who.lower() == "two":
			who = two.name
		elif who == 1:
			who = one.name
		elif who == 2:
			who = two.name
		elif who == 0:
			who = 0
		else:
			who = who.capitalize()

		if who == one.name:
			if one.card > two.card:
				print("Correct! One point has been added to " + str(one.name) + "'s score!")
				one.add_point()
			elif two.card > one.card:
				print("Incorrect! One point has been added to " + str(two.card) + "'s score because they won.")
				two.add_point()
			elif one.card == two.card:
				print("Incorrect! Neither of you won, so let's draw again! No points added.")
		elif who == two.name:
			if two.card > one.card:
				print("Correct! One point has been added to " + str(two.name) + "'s score!")
				two.add_point()
			elif one.card > two.card:
				print("Incorrect! One point has been added to " + str(one.card) + "'s score because they won.")
				one.add_point()
			elif two.card == one.card:
				print("Incorrect! Neither of you won, so let's draw again! No points added.")
		elif who == "Nobody" or who == "None of us" or who == "Both" or who == 0:
			if one.card == two.card and one.card == two.card:
				print("Correct! Neither of you won, so let's draw again! No points added.")
			elif one.card > two.card:
				print("Incorrect! One point has been added to " + str(one.card) + "'s score because they won.")
				one.add_point()
			elif two.card > one.card:
				print("Incorrect! One point has been added to " + str(two.card) + "'s score because they won.")
				two.add_point()

		if one.score == mp:
			game_done = True
		elif two.score == mp:
			game_done = True
	
	# end game message
	if one.score == mp:
		print("Congradulations! " + one.name + " won the game with " + str(mp) + " points! Yay!")
	else:
		print("Congradulations! " + two.name + " won the game with " + str(mp) + " points! Yay!")
	
	time.sleep(2.5)
	print("I hope you enjoyed playing my slightly-different version of War! :)")
	time.sleep(1)

		
def main():
	print("Hello! Welcome to this game called \"War\"!")
	print("This was made by Logan, with help from Nova.")
	
	name1 = input("What is player #1's name? Name: ")
	name2 = input("What is player #2's name? Name: ")
	
	one = Player(name1)
	two = Player(name2)
	
	while True:
		cont1 = input("Would you like to start the game?\n")
		cont1 = cont1.lower()
		if cont1 == "y" or cont1 == "yes":
			game(one, two)
			break
		elif cont1 == "n" or cont1 == "no":
			print("Okay. Exiting War now.")
			time.sleep(2)
			break
		else:
			print(error)
			print(s)
	
	play_again = input("Would you like to play again? y/n: ")
	if play_again.lower == "y":
		main()
	else:
		print("Okay. Exiting War now.")
		time.sleep(2)
	
	
main()
