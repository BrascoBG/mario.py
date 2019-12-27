from cs50 import get_int

# Prompt user for a positive number
while True:
    n = get_int("Height: ")
    if n > 0 and n <= 8:
        break

for i in range(n):
    print(" "*(n-i-1) + "#"*(i+1))

