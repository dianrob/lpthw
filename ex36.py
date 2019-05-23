from sys import exit


def green_room():
    print("You enter a green room")
    print("There is an table standing in the middle with a lot of untensiles.")
    print("A grinder, some good looking weed, papes and a filterbox")


    while True:

        preparation = False
        choice = input("> What do you do? ")

        if "grinder" in choice and "weed" in choice:

            print("You know your skills.")
            preparation = True
            roll = input("What now?")
            if "papes" in roll and "filter" in roll and preparation == True:
                print("All right. You got it done and light it up!")
                white_room()
            else:
                print("Try again!")
                exit(0)
        else:
            print("Try again!")


def white_room():
    exit(0)

def entry():
    print("You appear on a vast plane.")
    print("Three doors materialize in front of you: One green, another white and the last seems to be opaque.")
    print("A voice in your head whispers.. I should choose a door")

    choice = input("> Choose a door: ")

    if choice == "green":
        green_room()
    elif choice == "white":
        white_room()
    elif choice == "opaque":
        opaque_room()
    else:
        print("Please choose one of the doors!")

entry()
