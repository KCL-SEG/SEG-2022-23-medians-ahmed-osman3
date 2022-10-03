"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
if(len(numbers) % 2 == 0):
    print((int(numbers[len(numbers/2)]) + int(len(numbers/2 + 1)))/2)
else:
    print(numbers[int(len(numbers)/2)])





#if numbers length = 0dd, case : 1,2,3,4,5 return len[]/2
#if numbers length = even, case : 1,2,3,4,5,6 return len[5]%2 + len[]/2+1
