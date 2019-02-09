from sys import exit


def gold_room():
    print("This room is full of gold. ")

    while True:
        print("How much do you take?")
        choice = input(">")

        if choice.isnumeric():
            how_much = int(choice)

            if 0 < how_much < 50:
                print("Nice, you are not greedy, You win!")
                exit(0)
            elif how_much < 0:
                print("Are you out of your mind?")
            else:
                dead("You greedy shiat!")
                exit(0)

        else:
            print("That's not an amount")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input(">")

        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "Taunt bear" and bear_moved:
            dead("The bear gets pissed off and farts at you.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the Great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for you life or eat your head?")

    choice = input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")



start()