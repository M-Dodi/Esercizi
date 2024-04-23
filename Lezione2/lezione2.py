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
