import random
import time


def get_random_word():
	"""Creates random word from list"""
	names_listed = ['apple', 'orange', 'dog', 'cat', 'fish', 'pineapple', 'mushroom']
	# Generate random name from list names_listed
	random_word_test = random.choice(names_listed)
	random_word = list(random_word_test)
	return random_word


def show_message(grw):
	"""Print prompt message and print number of letters"""
	message1 = "Hello there!"
	message1 += "\nLet me think about a word...."
	print(message1)
	time.sleep(2)
	message2 = "Ok, I have a word in my mind!"
	message2 += f"\nIt's a  {len(grw)} letter word!"
	message2 += "\nNote : Type one letter at a time"
	print(message2)
	time.sleep(0.5)
	print("     ------")
	print("     |    |")
	print("     |    ")
	print("     |    ")
	print("     |    ")
	print("     |    ")
	message3 = "\nStage's set,now start guessing ( ͡° ͜ʖ ͡°)"
	print(message3)


def letter_found(user_letter, hidden_list, grw):
	"""If letter found update hidden_list"""
	print(f"\nYou guessed it right! '{user_letter}' is in my word!")
	for i in range(len(grw)):
		character = grw[i]
		if character == user_letter:
			hidden_list[i] = grw[i]


def letter_not_found(attempts):
	"""If letter not found add 1 attempt to attempts"""
	print("\nNope! I can't find a matching letter in my word!")
	attempts = attempts + 1
	return attempts


def draw_hangman(attempts):
	"""Draw hangman based on attempts"""
	time.sleep(1)
	print("     ------")
	print("     |    |")
	print("     |    " + ("O" if attempts >= 1 else ""))
	print("     |    " + ("/\\" if attempts >= 2 else ""))
	print("     |    " + ("|" if attempts >= 3 else ""))
	print("     |    " + ("/\\" if attempts >= 4 else ""))
	print(" --------")
	time.sleep(1)


def print_status(hidden_list):
	"""Print words found by player"""
	print(str(hidden_list) + "\n")


def player_won():
	"""Announce player won the game"""
	print("\nBingo! You've own the game! ( ͡o ͜ʖ ͡o) ")
	print("You saved an innocent man from death!")
	print("Bye champ!, game is closing now...")
	time.sleep(1)


def player_lose():
	"""Announce player ran out of attempts"""
	print("You ran out of attempts :(")
	print("Our man is dead:( ")
	print("\nBye! Game is closing now...")
	time.sleep(1)
