# Write a function is_even that will return true if the passed-in number is even.

is_even = lambda num: True if num % 2 == 0 else False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

is_even = lambda num: "Even" if num % 2 == 0 else "Odd"

print(is_even(num))
