# 3-1. Names: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.
names = ["Ana Rita", "Filipa", "Tiago", "David"]
for name in names:
    print(name)

# 3-2. Greetings: Start with the list you used in Exercise 3-1, 
# but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be personalized with the person’s name.
for name in names:
    print(f"How's it going {name}?")

# 3-3. Your Own List: Think of your favorite mode of transportation, 
# such as a motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, 
# such as “I would like to own a Honda motorcycle.”
cars = ["Renault Clio", "Volkswagen Golf", "BMW Series 3"]
print(f"My first car was a {cars[0]}, then I got my wife's {cars[1]}. Later I bought her father's {cars[2]} for 1€\n")


# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, 
# who would you invite? Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.
guests = ["Jesus", "Hitler", "Ghandi"]
for guest in guests:
    print(f"You, {guest}, are now cordially invinted to eat at my place. Please bring the food, though.")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Add a print() call at the end of your program 
# stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person 
# you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.
print("\nHitler can't make it, he found out Jesus was a jew")
guests[1] = "Zé"
for guest in guests:
    print(f"{guest}! You are invited to my dinner.")


# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
# Add a print() call to the end of your program informing people that you found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

print("\nThe carpenter made us a bigger table, we can now invite more guests!")
guests.insert(0, "Joan D'Arc")
guests.insert(2, "Ema")
guests.append("Zelda")
for guest in guests:
    print(f"{guest} is invited to dinner.")


# Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

print("\nSorry to everyone, Jesus got arrebatado and he never made the table. I can only invite two people now")
for i in range(len(guests)):
    if len(guests) == 2:
        print(f"{guests[0]} and {guests[1]}, you are still invited!")
        break
    print(f"I'm sorry {guests.pop()}, I don't like you enough to keep you invited.")

del guests[1], guests[0]
print(guests)
