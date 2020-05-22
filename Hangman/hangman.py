import hangman_game_functions as gf

# Crate a random word
grw = gf.get_random_word()

# Create a hidden list to add * respect to number of characters in random_word
hidden_list = []
for character in grw:
    hidden_list.append('*')

# Set max attempts and used attempts
max_attempts = 4
attempts = 0

# Print initial prompt
gf.show_message(grw)

# Start Game's main loop
game_running = True
while game_running:
    prompt1 = "\n Enter your guess here"
    prompt1 += f"\n(You've {max_attempts - attempts} attempts left) : "
    user_letter = input(prompt1)
    if user_letter in grw:
        gf.letter_found(user_letter, hidden_list, grw)
    elif user_letter not in grw:
        attempts = gf.letter_not_found(attempts)

# Draw hangman based on attempts left
    gf.draw_hangman(attempts)

# Print the words found by player in hidden_list and no. of attempts available
    gf.print_status(hidden_list)

# If user ran out of no. of attempts
    if attempts == max_attempts:
        gf.player_lose()
        game_running = False

# Announce player has own the game and quit
    if hidden_list == grw:
        gf.player_won()
        game_running = False
