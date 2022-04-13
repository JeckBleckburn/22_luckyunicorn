show_instructions = ""
while show_instructions.lower() != "xxx":

    show_instructions = input("Have you played this game"
                              "before? ").lower()
    if show_instructions == "yes":
        print("Program continues")

    elif show_instructions == "y":
        print("Display instructions")

    elif show_instructions == "no":
        print("Display instructions")

    elif show_instructions == "n":
        print("Display instructions")

    else:
        print("Please answer yes / no")

    print("You chose {}".format(show_instructions))
