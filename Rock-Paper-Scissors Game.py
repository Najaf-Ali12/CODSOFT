#Rule :Rock is superior than Scissor, Scissor is superior than paper and paper is superior than rock
import random
users_score=0
total_rounds=0
total_draw=0
computer_score=0
list_of_options=["ROCK","PAPER","SCISSOR"]
print("Welcome to the entertainment world of Rock, Paper Scissor")
while True:
    selection=input("what is your choice (Rock,Paper or Scissor):").upper()
    if selection in list_of_options:
        randomoption=random.choice(("ROCK","PAPER","SCISSOR"))
        print("Computer's choice is:",randomoption)
        if selection == randomoption:
            print("It's a draw!")
            total_draw += 1
        elif (selection == "ROCK" and randomoption == "SCISSOR") or \
         (selection== "PAPER" and randomoption == "ROCK") or \
         (selection== "SCISSOR" and randomoption == "PAPER"):
            print("You won!")
            users_score += 1
        else:
            print("You lost")
            computer_score+=1
        total_rounds+=1
    else:
        print("Recheck your input and try again")
        continue
    choice=input("1:play\n2:view result\n3:EXIT\nEnter 1,2 or 3:")
    try:
        if choice=="1":
            continue
        elif choice=="2":
            print("\n**Game Summary**")
            print("You played:",total_rounds,"rounds")
            print("you won:",users_score)
            print("Computer won:",computer_score)
            print("Draws:",total_draw)
            print("\nThanks for playing!")
            break
        elif choice=="3":
            break
        else:
            print("INVALID CHOICE!")
            break
    except:
        print("See")



