#Fibonacci sequence
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)
    return fib_sequence

# Test the function
num = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence up to {num} terms:")
print(generate_fibonacci(num))