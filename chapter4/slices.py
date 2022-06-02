# 4-10. Slices: Using one of the programs you wrote in this chapter, 
# add several lines to the end of the program that do the following:
deathnote = ["Potato", "Dark matter", "Bebbanburg", "Solipsis", "What's the matter with you?"]
# Print "The first three items in the list are:"
#  Then use a slice to print the first three items from that program’s list.
print("The first three items in the list are:", deathnote[:3])

# Print "Three items from the middle of the list are:"
# Use a slice to print three items from the middle of the list.
print("Three items from the middle of the list are:", deathnote[1:4])

# Print "The last three items in the list are:" 
# Use a slice to print the last three items in the list.
print("The last three items in the list are:", deathnote[-3:])

# 4-11. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
othernote = deathnote[:]
# Add a new pizza to the original list.
deathnote.append("ketchup")
# Add a different pizza to the list friend_pizzas.
othernote.append("mayo")
# Prove that you have two separate lists. 
print(deathnote, othernote)
# Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
print("\nMy favourite deaths are:", end=" ")
for notes in deathnote:
    print(notes, end=", ")
# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list.
print("\nBut also:", end=" ")
for notas in othernote:
    print(notas, end=", ")

# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. 
# Choose a version of foods.py, and write two for loops to print each list of foods.
# nah