
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


def instructions(question):
    print("Here are the Instructions")

    helpneed = input(question).lower().strip()

    if helpneed == "Yes" or helpneed == "Y":
        print("That's ok here you go")
        instructions()

    else:
        print("Ok that good lets start the game")


morehelp = instructions("are you ok with the rules? >>> Y/N")

show_instructions = yes_no("Have you ever played this game before?").lower().strip()

if show_instructions == "no":
    instructions()

else:
    print("Well lets get you started then")
