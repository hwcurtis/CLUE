import sys
import pandas as pd
print("""Welcome, to todays  challenge, there has been an SOS from a group of people , we are unsure the number but they have given a location on
 a forgotten Island , this is the information we were provided, shoud you choose to proceed, please enter your name bellow"")
 
been gone or the supplies they may need, but it's almost guaranteed the food supply is low. Also not sure of their "physical condition".
In short, just be prepared for anything.""")


name = input(
    "If you dare to proceed, please tell us your name: , otherwise type exit  ").strip()
if name.lower() == "exit":
    print("You have chosen to exit the game. Wise Choice  Goodbye!")
    sys.exit()


allowed_names = ["george", "william", "chris", "bre", "riley"]
if name.lower() in allowed_names:
    print(f"Welcome {name}, please let's get started as time is ticking ")
else:
    print("Be wise and exit the game. Only authorized rescuers may proceed.")
    sys.exit()


print("""The first objective is to find your way down the hill, that much you are aware,  the lights you see are below you, but how far down and which way?
After all, you must be safe; you're needed to rescue people, not be rescued yourself—how embarrassing would that be? Now, which way did they say, or did they?""")
print("You have three choices: left, right, or straight ahead. Which way do you choose?")
direction = input(
    "Please choose a direction (left, right, straight): ").strip().lower()


if direction == "left":
    print("""choosing left which is closer looks like a good choice, but not a "direct route", as it leads away from most lights,
    it could take precious time, you may not want to lose""")


elif direction == "right":
    print("""choosing right, which is a more direct route, but it is also the steepest and most dangerous, you could fall and hurt yourself,
    or worse, you could be lost forever.""")
    print('Do you risk the steep hill or take the longer route?')
    risk = input(
        "Do you choose to risk the steep decent ? (yes/no): ").strip().lower()
    # You can add more logic here based on the risk input if desired


elif direction == "straight":
    print("""You chose to go straight ahead, hoping it's the safest and quickest route. You proceed cautiously, keeping an eye out for any signs or clues.""")


else:
    print("Invalid direction chosen. Please restart the game and choose left, right, or straight.")
    sys.exit()


print("At the bottom of the hill you find a row boat and paddles and you can barely make out a light in the distance, maybe it's the Island you have been searching for.")
print("""Your choices are: the row boat, a jet ski, or a sail boat. The question is , how many people are waiting for you? and which of these do you think you can handle,
keeping in mind there is a time limit to get to the island to help them.""")


pass


# print("""As you're moving towards the choices you see a bag, which has several weapons: a small gun, a knife, and a bigger gun, also a net. Depending on the vessel will
# depend on which to choose, because you also see food and medical equipment. All would be good to have when you reach the island.""")


# print("How much food and what kind of medical supplies and what for transportation not to mention the weapons, so much to decide in so little time will you get there quick enough")


boat_choice = input(
    "Which vessel do you choose: sailboat, jet ski, or fishing boat (with an engine)? ").strip().lower()


# if "sailboat" in boat_choice:
#    print("Will there be enough wind?")
# elif "jet ski" in boat_choice or "jetski" in boat_choice:
# print("There won't be enough room for everything, you could go help, but not have any supplies.")
# elif "fishing" in boat_choice or "engine" in boat_choice:
#  print("There should be enough room to carry supplies and if needed a few people can return with you.")
# else:
#   print("You hesitate to choose a vessel, and time is running out!")
pass


# def get_coordinates():
"""Generate random coordinates for the rescue mission."""
# latitude = random.uniform(-90, 90)
# longitude = random.uniform(-180, 180)
# return latitude, longitude
