import sys

script, number_string = sys.argv

number = int(number_string)

numbers = []

def loop(number):
    for i in range(number):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

print("The numbers: ")

loop(number)
