# Convert formatted string to list
fruits = eval(input())
# Catch the exception and make sure the code runs without crashing.


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
