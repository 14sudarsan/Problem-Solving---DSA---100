# Create a dictionary with only one pair: ')' maps to '('
match = {')': '('}

# Extract the values from the dictionary
value = list(match.values())

# Repeat the value n times
n = 2
repeat = value * n  # repeat is ['(', '(']

# Loop through the repeat list and append ')' after each '('
i = 0
while i < len(repeat):
    if repeat[i] == '(':
        repeat.append(')')  # Append the corresponding closing parenthesis
    i += 1

# Convert the list to a string
final_string = ''.join(repeat)

# Print the final result
print(repeat)        # Output: ['(', '(', ')', ')']
print(final_string) # Output: (())
