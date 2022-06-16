# 7-1. Rental Car: 
# Write a program that asks the user what kind of rental car they would like. 
# Print a message about that car, such as “Let me see if I can find you a Subaru.”

# 7-2. Restaurant Seating: 
# Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying they’ll have to wait for a table.
#  Otherwise, report that their table is ready.

# 7-3. Multiples of Ten:
# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

def main():
    seven_three()

def seven_one():
    car = input("What kind of rental car would you like? ")
    print(f"Let me see if I can find you a {car.title()}.")

def seven_two():
    n = input("How many people are in your dinner group? ")
    if int(n) > 8:
        print("You'll have to wait for a table.")
    else:
        print("Your table is ready, right this way.")

def seven_three():
    n = input("Number: ")
    if int(n) % 10:
        print(f"{n} is not a multiple of 10.")
    else:
        print(f"{n} is a multiple of 10.")

main()