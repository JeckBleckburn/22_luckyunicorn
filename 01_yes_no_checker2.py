show_instructions = ""
while show_instructions.lower() != "xxx":

    show_instructions = input("Have you played this game before? ").lower()
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("Program continues")

    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")

    else:
        print("Please answer yes / no")

    print("You chose {}".format(show_instructions))
