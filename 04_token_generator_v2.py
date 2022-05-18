from time import sleep
import random


def num_check(question, lowest, highest,):
    error = "Please enter a amount between 1 and 10 plz"

    valid = False
    while not valid:
        try:
            bank = int(input(question))

            if lowest < bank <= highest:
                print("You have asked to play with ${}".format(bank))
                return bank

        except ValueError:
            print(error)



balance = num_check("How much would you like to pay With\n>>>", 0, 10,)
sleep(1)


def token_game(balance):
    token = ["unicorn", "horse", "horse", "horse", "zebra", "donkey", "donkey", "donkey", "donkey"]
    token_gen = True
    while token_gen:
        try:
            rounds = int(input("--How many rounds would you like to play--"))
            if rounds <= balance:
                for item in range(1, rounds + 1):
                    chosen_num = random.choice(token)

                    if chosen_num == "unicorn":
                        balance += 4
                    elif chosen_num == "donkey":
                        balance -= 1
                    else:
                        balance -= .5

                    print("Token: {} , Balance: ${}".format(chosen_num, balance))
                    print("-------------------------")
                    sleep(.5)

                    if balance <= .5:
                        token_gen = False

        except ValueError:
                print("Must be equal or lower than your balance")


token_game(balance)




