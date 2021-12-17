print("""You enter a dark room with two doors. 
Do you go through door #1 or door #2 or door3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job.")
    elif bear == "2":
        print("The bear eats your legs off. Good job.")
    else:
        print(f"Well, doing {bear} id probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into endless abyss at Cthulhu' retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")


elif door == "3":
    print("You chosed a good door.")
    print("1. red ball.")
    print("2. blue ball")
    print("3. yellow ball.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Sorry, you died.")
        print("Good BYE!")
    else:
        print("VERY GOOD, Continue your game!")

        print("1. hair.")
        print("2. leg")
        print("3. head.")
        lastchose = input("> ")
        if lastchose == "1" or lastchose == "3":
            print("GAME OVER.")
            print("Good job!")
        else:
            print("Congratulations!")


else:
    print("You stumble around and fall on a knife and die. Good job!")