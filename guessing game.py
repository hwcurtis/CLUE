<<<<<<< HEAD
import sys
print("""Welcome, to todays  challenge, there has been an SOS from a group of people , we are unsure the number but they have given a location on
 a forgotten Island , this is the information we were provided, shoud you choose to proceed, please enter your name below, however
 if you have a change of heart, dont hesitate to exit and allow someone else a chance .""")

print("""The objective of the game is to quickly find the lost island and rescue the people. Not certain how long they have
been gone or the supplies they may need, but it's almost guaranteed the food supply is low. Also not sure of their "physical condition".
In short, just be prepared for anything.""")


name = input(
    "If you dare to proceed, please tell us your name: , otherwise type exit  ").strip()
=======
import random
import sys
print("""Welcome, to todays  challenge, there has been an SOS from a group of people , we are unsure the number but they have given a location on
 a forgotten Island , this is the information we were provided, shoud you choose to proceed, please enter your name below, however 
 if you have a change of heart, dont hesitate to exit and allow someone else a chance ,.""") 

The cordinates are latitude 22 04'60.00"N
-159 29' 59.99"W


name = input("What is your name? ").strip()


>>>>>>> 09510cd83f0382f8d79926d103527858891c9bb7
if name.lower() == "exit":
    print("You have chosen to exit the game. Wise Choice  Goodbye!")
    sys.exit()

<<<<<<< HEAD
allowed_names = ["george", "william", "chris", "bre", "riley"]
if name.lower() in allowed_names:
    print(f"Welcome {name}, please let's get started as time is ticking ")
=======

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
>>>>>>> 09510cd83f0382f8d79926d103527858891c9bb7
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
    print{'Do you risk the steep hill or take the longer route ')
    risk = input(
        "Do you choose to risk the steep decent ? (yes/no): ").strip().lower()


print("At the bottom of the hill you find a row boat and paddles and you can barely make out a light in the distance, maybe it's the Island you have been searching for.")
print("""Your choices are: the row boat, a jet ski, or a sail boat. The question is , how many people are waiting for you? and which of these do you think you can handle,
keeping in mind there is a time limit to get to the island to help them.""")


# print("""As you're moving towards the choices you see a bag, which has several weapons: a small gun, a knife, and a bigger gun, also a net. Depending on the vessel will
# depend on which to choose, because you also see food and medical equipment. All would be good to have when you reach the island.""")


# print("How much food and what kind of medical supplies and what for transportation not to mention the weapons, so much to decide in so little time will you get there quick enough")


# boat_choice = input(
"Which vessel do you choose: sailboat, jet ski, or fishing boat (with an engine)? ").strip().lower()


<<<<<<< HEAD
    # if "sailboat" in boat_choice:
    #    print("Will there be enough wind?")
    # elif "jet ski" in boat_choice or "jetski" in boat_choice:
    # print("There won't be enough room for everything, you could go help, but not have any supplies.")
    # elif "fishing" in boat_choice or "engine" in boat_choice:
    #  print("There should be enough room to carry supplies and if needed a few people can return with you.")
    # else:
    #   print("You hesitate to choose a vessel, and time is running out!")
=======
if "sailboat" in boat_choice:
    print("Will there be enough wind?")
elif "jet ski" in boat_choice or "jetski" in boat_choice:
    print("There won't be enough room for everything, you could go help, but not have any supplies.")
elif "fishing" in boat_choice or "engine" in boat_choice:
    print("There should be enough room to carry supplies and if needed a few people can return with you.")
else:
    print("You hesitate to choose a vessel, and time is running out!")
>>>>>>> 09510cd83f0382f8d79926d103527858891c9bb7
