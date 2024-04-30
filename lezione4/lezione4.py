# use a function usin substract with two numbers as arguments

def substract(x:float,y:float) -> float:
    
    print(f"x={x}, y={y}")
    return x - y

x = 3
y = 5
out = substract(x,y)

print(f'La diff è {out}')


#write a function check_value() witch takes a number as argument
#using if/else should print wether the number is bigger smaller or equal to 5



def check_value(number: int):
    if number > 5:
        print(f"{number} è più grande di 5")
    elif number < 5:
        print(f"{number} è più piccolo di 5")
    else:
        print(f"{number} è uguale a 5")        

check_value(4)
check_value(7)
check_value(5)

#write a function print_numbers(), which takes a list of numbers
#as argument using a for loop, print each number one by one

def print_numbers(numbers_list):
    for number in numbers_list:
        print(number)

print_numbers([1,2,3,4,5])


#Write a function check_each(), which takes a list of numbers as argument.
#Using a for loop, iterate through the list.
#For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5,
#and “equal” if it’s equal to 5

def check_each(numbers_list):
    for number in numbers_list:
        if number > 5:
            print("Bigger")
        elif number < 5:
            print("Smaller")    
        else:
            print("Equal") 

check_each([3, 6, 5])       



#School Grading System:
#Create a function that takes a student's name and their scores in different 
#subjects as input.
#The function calculates the average score and prints the student's name, 
#average, and a message indicating whether the student passed the exam (
#average >= 60) or failed.
#Create a for loop to iterate over a list of students and scores, 
#calling the function for each student.

def calculate_average(scores):
    if not scores:
        return 0.0
    
    return sum(scores) / len(scores)

def calculate_grade(score):
    if score >= 90: 
        return 'A' 
    elif score >= 80: 
        return 'B' 
    elif score >= 70: 
        return 'C' 
    elif score >= 60: 
        return 'D' 
    else: 
        return 'F' 
    
student_data = {'Alice': [85, 90, 92],'Bob': [78, 80, 82],'Charlie': [95, 87, 88]}

for student, scores in student_data.items(): 
    average_score = calculate_average(scores)
    grade = calculate_grade(average_score)

print(f"Student: {student}")

print(f"Average Score: {average_score}")

print(f"Grade: {grade}\n")


#2. Guess the Number Game:
#Create a function that generates a random number within a range specified by the user.
#Prompt the user to guess the number within a specified maximum number of attempts.
#Provide feedback to the user after each guess, indicating whether their guess is too 
#high, too low, or correct.
#Terminate the loop when the user guesses the number correctly or reaches the 
#maximum number of attempts.

import random
number = random.randint(1,20)

print("Hello, your name is?")


my_name = input()
guess_taken = 0

print("Well," + my_name + ",I'm thinking of a number from 1 to 20")
while guess_taken < 4:
    print("Take a guess...")
    guess = input()
    guess = int(guess)
    guess_taken += 1

    if guess < number:
        print("Your guess is to low")
    if guess > number:
        print("your guess is to high")
    if guess == number:
        break

if guess == number:
   guess_taken = str(guess_taken)
   print("goodjob," + my_name + ", You said it right!") 

if guess != number:
    number = str(number)
    print("Nope, the number I was thinking was " + number)
    

#3. E-commerce Shopping Cart:
#Create a function that defines a product with a name, price, and quantity.
#Create a function that manages the shopping cart, allowing the user to add, remove, 
#and view products in the cart.
#The function should calculate the cart total and apply any discounts or taxes.
#Implement a for loop to iterate over the items in the cart and print detailed information
# about each product and the total.

# Define a class called ShoppingCart to represent a shopping cart
class ShoppingCart:
    # Initialize the shopping cart with an empty list of items
    def __init__(self):
        self.items = []

    # Add an item with a name and quantity to the shopping cart
    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    # Remove an item with a specific name from the shopping cart
    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    # Calculate and return the total quantity of items in the shopping cart
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
    
    # Example usage
# Create an instance of the ShoppingCart class
cart = ShoppingCart()

# Add items to the shopping cart
cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)

# Display the current items in the cart and calculate the total quantity
print("Current Items in Cart:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)

# Remove an item from the cart, display the updated items, and recalculate the total quantity
cart.remove_item("Orange")
print("\nUpdated Items in Cart after removing Orange:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)


#4. Text Analysis:
#Create a function that reads a text file and counts the number of occurrences of each word.
#The function should print a report showing the most frequent words and their number of occurrences.
#You can use a for loop to iterate over the words in the text and a dictionary 
#to store the occurrences.
#Implement error handling to handle missing files or other input issues.

"""# Open the file in read mode 
text = open("sample.txt", "r") 

# Create an empty dictionary 
d = dict() 

# Loop through each line of the file 
for line in text: 
	# Remove the leading spaces and newline character 
	line = line.strip() 

	# Convert the characters in line to 
	# lowercase to avoid case mismatch 
	line = line.lower() 

	# Split the line into words 
	words = line.split(" ") 
						

	# Iterate over each word in line 
	for word in words: 
		# Check if the word is already in dictionary 
		if word in d: 
			# Increment count of word by 1 
			d[word] += 1
		else: 
			# Add the word to dictionary with count 1 
			d[word] = 1

# Print the contents of dictionary 
for key in list(d.keys()): 
	print(key, ":", d[key]) """


#5. Inventory Management System:
#Create a function that defines an item with a code, name, quantity, and price.
#Create a database or dictionary to store the items in inventory.
#Implement functions to add, remove, search, and update items in the inventory.
#Use for loops and conditional statements to manage the various inventory operations.



def create_item(code, name, quantity, price):

 item = {'code': code,'name': name,'quantity': quantity,'price': price}
 return item

item1 = create_item(code="A1", name="Banana", quantity=10, price=0.99)
item2 = create_item(code="B2", name="Apple", quantity=5, price=1.49)
item3 = create_item(code="C3", name="Orange", quantity=40, price=1.90)


inventory_db = {}

def add_item_to_inventory(inventory, item):

 inventory[item['code']] = item
 return inventory


inventory_db = add_item_to_inventory(inventory_db, item1)
inventory_db = add_item_to_inventory(inventory_db, item2)
inventory_db = add_item_to_inventory(inventory_db, item3)

for code, item in inventory_db.items():
    print(f"Code: {code}, Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")

def remove_item_from_inventory(inventory, code):

 if code in inventory:
        del inventory[code]
 return inventory

def search_item_in_inventory(inventory, code):

 return inventory.get(code)

searched_item = search_item_in_inventory(inventory_db, "A1")
if searched_item:
    print(f"Found item: {searched_item['name']}")

def update_item_in_inventory(inventory, code, quantity=None, price=None):


 if code in inventory:
        if quantity is not None:
            inventory[code]['quantity'] = quantity
        if price is not None:
            inventory[code]['price'] = price
 return inventory

inventory_db = update_item_in_inventory(inventory_db, "A1", quantity=15)



for code, item in inventory_db.items():
    print(f"Code: {code}, Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")



#6. Password Generator:
#Create a function that generates a random password with a specified length and 
#desired character types (lowercase letters, uppercase letters, numbers, symbols).
#Allow the user to specify the password length and desired character types.
#Generate and return a random password that meets the user's criteria.

import random
import string

lowercase_chars = string.ascii_lowercase
uppercase_chars = string.ascii_uppercase
digit_chars = string.digits
symbol_chars = string.punctuation



def generate_random_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):

    all_chars = ""
    if use_lowercase:
      all_chars += lowercase_chars
    if use_uppercase:
     all_chars += uppercase_chars
    if use_digits:
        all_chars += digit_chars
    if use_symbols:
        all_chars += symbol_chars


    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

desired_length = 12
password = generate_random_password(desired_length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True)
print(f"Generated password: {password}")