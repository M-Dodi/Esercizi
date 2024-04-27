# Marin Dodi

print("Hello World")


#  2.5 Personal massage: use a variable to rapresent a persons name
# then write a massage to that person


#This variable contains the name
name: str = "Mario"

#This variable contains the massage
massage: str = f"Ciao {name}, ti va di imparare un pò di python insieme?"

print(massage)



#Name case
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

massage: str = f"War is peace, freedom is slavery", {name}

print(massage)



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