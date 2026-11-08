import random

print("""

        Game gussing 

""")

def game_rock_paper_scissor_game() :
    chosses = ["Paper" , "Rock" ,"Scissor"]
    score_computer = 0
    score_user = 0 
    while score_computer < 3 and score_user < 3 : 
        computer_gussing = random.choice(chosses)

        user_chose = input(f"Ener your chose{chosses}:").strip().capitalize()

        if computer_gussing == "Paper" and user_chose == "Scissor" :
            score_user += 1
            print(f"""
    {name} Score :{score_user}
    Coputer Score :{score_computer}
    """)
        elif computer_gussing == "Rock" and user_chose == "Paper" :
            score_user += 1
            print(f"""
        {name} Score :{score_user}
        Coputer Score :{score_computer}
        """)
        elif computer_gussing == "Scissor" and user_chose == "Rock" :
            score_user += 1
            print(f"""
    {name} Score :{score_user}
    Coputer Score :{score_computer}
    """)
        elif computer_gussing == "Paper" and user_chose == "Rock": 
            score_computer += 1
            print(f"""
    {name} Score :{score_user}
    Coputer Score :{score_computer}
    """)
        elif computer_gussing == "Rock" and user_chose == "Scissor": 
            score_computer += 1
            print(f"""
    {name} Score :{score_user}
    Coputer Score :{score_computer}
    """)
        elif computer_gussing == "Scissor" and user_chose == "Paper": 
            score_computer += 1
            print(f"""
    {name} Score :{score_user}
    Coputer Score :{score_computer}
    """)
        else:
            print(f"Same choice {name} is :{user_chose} \n Computer choice : {computer_gussing}  \n Draw.")

def number_cards_game() :
    computer_gussing = random.randint(1,10)
    counter = 0
    print("You have 3 times")
    while counter < 3 :
        try:
            ansswer_user = int(input(f"the computer pulled a random card between (1-10) \n Can you geuss this  number card !! :"))
        except ValueError : 
            print("invaild value")
            continue
        except :
            print("invaild value")
        if computer_gussing > ansswer_user :
            counter += 1
            print(f"{ansswer_user} : Your choice is smaller than the selected card ")
        elif computer_gussing < ansswer_user :
            counter += 1
            print(f"{ansswer_user} : Your choice is bigger than the selected card")
        else:
            counter += 1 
            print(f"{name} Wow, you managed to figure out the card in just {counter} times")
            break

def color_balles_game() :
    balles = ["Red","Yellow","Green"]
    computer_choose = random.choice(balles)
    user_guess = input(f"We have a box with three balls,\n{balles} radom ball draw,\n Can you guess which ball\nWas pulled?:").strip().capitalize()

    if computer_choose == user_guess : 
        print(f"{name} You are Winer!")
    else:
        print(f"{name} you are loser the ball,\nWas drawed is :{computer_choose}")



name = input("Enter your name:").strip().capitalize()


if not name:
    print("Name can't be empty, Try agian")
else:
    while True : 
        try: 
            choose = int(input(f"""         Hello {name}
                            Which of the games do yiu want to play.
                            1-Rock - Paper - Scissors

                            2- Guess the cards 

                            3- Guess the color Ball

                            0- Exist
            """))
        except ValueError : 
            print("Invaild Value.")
            continue
        except:
            print("Invaild Value.")
        try:
            match choose :
                case 1 :
                    game_rock_paper_scissor_game()
                case 2 :
                    number_cards_game()
                case 3 :
                    color_balles_game()
                case 0 : 
                    print(f"{name} see you in another time.")
                    break
                case _:
                    print("Invaild Value.")
        except:
            print("Invaild Value.")

Add mini games project

