from add import add_fruit
from divide import divide_fruit
from multiply import multiply_fruit

apples = int(input("how many apples?"))
oranges = int(input("how many oranges?"))

# function call for adding apples and oranges
add = add_fruit(apples, oranges)
print(add)
# function for dividing apples and oranges
divide = divide_fruit(apples, oranges)
print(divide)
# function for multiplying apples and oranges
multiply = multiply_fruit(apples, oranges)
print(multiply)


