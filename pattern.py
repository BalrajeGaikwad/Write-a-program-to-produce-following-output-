#Write a program to produce following output 
"""

A B C D E F G F E D C B A
A B C D E F   F E D C B A
A B C D E       E D C B A
A B C D           D C B A
A B C               C B A 
A B                   B A 
A                       A 

""" 
n=7

for i in range(n):
    for j in range(n-i):
        print(chr(65+j), end="  ")
    print("    "*i, end=" ")


    for i in range(n-i-1,-1,-1):
        print(chr(65+j), end="  ")
    
    print()

n = 7  # Number of rows

"""# Loop through rows
for i in range(n):
    # Print the left part (A, B, C, ...)
    for j in range(n - i):
        print(chr(65 + j), end="  ")  # Convert number to character (A=65)
    
    # Print the spaces in the middle
    print("    " * i, end="")
    
    # Print the right part (..., C, B, A)
    for j in range(n - i - 1, -1, -1):
        print(chr(65 + j), end="  ")

    # Move to the next row
    print()"""
