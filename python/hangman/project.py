import random

w_list = [
    "ayush",
    "aman",
    "rohit",
    "suman",
    "santy",
]
randomword = random.choice(w_list)

print(randomword)


rightg = ""


while not rightg == randomword:
    guesss = input("guess the letter?\n").lower()
    for l in randomword:
        if l == randomword:
            rightg += guesss
        else:
            rightg += "_"
print(rightg)
