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


def main():
    six_five()


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


main()