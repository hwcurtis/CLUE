import random
import sys
print("""Welcome to the game of choice, you have less than an hour to make your way out safely. Any more time may result in an unfavorable outcome, or simply type exit to quit if
you fear for your life.""")

name = input("What is your name? ").strip()


if name.lower() == "exit":
    print("You have chosen to exit the game. Wise Choice  Goodbye!")
    sys.exit()
    exit()


print(f"Welcome {name}, please let's get started as time is ticking.")


print("""This being a game of search and rescue,the details you have been told, there is an island, in which people have been stranded, they sent out an sos ,
      there is a need for an emergency rescue """)


print("""The one to the right is closest and the path looks easy, but what lies beyond?
The one to the left leads into trees, but there is a light in the distance.""")


choice = input("Which way do you choose: the smooth path which is closer, or the path that leads into the trees but has a distant light? ").strip().lower()


if "smooth" in choice or "right" in choice:
    print("Look out ahead, there is a hill, which has a body of water at the bottom, maybe full of sharks and snakes.")
elif "left" in choice or "trees" in choice or "light" in choice:
    print("You head into the trees towards the distant light, unsure of what awaits you.")
else:
    print("You hesitate, unable to decide, and time keeps ticking...")


print("At the bottom of the hill you find a row boat and paddles and you can barely make out a light in the distance, maybe it's the Island you have been searching for.")
print("""Your choices are: the row boat, a jet ski, or a sail boat. The question is, how many people are waiting for you? and which of these do you think you can handle,
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
