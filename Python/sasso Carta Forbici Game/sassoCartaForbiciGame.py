import random

game_list = ['Sasso','Carta','Forbice']
computer = c = 0
command = p = 0
print("Score: Computer" + str(c) + " Player " + str(p))

#the loop
run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("Sasso, Carta, Forbice o Esci: ")
    if command == computer_choice:
        print("Tie")
    elif command == "Sasso":
        if computer_choice == "Forbice":
            print("Ha vinto il player!")
            p += 1
        else:
            print("Ha vinto il computer!")
            c += 1
    elif command == "Carta":
        if computer_choice == "Sasso":
            print("Ha vinto il player!")
            p += 1
        else:
            print("Ha vinto il computer!")
            c += 1   
    elif command == "Forbice":
        if computer_choice == "Carta":
            print("Ha vinto il player!")
            p += 1
        else:
            print("Ha vinto il computer!")
            c += 1
    elif command == "Esci":
        break
    else:
        print("Comand sbagliato!")
    print("Player: " + command)
    print("Computer: " + computer_choice)
    print("")
    print("Score: Computer " + str(c) + " Player " + str(p))
    print("")
