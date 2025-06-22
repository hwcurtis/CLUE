print("Good luck, and may the odds be ever in your favor!")

name = input("If you dare to proceed, please tell us your name: ").strip()

allowed_names = ["george", "william", "chris", "bre", "riley"]

if name.lower() in allowed_names:
    print(
        f"Welcome, {name.capitalize()}. Let's get started — time is ticking!")
else:
    print("Be wise and wait right there. You will be escorted to the exit.")
