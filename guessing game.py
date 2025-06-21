import pandas as pd
import sys

print('WELCOME TO THE RESCUE MISSION, should you choose to accept it!')
print("""These are the details we have at the moment, folks are in need of rescue on a remote isalnd, we know
      very little information about the situation, other than we are working to find the coordinates  and will be provided to you should you
choose to accept such challenges. Please start moving quickly to the next stop, instructions will be provided as you go along.
Good luck and may the odds be ever in your favour!""")
name = input(
    "If you dare to proceed, please tell us your name: ").strip()
if name.lower() == "exit":
    print("You have chosen to exit the game. Wise Choice  Goodbye!")
    sys.exit()


allowed_names = ["george", "william", "chris", "bre", "riley"]
if name.lower() in allowed_names:
    print(f"Welcome {name}, please let's get started as time is ticking ")
else:
    print("Be wise and wait right there, you will  be escorted to the exit, you are not welcome here")
    sys.exit()
