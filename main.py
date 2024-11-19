import itertools

# Sample cryptarithmetic problem: BASE + BALL = GAME
input_string = "SEND MORE MONEY"
x, y, z = input_string.split()

# Get unique letters
unique_letters = set(x + y + z)

# Ensure no leading zeros
starting_letters = {x[0], y[0], z[0]}

# Define the function to convert words to numbers based on the letter-to-digit mapping
def word_to_number(word, letter_to_digit):
    return sum(letter_to_digit[letter] * (10 ** i) for i, letter in enumerate(reversed(word)))

# Generate permutations for the unique letters
possible_permutations = itertools.permutations(range(10), len(unique_letters))

# Iterate through permutations and check if the equation holds
for perm in possible_permutations:
    # Map letters to digits
    letter_to_digit = dict(zip(unique_letters, perm))
    
    # Prune if the first letter of any word is zero
    if letter_to_digit[x[0]] == 0 or letter_to_digit[y[0]] == 0 or letter_to_digit[z[0]] == 0:
        continue
    
    # Convert words to numbers
    num_x = word_to_number(x, letter_to_digit)
    num_y = word_to_number(y, letter_to_digit)
    num_z = word_to_number(z, letter_to_digit)
    
    # Check if the equation holds
    if num_x + num_y == num_z:
        print(f"Solution found: {x} + {y} = {z}")
        print(f"Mapping: {letter_to_digit}")
        break
