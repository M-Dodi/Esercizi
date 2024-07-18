# Marin Dodi

print("Hello World")


#  2.5 Personal massage: use a variable to rapresent a persons name
# then write a massage to that person


#This variable contains the name
name: str = "Mario"

#This variable contains the massage
massage: str = f"Ciao {name}, ti va di imparare un pò di python insieme?"

print(massage)



#Namer case
#Questa è la variabile di una persona
#name: str = "Mario"


#Altro modo
name_lower = name.lower()
name_upper = name.upper()

print(f"{name}, {name_upper}, {name_lower}")

#print(f"{name}, {name.upper()}, {name.lower()}")


# 2.5 Find a famouse quote, print it with the name of the author
#author

name: str = "George Orwell"

message: str = "War is peace, freedom is slavery", name # type: ignore

print(message)


#  2.6 represent the famous person’s name using a variable called famous_person. 
#Then compose your message and represent it with a new variable called message. Print your message. 

famous_person = "Albert Einstein"

message = f"Happy Birthday to the legendary {famous_person}! Your contributions to science continue to inspire us all."

print(message)

#  2.8  Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.


filename = "python_notes.txt"

print(filename.removesuffix('.txt')) 



#3-1. Names: Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time

names = ["Bob", "Jonny", "Mario"]

print(names[0])
print(names[1])
print(names[2])

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
#printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.


print(f"Hi", names[0].title(), "!")
print(f"Hello", names[1], str("..."))
print(f"Grettings", names[2], "," "How are you today?")
    

#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list 
#that stores several examples. Use your list to print a series of statements about these items, 
#such as “I would like to own a Honda motorcycle.”

my_list = ["Harley", "Honda", "Suzuki"]

print("La", my_list[0], "è un sogno!")
print("Tra", my_list[1], "e", my_list[2], "è meglio", "l'", my_list[1], "!")


#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

stupid_guests = ["Maria Defilippi", "Malgioglio", "Mario"]

print(stupid_guests[0], ",", stupid_guests[1], ",", stupid_guests[2], ", please come to dinner!!!" )


#3-5. Changing Guest List: You just heard that one of your guests can’t
# make the dinner, so you need to send out a new set of invitations. 
#You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.

print("\nSorry", stupid_guests[0], "can't come to dinner")
del stupid_guests[0]
stupid_guests.insert(0, 'Maurizio Costanzo')

print("\n", stupid_guests[0], ", Please come to dinner")
print("\n", stupid_guests[1], ", Please come to dinner")
print("\n", stupid_guests[2], ", Please come to dinner")

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.

print("\n We found a bigger table")
stupid_guests.insert(0, "amadeus")
stupid_guests.insert(2, "madonna")
stupid_guests.append("Mango")

print("\n", stupid_guests[0].title(), ", Pease come to dinner")
print("\n", stupid_guests[2].title(), ", Please come to dinner")
print("\n", stupid_guests[5], ", Please come to dinner")
print(stupid_guests)

# 3.7 You just found out that your new dinner table won’t arrive in time for 
#the dinner, and you have space for only two guests.
#Start with your program from Exercise 3-6. Add a new line that prints a message 
#saying that you can invite only two people for dinner.
#Use pop() to remove guests from your list one at a time until only two names
# remain in your list. Each time you pop a name from your list, print a message
# to that person letting them know you’re sorry you can’t invite them to dinner.
#Print a message to each of the two people still on your list, letting them 
#know they’re still invited.   Use del to remove the last two names from your list,
# so you have an empty list. Print your list to make sure you actually have an empty
# list at the end of your program.


print("\nSorry, we can only invite two people to dinner.")


print("Sorry," + stupid_guests[2].title() + ", there is no room at the table")
print("Sorry," + stupid_guests[3] + ", there is no room at the table")
print("Sorry," + stupid_guests[4] + ", there is no room at the table")
print("Sorry," + stupid_guests[5] + ", there is no room at the table")

stupid_guests.pop(2)
stupid_guests.pop(3)
stupid_guests.pop(2)
stupid_guests.pop(2)
print(stupid_guests)

del stupid_guests[0]
del stupid_guests[0]
print(stupid_guests)


#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.


locations = ['philippine', 'himalaya', 'mexico', 'labrador', 'mauritius']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print(f"\nOriginal order:",locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical:")
locations.sort()
print(locations)

print("\nReverse alphabetical:")
locations.sort(reverse=True)
print(locations)


#3-9. Dinner Guests: Working with one of the programs from Exercises 3,
#use len() to print a message indicating the number of people you’re inviting
# to dinner.

guest_list = ["Maria Defilippi", "Malgioglio", "Mario"]
print(len(guest_list))




##3-10. Every Function: Think of something you could store in a list . For example, you could make a 
# list of mountains, rivers, countries, cities, languages, or anything else you’d like .
#Write a program that creates a list containing these items and then uses each function introduced 
# in this chapter at least once .

x=["cat",2.5,500,True]
print(x)
x[1]="dog" # changing first element of x from 2.5 to dog
print(x)

bike=["honda","yamaha","suzuki"]
del bike[1] #deleting the value at index 1 from x
print(bike)

x=["cat",2.5,500,True]
x.insert(1,"dog")#its insert the element in given position
print(x)

x.append(False)#it will append the element at last
print(x)

y=x.pop(2)#it will pop that element out at given index and remove from that 
#list If no index is specified , list.pop() removes the last item in the list
print(y+1)#you can also play with that pop out no
print("pop",x)

x.remove(False)#it will remove the given elment from the list
print(x)

list_one = [1, 2, 3, 4, 5, 6, 7]  # This is the first list
list_two = [10, 12, 14]           # This is the second list
list_one.extend(list_two)         # Extend list_one by appending all items of list_two
print(list_one)

my_list = [2, 3, 5, 7, 11, 13] # Create a list
my_list.clear()                # Remove all the items from the list
print(my_list) 

my_list = ["Python", "is", "awesome", "Java", "is", "Alright"]# Create a list
my_index = my_list.index("is")                                # Return the index of the first "is"
print("The item was first found at index:", my_index)

my_list = ["mew", "mew", "kitten", "mew", "mew"]                  # Create a list
my_count = my_list.count("mew")                                   # Return the number of times "mew" appears
print("The number of times the item appeared was:", my_count)

my_list = ["zero", "one", "two", "three", "four", "five"]        # Create a list
my_list.reverse()                                                # Reverse the items of the list in place
print("Reversed list looks like:", my_list)

my_list.sort(reverse=True)                             #it will sort list in descending order
print(my_list)

my_list.sort()                             #it will sort list in ascending order
print(my_list)

original_list = ["zero", "one", "two", "three"]        # Create a list
copied_list = original_list.copy()  #Copy the original and return
print("The copied list looks like:", copied_list)



#6-1. Person: Use a dictionary to store information about a person you know. 
#Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.

person = {'first_name': 'Andi', 'last_name': 'Dodi', 'age': '46','city': 'Brescia'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. 
#Think of a favorite number for each person, and store each as a value in your 
#dictionary. Print each person’s name and their favorite number. 
#For even more fun, poll a few friends and get some actual data for your program.




favorite_numbers = {'mandy': 42,'micah': 23,'gus': 7,'hank': 100000,'maggie': 3,}
    

num = favorite_numbers['mandy']
print("Mandy's favorite number is " + str(num) + ".")

num = favorite_numbers['micah']
print("Micah's favorite number is " + str(num) + ".")

num = favorite_numbers['gus']
print("Gus's favorite number is " + str(num) + ".")

num = favorite_numbers['hank']
print("Hank's favorite number is " + str(num) + ".")

num = favorite_numbers['maggie']
print("Maggie's favorite number is " + str(num) + ".")


#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
#However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. 
#You might print the word followed by a colon and then its meaning, 
#or print the word on one line and then print its meaning indented on a second line.
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.



glossary = {'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs."}

word = 'string'
print("\n" + word.title() + ": " + glossary[word])

word = 'comment'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'loop'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])



#6-7. People: Start with the program you wrote for Exercise 6-1. 
#Make two new dictionaries representing different people, and store all three 
#dictionaries in a list called people. Loop through your list of people. 
#As you loop through the list, print everything you know about each person

people = []

person = {'first_name': 'Andi', 'last_name': 'Dodi', 'age': '46','city': 'Brescia'}
people.append(person)
person = {'first_name': 'Einar','last_name': 'Dodi','age': 6,'city': 'Roma'}
people.append(person)


for person in people:
    name = person['first_name'] + person['last_name']
    age = str(person['age'])
    city = person['city']

    print(name + ", of " + city + ", is " + age + " years old.")


#6-8. Pets: Make several dictionaries, where each dictionary represents a 
#different pet. In each dictionary, include the kind of animal and 
#the owner’s name. Store these dictionaries in a list called pets. 
#Next, loop through your list and as you do, print everything you 
#know about each pet. 

pets = []

pet = {'animal type': 'chicken','name': 'clarence','owner': 'tiffany','weight': 2,'eats': 'seeds',}
pets.append(pet)

pet = {'animal type': 'dog','name': 'peso','owner': 'eric','weight': 37,'eats': 'shoes',}
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'] + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))


#6-9. Favorite Places: Make a dictionary called favorite_places. 
#Think of three names to use as keys in the dictionary, and store one 
#to three favorite places for each person. To make this exercise a bit 
#more interesting, ask some friends to name a few of their favorite places. 
#Loop through the dictionary, and print each person’s name and their 
#favorite places.        


favorite_places = {'Marco': ['bear mountain', 'death valley', 'alaska'],
'Julia': ['hawaii', 'iceland'],
'Hulio': ['baiahibe', 'the playground', 'south carolina']}


for name, places in favorite_places.items():
    print("\n" + name + " likes the following places:")
    for place in places:
        print("- " + place.title())


#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person
# can have more than one favorite number. Then print each person’s 
#name along with their favorite numbers.        



favorite_numbers = {'mandy': [42, 17],'micah': [42, 39, 56],'gus': [7, 12],}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))


#6-11. Cities: Make a dictionary called cities. Use the names of three cities 
#as keys in your dictionary. Create a dictionary of information about each 
#city and include the country that the city is in, its approximate population,
# and one fact about that city. The keys for each city’s dictionary 
#should be something like country, population, and fact. Print the name 
#of each city and all of the information you have stored about it.

cities = {'santiago': {'country': 'chile','population': 6158080,
'nearby mountains': 'andes'},
'kathmandu': {'country': 'nepal','population': 1003285, 
              'nearby mountains': 'himilaya',}}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + mountains + " mountains are nearby.")


#6-12. Extensions: We’re now working with examples that are complex 
#enough that they can be extended in any number of ways. Use one of the 
#example programs from this chapter, and extend it by adding new keys 
#and values, changing the context of the program, or improving the 
#formatting of the output.



fav_numbers = {'luke': [2,4],'william': [13,87],'allie': [11,91],'sookie': [0,100],
	'elsa': [1,11],}

for name, numbers in fav_numbers.items():
	print(name.title() + ", your favorite numbers are: ")
	for num in numbers:
		print("\t" + str(num))
