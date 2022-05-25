import random


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
       print("Here are the Instructions")
       print("When the game begins, you will be prompted to enter how much money you will be spending to play.\nYou can spend a maximum of $10, and each dollar equals one round.\nEvery round you get to draw a random token. A donkey is worth nothing, a horse or zebra are worth 50 cents and a unicorn is worth $5.\nAfter the round ends, you can spend more of your earnings to play again.Skipping Instructions...")


def num_check(question, lowest, highest,):
    dumb = "Please enter a amount between 1 and 10 plz"

    valid = False
    while not valid:
        try:
            bank = int(input(question))

            if lowest < bank <= highest:
                print("thank you.\nYou have asked to play with ${}".format(bank))
                return bank

        except ValueError:
            print(dumb)


show_instructions = yes_no("Have you ever played this game before?").lower().strip()

if show_instructions == "no":
    instructions()

else:
    print("Well lets get you started then")


balance = num_check("How much would you like to pay With\n>>>", 0, 10,)


rounds_played = 0

play_again = input("Press <Enter> to play...").lower()

token = ["unicorn", "horse", "horse", "horse", "zebra", "donkey", "donkey", "donkey", "donkey"]
while play_again == "":
    rounds_played += 1

    print("*** Rounds #{} ***".format(rounds_played))

    chosen_num = random.choice(token)

    if chosen_num == "unicorn":
        balance += 4
    elif chosen_num == "donkey":
        balance -= 1
    else:
        balance -= .5

    print("Token: {} , Balance: ${}".format(chosen_num, balance))


    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again"
                       " or 'xxx' to quit")


print("Final balance", balance)

