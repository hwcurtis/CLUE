print("Welcome to the game of choice, you have less than an hour to make your way out safely, anymore time may result in unfavorable outcome, ")

name = input("If you dare to enter, please tell us your name: ")

print(f"Welcome {name}, please let's get started as time is ticking.")

print("""This being a game of best choices, and limited time, you want to find the correct path. There are three: one to the right,
which as far as you can see looks safe; the one to the left slopes downward— is that the way out Or the one straight ahead that goes up a steep hill...""")


choice = input("Which way do you go? (straight/right/left): ").lower()

if choice == "left":
    print("You find yourself going down a steep hill, not sure what will be at the bottom.")
    print("You reach the bottom and find a snorkel and goggles. Ahead of you is a body of water.")
    swim = input(
        "Do you swim across or continue on foot? (swim/foot): ").lower()
    if swim == "swim":
        print("You bravely swim across the water, hoping for the best...")
    else:
        print("You continue on foot, keeping an eye on the ticking clock...")

elif choice == "right":
    print("Right looks the safest as far as you can tell, but what lies ahead?")
    print("As you start to move in that direction, you trip over an object, which you later realize is a bucket with a knife, gun, and rope.")
    item = input("Which one would you choose? (knife/gun/rope): ").lower()
    print(f"You pick up the {item} and proceed cautiously...")

elif choice == "straight":
    print("Straight ahead seems to be the way you want to go, after seeing a gun, knife, and a rope.")
    print("You climb the steep hill, determined to find your way out...")

else:
    print("WOW that was fast you must join our team ")
