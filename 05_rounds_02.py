import random

balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()

token = ["unicorn", "horse", "horse", "horse", "zebra", "donkey", "donkey", "donkey", "donkey"]
while play_again == "":


    rounds_played += 1

    print()
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
                       "or 'xxx' to quit")

print()
print("Final balance", balance)
