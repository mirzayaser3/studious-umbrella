# Simple Pyramid Program
def simple_pyramid(height):
    for i in range(1, height + 1):
        print("*" * i)

# Get the height of the pyramid from the user
try:
    height = int(input("Enter the height of the pyramid: "))
    simple_pyramid(height)
except ValueError:
    print("Please enter a valid integer.")

