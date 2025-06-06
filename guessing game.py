print("Welcome to the game of choice, you have less than an hour to make your way out safely. Any more time may result in an unfavorable outcome.")

name = input("If you dare to enter, please tell us your name: ")

print(f"Welcome {name}, please let's get started as time is ticking.")

print("""This being a game of best choices, and limited time, you want to find the correct path. There are three: one to the right,
which as far as you can see looks safe; the one to the left slopes downward— is that the way out Or the one straight ahead that goes up a steep hill...""")


choice = input("Which way do you go? (straight/right/left): ").lower()

if choice == "left":
    print("You find yourself going down a steep hill, not sure what will be at the bottom.")
    print("You reach the bottom and find a snorkel and goggles. Ahead of you is a body of water.")
    swim = input(
        "Do you swim or continue on foot? (swim/foot): ").lower()
    if swim == "swim":
        print("You bravely swim across the water, hoping for the best...")
    elif swim == "foot":
        print("You continue on foot, keeping an eye on the ticking clock...")

    bike_choice = input(
        "Do you jump on the bike or start to run? (bike/run): ").lower()
    if bike_choice == "bike":
        print("You jump on the bike and speed away, hoping you don't crash!")
    elif bike_choice == "run":
        print("You start to run as fast as you can, hoping to beat the clock!")
    else:
        print("Invalid choice. You hesitate and lose precious time!")

elif choice == "right":
    print("Right looks the safest as far as you can tell, but what lies ahead?")
    print("As you start to move in that direction, you trip over an object, which you later realize is a bucket with a knife, gun, and rope.")
    item = input("Which one would you choose? (knife/gun/rope): ").lower()
    if item not in ["knife", "gun", "rope"]:
        print("Invalid choice. You hesitate and lose precious time!")

    print(f"You pick up the {item} and proceed cautiously...")
    print("As you continue right, you hear a noise. Do you wait to see what it is, hide and wait for it to pass, or throw your weapon and hope for the best?")
    action = input("What do you do? (wait/hide/throw): ").lower()
    if action == "wait":
        print("You wait and see a harmless animal pass by. You continue on your way.")
    elif action == "hide":
        print("You hide and the noise passes. You feel safer and move on.")
    elif action == "throw":
        print(
            f"You throw your {item}, but nothing happens. You continue, now unarmed.")
    else:
        print("Unable to decide, you lose precious time.")

elif choice == "straight":
    print("Straight ahead seems to be the way you want to go, but your fear of heights makes you hesitate")
    print("You climb the steep hill, determined to find your way out...")
else:
    print("WOW that was fast you must join our team ")

    print("Congratulations on playing this game, we hope to see you again real soon.")
