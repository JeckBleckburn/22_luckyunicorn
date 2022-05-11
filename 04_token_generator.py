from random import randint
import random

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


balance = num_check("How much would you like to pay with???\n>>>", 0, 10,)


token = ["unicorn", "horse", "zebra", "donkey"]

for item in range(0, 100):
    chosen_num = random.randint(1, 100)

    if 1 <= chosen_num <= 5:
        chosen_num = "unicorn"
        balance += 4
    elif chosen_num == "donkey":
        balance -= 1
    else:
        balance -= .5

    print("Token:{} , Balance${}".format(chosen_num, balance))



