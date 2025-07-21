# Coin-Flip-App

import random

# --- Introduction and User Input Section ---
print("Welcome to my Coin Toss App")
print("\\nI will flip a coin a set number of times.")

# Get the number of flips from the user
while True:
    try:
        flip_number = int(input("How many times would you like me to flip the coin: "))
        if flip_number > 0:
            print("Thank you!")
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid whole number")

# Ask the user if they want to see the result of each individual flip
while True:
        try:
            choice = input("Would you like to see the result of each flip (y/n): ").lower()
            if choice == ("y") or choice == ("n"):
                break
            else:
                print("Please enter y or n!")
        except Exception as e:
            print(f"An error occurred!: {e}")

# --- Initialized Counters for Heads and Tails ---
heads_count = 0
tails_count = 0

# --- Flip the Coin the Requested Number of Times ---
# Loop through the number of flips and simulate the coin toss
# For each flip:
#   - Generate a random number: 0 for tails, 1 for heads
#   - Update the appropriate counter (heads or tails)
#   - If the user wants, display the result of this flip
#   - Check if heads and tails counts are equal and print a message if so

for flips in range(flip_number):
    coin = random.randint(0,1)

    if coin == 1:
        heads_count += 1
        if choice.startswith('y'):
            print("HEADS")
    else:
        tails_count += 1
        if choice.startswith('y'):
            print("TAILS")
    
if heads_count == tails_count:
    print(f"At {flips + 1} flips, the number of heads and tails were equal at {str(heads_count)}, each.")

# --- Calculate and Print Flip Statistics ---
# After the loop, calculate the percentage of heads and tails (rounded to two decimal places)
heads_percentage = round(100 * heads_count / flip_number, 2)
tails_percentage = round(100 * tails_count / flip_number, 2)
# Print a summary
print(f"\nResults of Flipping a Coin {flip_number} Times: ")
print(f"\nSide\t\tCount\tPercentage: ")
print(f'Heads\t\t{str(heads_count)}/{str(flip_number)}\t\t{str(heads_percentage)}%')
print(f'Tails\t\t{str(tails_count)}/{str(flip_number)}\t\t{str(tails_percentage)}%\n')


