import sys
import time

print('WELCOME TO THE RESCUE MISSION, should you choose to accept it!')
print("""These are the details we have at the moment, folks are in need of rescue on a remote island, we know
      very little information about the situation, but will be providing more information soon should you
choose to accept such challenges. Please maek your decision quickly as folks are waiting on a rescue 
""")

print("Good luck and may the odds be ever in your favour!")


name = input("If you dare to proceed, please tell us your name: ").strip()

allowed_names = ["george", "william", "chris", "bre", "riley"]

if name.lower() in allowed_names:
    print(
        f"Welcome, {name.capitalize()}. Let's get started — time is ticking!")
else:
    print("Be wise and wait right there. You will be escorted to the exit. You are not welcome here")
    time.sleep(2)
    choice = input(
        "You don't want to exit, you have come to help. What do you choose (run/hide/exit): ").strip().lower()


# print("You have made your choice, now let's see what happens next.")
# print("You are now at the rescue point, and see a few boats. Which one would you choose: the sailboat, the motorboat, or the kayak?

    #  "...unless you'd rather run and hide? Choose quickly! (run/hide/exit): ").strip().lower()

"""
Supplies you have been given, include, a water flask, night time gogles and a radio phone, in which you can be contancted
for updats, the main thing to know is, the SOS was from a remote island, where an unkown number of folks are waiting for rescue...THAT AND THAT YOU are on 
top of a very large moutnain ,as you know its pitch dark , we are unsure of the decent, except its steep, and full of trees until
you reach the bottom, in which you need to find the clearing with  the boats and more supplies  to satrt you will find supplies , which are ina  bag, consisiting of, a water flask, night goggles, roap and a falre gun, 
please use your outdoor skills and if your unsure if this is for you , please exit, as we dont need anyone taking away from our rescue efforts, 
best of luck and speed
please tell us your nsame and proceed with cautopn all we know for sure, is your currently on s high mountain, with only steep decenst
"""
