# 6-1. Person: 
# Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.

# 6-2. Favorite Numbers: 
# Use a dictionary to store people’s favorite numbers. 
# Think of five names, and use them as keys in your dictionary. 
# Think of a favorite number for each person, and store each as a value in your dictionary. 
# Print each person’s name and their favorite number. 
# For even more fun, poll a few friends and get some actual data for your program.

# 6-3. Glossary: 
# A Python dictionary can be used to model an actual dictionary. 
# However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. 
# You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.




def main():
    six_three()

def six_one():
    myperson = {
        'first_name': 'Ana Rita', 
        'last_name': 'Robalo',
        'age': 29,
        'city': 'Lisbon',
    }

    for i in myperson:
        print(myperson[i])

def six_two():
    favourite_numbers = {
        'anon': 1488,
        'Davidson': 1619,
        'Clara': 1776,
        'Bro': 420,
        'Kevin': 69, 
    }

    for i in favourite_numbers:
        print(f"{i.title()}'s favourite number is {favourite_numbers[i]}")

def six_three():
    python_help = {
        'String': 'a contiguous line of chars',
        'Dictionary': 'a set of key-value pairs',
        'Tuple': 'an immutable list',
        'Variable': 'a place in the memory, connected to a value'
    }

    for i in python_help:
        print(f"A {i} is:\n{python_help[i]}")


main()