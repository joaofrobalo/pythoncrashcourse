# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
places = ["Bed", "Bathroom", "Refrigerator", "Toilet", "Sofa"]
# Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
print(places)
# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(places))
# Show that your list is still in its original order by printing it.
print(places)
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(places, reverse=True))
# Show that your list is still in its original order by printing it again.
print(places)
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print(places)
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places.reverse()
print(places)
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places.sort()
print(places)
# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
places.sort(reverse=True)
print(places)


# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 42), 
# use len() to print a message indicating the number of people you are inviting to dinner.

print(f"I'm visiting {len(places)} amount of places")

# 3-10. Every Function: Think of something you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.


