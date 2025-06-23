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
    print("Be wise and wait right there. You will be escorted to the exit.")
    time.sleep(2)
    choice = input(
        "You don't want to exit, you have come to help. What do you choose (run/hide/exit): ").strip().lower()


# print("You have made your choice, now let's see what happens next.")
# print("You are now at the rescue point, and see a few boats. Which one would you choose: the sailboat, the motorboat, or the kayak?")


#
# print("You have chosen to exit the game. Wise Choice  Goodbye!")
# sys.exit()
# if name.lower() == "exit":
#   print("You have chosen to exit the game. Wise Choice. Goodbye!")
#  sys.exit()

    #  "...unless you'd rather run and hide? Choose quickly! (run/hide/exit): ").strip().lower()
