def main():
    six_eleven()


# 6-7. People: 
# Start with the program you wrote for Exercise 6-1 (page 99). 
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
# Loop through your list of people. As you loop through the list, print everything you know about each person.

def six_seven():
    
    people = {
        'wife': {
            'first_name': 'Ana Rita', 
            'last_name': 'Robalo',
            'age': 29,
            'city': 'Lisbon',
        },
        'co-worker': {
            'first_name': 'Ricardo',
            'last_name': 'Ramos',
            'age': 42,
            'city': 'Benfica',
        },
        'friend': {
            'first_name': 'Alexandre',
            'last_name': 'Carvalho',
            'age': 32,
            'city': 'High Seas',
        },
    }

    for person, info in people.items():
        # form the full name of the person
        full_name = f"{info['first_name']} {info['last_name']}"
        print(f"My {person}'s name is {full_name}, they live in {info['city']} and are {info['age']} years old.") 



# 6-8. Pets: 
# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, print everything you know about each pet.

def six_eight():
    pets = [
        {
            'type': 'dog',
            'name': 'kyla',
            'owner': 'k',
        },
        {
            'type': 'cat',
            'name': 'meggy',
            'owner':'mariana',
        },
        {
            'type': 'dragon',
            'name': 'saphire',
            'owner': 'eragon',
        }
    ]
    for pet in pets:
        print(f"{pet['owner'].title()} is the owner of a {pet['type']} called {pet['name'].title()}")


# 6-9. Favorite Places: 
# Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
# Loop through the dictionary, and print each person’s name and their favorite places.

def six_nine():
    favourite_places = {
        'ana': ['Adraga', 'Ikea'],
        'k': ['cinema'],
        'zelda': ['parque', 'casota']
    }

    for person in favourite_places:
        print(f"{person} loves the following places:")
        for i in favourite_places.get(person):
            print(f"\t{i}")



# 6-10. Favorite Numbers: 
# Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

def six_ten():
    favourite_numbers = {
        'anon': [14, 88],
        'Davidson': [1619, 2009],
        'Clara': [1776, 0],
        'Bro': [420],
        'Kevin': [69, 1, 3],
    }

    for i in favourite_numbers:
        print(f"{i.title()}'s favourite number are: ")
        for n in favourite_numbers.get(i):
            print(f"\t{n}")


# 6-11. Cities: 
# Make a dictionary called cities.
# Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, 
# its approximate population, and one fact about that city. 
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.

def six_eleven():
    cities = {
        'lisboa': {
            'country': 'portugal',
            'population': '500',
            'fact': 'no homes',
        },
        'brussels': {
            'country': 'belgium',
            'population': '7',
            'fact': 'chocolate',
        },
        'new york': {
            'country': 'usa',
            'population': '9999',
            'fact': 'dirty',
        },
    }

    for city, city_info in cities.items():
        print(f"The city of {city.title()} is in {city_info['country']}, has about {city_info['population']} peeps in it loves{city_info['fact']}")


# 6-12. Extensions: 
# We’re now working with examples that are complex enough that they can be extended in any number of ways. 
# Use one of the example programs from this chapter, and extend it by adding new keys and values, 
# changing the context of the program or improving the formatting of the output.

def six_twelve():
    pass

main()