# import pandas as pd
# import random
# import sys

print('WELCOME TO THE RESCUE MISSION, should you choose to accept it!')
print("""These are the details we have at the moment, you have been asked to come, because your name precedes you, please be aware
the only information we have is there are people on a remote island, which the coordinates will be provided to you should you
choose to accept such challenges. Please start moving quickly to the next stop, instructions will be provided as you go along.
Good luck and may the odds be ever in your favour!""")
name = input(
    "If you dare to proceed, please tell us your name: ").strip().title()
print(f"Welcome {name}, we are glad to have you on board!")

allowed_names = ["george", "william", "chris", "bre", "riley"]
if name.lower() in allowed_names:
    print(f"Welcome {name}, please let's get started as time is ticking ")
else:
    print("Be wise and exit the game. Only authorized rescuers may proceed.")
    sys.exit()
