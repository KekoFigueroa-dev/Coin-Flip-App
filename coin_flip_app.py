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

print(flip_number)
print(choice)

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

# --- Calculate and Print Flip Statistics ---
# After the loop, calculate the percentage of heads and tails (rounded to two decimal places)
# Print a summary showing:
#   - Total heads and tails
#   - Percentage results
