# Define a function to generate the Fibonacci sequence
def fibonacci(n):
    # Initialize the first two terms
    a = 0
    b = 1
    # Create an empty list to store the sequence
    sequence = []
    # Loop until the nth term
    for i in range(n):
        # Append the current term to the list
        sequence.append(a)
        # Update the next two terms by adding them
        a, b = b, a + b
    # Return the list of the sequence
    return sequence

# Ask the user how many terms they want to generate
n = int(input("How many terms do you want to generate? "))

# Call the fibonacci function with the user input
sequence = fibonacci(n)

# Print the sequence
print(f"The Fibonacci sequence of {n} terms is: {sequence}")
