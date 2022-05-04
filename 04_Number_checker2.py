def Number_checker():
    error = "Please enter a number between 1 to 10"

    valid = False
    while not valid:
        try:
            reply = int(input("Enter a amount you want to spend between 1 and 10"))

            if reply >= 1 or reply <= 10:
                print("thank you.\nYou have asked to play with ${}".format(reply))
                return reply

        except ValueError:
            print(error)


Number_checker()
