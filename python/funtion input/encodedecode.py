

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']




# def encode(text , shift):
#     indee = []
#     encoded=""
#     for i in text:
#         if i in alphabet:
#             new = (alphabet.index(i) + shift)%26
#             indee.append((alphabet[new]))
#         else:
#             encoded+=i
#     for j in indee:
#         encoded+=j
#
#
#     print(encoded)
#
#
#
#     # print(indee)
#
# def decode(text, shift):
#     indee = []
#     decoded = ""
#     for i in text:
#         if i in alphabet:
#             new = (alphabet.index(i) - shift) % 26
#             indee.append((alphabet[new]))
#         else:
#             decoded += i
#     for j in indee:
#         decoded += j
#
#     print(decoded)
#
# def runfun(direction):
#     if direction == "encode":
#         encode(text, shift)
#     elif direction == "decode":
#         decode(text, shift)
#     elif direction == "exit":
#         print("exted")
#     else:
#         print("eroor")



def ciper(direction , text , shift):
    encoded = ""
    for i in text:
        if i in alphabet:
            if direction == "encode":
                new = (alphabet.index(i) + shift) % 26
                encoded += alphabet[new]
            elif direction == "decode":
                new = (alphabet.index(i) - shift) % 26
                encoded += alphabet[new]
            elif direction == "exit":
                break

            else:
                print("try again")

        else:
            encoded += i

    print(encoded)
    return encoded

should_continue = True

while should_continue:
    direction = input("type encode to or decode to proceed: \n").lower()
    text = input("Enter your message: \n" )
    shift = int(input("Enter shift number: \n"))
    ciper(direction,text,shift)
    continuethegame = input("do you want to continue the game yes / no ").lower()
    if continuethegame == "no"  :
        print("Good Bye")
        should_continue = False


