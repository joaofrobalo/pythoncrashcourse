# 6-4. Glossary 2: 
# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 
# by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. 
# When you’re sure that your loop works, add five more Python terms to your glossary. 
# When you run your program again, these new words and meanings should automatically be included in the output.

# 6-5. Rivers: 
# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

# 6-6. Polling: 
# Use the code in favorite_languages.py
# Make a list of people who should take the favorite languages poll. I
# nclude some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. 
# If they have already taken the poll, print a message thanking them for responding. 
# If they have not yet taken the poll, print a message inviting them to take the poll.


def main():
    six_six()


def six_four():
    python_help = {
        'String': 'a contiguous line of chars',
        'Dictionary': 'a set of key-value pairs',
        'Tuple': 'an immutable list',
        'Variable': 'a place in the memory, connected to a value',
        'Set': 'a list of unique items',
    }

    for term, description in python_help.items():
        print(f"A {term} is {description}")

def six_five():

    rivers = {
        'tejo': ['portugal', 'spain'], 
        'mississipi': 'usa', 
        'nile': 'egypt'
    }
    
    for river, country in rivers.items():
        print(f"The {river.title()} runs through {country.title()}" if type(country) is str else f"The {river.title()} runs through {country[0].title()} and {country[1].title()}")

def six_six():
    favourite_languages = {
        'Ana': 'Wordpress',
        'Rita': 'Potato',
        'João': 'Kotlin',
        'Robalo': 'Python',
    }

    people = ['Ana', 'Rita', 'João', 'Robalo', 'Tiago', 'André']

    for name in people:
        if name in favourite_languages.keys():
            print(f"Thank you for responding to the poll, {name}!")
        else:
            print(f"Please take the poll, {name}!")


main()