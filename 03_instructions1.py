
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
    print("----How To Play----")
    print("")
    print("")
    print("")


show_instructions = yes_no("Have you played this game before? ").lower().strip()
if show_instructions == "yes":
    instructions()
else:
    print("Well since you're Sooooo smart just play then\n Don't Come crying to me")
