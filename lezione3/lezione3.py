#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store 
#these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, instead of printing 
#just the name of the pizza. For each pizza, you should have one line of output containing a 
#simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how 
#much you like pizza. The output should consist of three or more lines about the 
#kinds of pizza you like and then an additional sentence, such as I really love pizza!


favorite_pizzas = ['salame', 'boscaiola', 'margherita']


for pizza in favorite_pizzas:  # All pizzas
    print(pizza)
print("\n")  


for pizza in favorite_pizzas:  # Print a sentence about each pizza.
    print("I really love " + pizza + " pizza!")

print("\nI really love pizza!")


#4-2. Animals: Think of at least three different animals that have a common 
#characteristic. Store the names of these animals in a list, and then use a 
#for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as 
#A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have 
#in common. You could print a sentence, such as Any of these animals would 
#make a great pet!


animals = ["lion", "monkey", "goat"]

for animal in animals:  # Print each animal.
    print(animal)

print("\n")

for animal in animals:   # Print a statement about each animal.
    print(f"A {animal} has a long tail.")

print("\nAll of these animals are lovely.")


#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

numbers = list(range(1, 21))
for number in numbers:
    print(number)


#4-4. One Million: Make a list of the numbers from one to one million, 
#and then use a for loop to print the numbers. (If the output is taking too long,
# stop it by pressing CTRL-C or by closing the output window.)


one_million = list(range(1,1000001))
##print(one_million) ## commented out to save time


#4-5. Summing a Million: Make a list of the numbers from one to one million, 
#and then use min() and max() to make sure your list actually starts at one 
#and ends at one million. Also, use the sum() function to see how quickly 
#Python can add a million numbers.


numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))


#4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.


odd_numbers = list(range(1, 20, 2))

for number in odd_numbers:
    print(number)


#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a 
#for loop to print the numbers in your list.    


threes = list(range(3, 31, 3))

for number in threes:
    print(number)


#4-8. Cubes: A number raised to the third power is called a cube. 
#For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer 
#from 1 through 10), and use a for loop to print out the value of each cube.


cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)


#4-9. Cube Comprehension: Use a list comprehension to generate a list of 
#the first 10 cubes.

cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)


#4-10. Slices: Using one of the programs you wrote in this chapter, add several 
#lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice 
#to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. T
#hen use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. 
#Then use a slice to print the last three items in the list.    


print(cubes[:3])  # The first three items in the list

print(cubes[2:5])  # Three items from the middle of the list

print(cubes[-3:])  # Last three items in the list


#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1.
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite pizzas are:, 
#and then use a for loop to print the first list. Print the message 
#My friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.


favorite_pizzas = ['salame', 'boscaiola', 'margherita']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('vegetariana')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")


#4-12. More Loops: All versions of foods.py in this section have avoided 
#using for loops when printing, to save space. Choose a version of foods.py,
# and write two for loops to print each list of foods.   


my_foods = ['pizza', 'pasta', 'fagioli']
friend_foods = my_foods[:]

my_foods.append('tiramisù')
friend_foods.append('gelato')

print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")


#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#• Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.   


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

car = 'ford'
print("Is car == 'ford'. I predict True.")
print(car == 'ford')

print("\nIs car == 'audi'. I predict False")
print(car == 'audi') 

car = 'suzuki'
print("Is car == 'suzuki'? I predict True")
print(car == 'suzuki')

print("\nIs car == 'ford'? I predict False.")
print(car == 'ford')


#5-2. More Conditional Tests: You don’t have to limit the number of tests you 
#create to 10. If you want to try more comparisons, write more tests and add them
#to conditional_tests.py. Have at least one True and one False result for each of
#the following:
#• Tests for equality and inequality with strings
#• Tests using the lower() method
#• Numerical tests involving equality and inequality, greater than and less
#than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a lis


my_car = 'dodge'
fav_car = input(print("What's your favorite car brand?"))
if fav_car.lower() == my_car:
	print("Your favorite car is what I drive!")
else:
	print("Your favorite car is a " + fav_car + ".")

age = int(input(print("What's your age?")))
if age < 18:
	print("Sorry, you can't buy tobacco products.")
else:
	print("You are allowed to buy tobacco products.")
     





