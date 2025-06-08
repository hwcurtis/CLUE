import random
import sys
print("""Welcome, to todays  challenge, there has been an SOS from a group of people , we are unsure the number but they have given a location on
 a forgotten Island , this is the information we were provided, shoud you choose to proceed, please enter your name below, however 
 if you have a change of heart, dont hesitate to exit and allow someone else a chance .""")


name = input(
    "If you dare to proceed, please tell us your name: , otherwise type exit  ").strip()
if name.lower() == "exit":
    print("You have chosen to exit the game. Wise Choice  Goodbye!")
    sys.exit()


print(f"Welcome {name}, please let's get started as time is ticking ")

print("""This being a game of best choices, and limited time, you want to find the correct path. There are two: one to the right,
and one to the left, which one leads to the lost island?  Remember, there is a catch, the folks on the island are counting on you """)


print("""The one to the right is closest and the path looks easy, but what lies beyond?
The one to the left leads into forest, but there is a light in the distance.""")


print("""The one to the right is closest and the path looks easy, but what lies beyond?
The one to the left leads into a forest, there is a light in the distance.""")


choice = input("Which way do you choose:  smooth path which is closer, or the path that leads into the forest but has a distant light?  ").strip().lower()


if "smooth" in choice or "right" in choice:
    print("Look out ahead, there is a hill, which has a body of water at the bottom, maybe full of sharks and snakes.")
elif "left" in choice or "trees" in choice or "light" in choice:
    print("You head into the forest towards the distant light, unsure of what awaits you.")
else:
    print("You hesitate, unable to decide, and time keeps ticking...")


print("At the bottom of the hill you find a row boat and paddles and you can barely make out a light in the distance, maybe it's the Island you have been searching for.")
print("""Your choices are: the row boat, a jet ski, or a sail boat. The question is , how many people are waiting for you? and which of these do you think you can handle,
keeping in mind there is a time limit to get to the island to help them.""")


print("""As you're moving towards the choices you see a bag, which has several weapons: a small gun, a knife, and a bigger gun, also a net. Depending on the vessel will
depend on which to choose, because you also see food and medical equipment. All would be good to have when you reach the island.""")


print("How much food and what kind of medical supplies and what for transportation not to mention the weapons, so much to decide in so little time will you get there quick enough")


boat_choice = input(
    "Which vessel do you choose: sailboat, jet ski, or fishing boat (with an engine)? ").strip().lower()


if "sailboat" in boat_choice:
    print("Will there be enough wind?")
elif "jet ski" in boat_choice or "jetski" in boat_choice:
    print("There won't be enough room for everything, you could go help, but not have any supplies.")
elif "fishing" in boat_choice or "engine" in boat_choice:
    print("There should be enough room to carry supplies and if needed a few people can return with you.")
else:
    print("You hesitate to choose a vessel, and time is running out!")
