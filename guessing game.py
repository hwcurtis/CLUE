import sys
import time

print('WELCOME TO THE RESCUE MISSION, should you choose to accept it!')
print("""These are the details we have at the moment, folks are in need of rescue on a remote island, we know
      very little information about the situation, other than we are working to find the coordinates  and will be provided to you should you
choose to accept such challenges. Please start moving quickly to the next stop, instructions will be provided as you go along.
""")


choice = input(
    "Do you want to run or hide? ").strip().lower()
if choice == 'run':
    print("You chose to run! You sprint towards the rescue point.")
elif choice == 'hide':
    print("You chose to hide! You find a safe spot and wait for the rescue team.")
else:
    print("Invalid choice! You must choose either 'run' or 'hide'.")
    sys.exit()


print("You have made your choice, now let's see what happens next.")
print("You are now at the rescue point, and see a few boats. Which one would you choose: the sailboat, the motorboat, or the kayak?")


# print('you dont want to exit, you have come to help, your options are to run or hide, what do you choose?')
# print("You have chosen to exit the game. Wise Choice  Goodbye!")
# sys.exit()
# if name.lower() == "exit":
#   print("You have chosen to exit the game. Wise Choice. Goodbye!")
#  sys.exit()
