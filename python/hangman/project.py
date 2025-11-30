import random

hangman_stages = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]

w_list = ["ayush", "aman", "rohit", "suman", "santy"]
randomword = random.choice(w_list)

hangman_stages.reverse()
print(randomword)

game_over = False
correct_letter = []
lives = len(hangman_stages) - 1

while not game_over:
    guess = input("guess a letter \n").lower()
    display = ""

    for letter in randomword:
        if letter in correct_letter or letter == guess:
            display += letter
        else:
            display += "_"

    if guess in randomword:
        correct_letter.append(guess)
    else:
        print(hangman_stages[lives])
        lives -= 1
        if lives < 0:
            game_over = True
            print("you lose")
            break

    print(display)

    if "_" not in display:
        game_over = True
        print("you win")
