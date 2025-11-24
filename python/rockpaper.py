import random

rps = ["rock", "paper", "secissors"]
userr = input("Choose rock paper secissors ")

computer = random.choice(rps)

# print(computer)

if userr == computer:
    print("its a draw")
elif (
    (userr == "rock" and computer == "secissors")
    or (userr == "paper" and computer == "rock")
    or (userr == "secissors" and computer == "paper")
):
    print("you won")
else:
    print("you have lost")
