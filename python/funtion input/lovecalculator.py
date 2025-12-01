

def calculate_love_score(name1 , name2):
    new1=name1.lower()
    new2=name2.lower()
    true_v = ["t", "r", "u", "e", ]
    countt = 0
    love_v = ["l", "o", "v", "e", ]
    countl = 0


    for i in new1  :
        if i in  true_v :
            countt+=1
    for j in new2  :
        if j in  true_v :
            countt+=1
    for k in new1:
        if k in love_v:
            countl += 1
    for l in new2:
        if l in love_v:
            countl += 1

    print(f"The love Score for {name1} and {name2} is {countt}{countl}")


calculate_love_score("Ayush", "Anshika Ananad")