# dato una stringa che contiene parole è spazi
#una parola è una sottostringa che contiene caratteri contigui diversi dallo spazio

def length_of_last_word(s: str) -> int:
    s = s.strip()           # Rimuoviamo gli spazi
    words = s.split()       #dividiamo la stringa in parole
    if words:           # se troviamo parole restituisci la lungezza del ultima parola
     return len(words[-1])    
    else:               # Ritorna 0 se stringa vuota   
       return 0
input_str = " hello world "   
print(f"Lungezza: {length_of_last_word(input_str)}")


# Dato un itero x , restituisce True se x è palindromo è False altrimenti

def is_palindrome(x):
    x_str = str(x)
    return x_str == x_str[::-1]


x = 12345
print(f"L'intero{x} è palindromo? {is_palindrome(x)}")



class Person:
   
   def __init__(self,name,age):
      self.name = name
      self.age = age

alice = Person("Alice", 45)
bob = Person("Bob", 36)

print(f" nome = {bob.name}")

if alice.age > bob.age:
   print(f"The odest is:{alice.name}")
elif bob.age > alice.age:
   print(f"The oldest is:{bob.name}")
else:
   print("They have the same age")
    

people = ["Alice", 45, "Bob", 36 "Marin", 40, "Martin", 38, "Andi", 32]
   
min_age = 



 #1- Write a class called Student with the attributes name(str) and study program(str) 
 #2- Create three instances, one for yourself, one for your left and right neighbour.
 #3- Add a method print info that prints the name and studyProgram of a Student. test
 #your method on the object
 #4- Modyfe the code  and add age and gender to atributes, modify the printing methods too

class Student:
   
   

   def __init__(self,name: str,studyProgram: str):
      self.name: str = name
      self.studyProgram: str = studyProgram
      self.age: int = None
      self.gender: str = None


   def __str__(self) -> str:
       return f'Person(name={self.name},studyProgram={self.studyProgram})'

   def set_age(self, new_age: int):
       self.age = new_age

   def set_gender(self, new_gender: str):
       self.gender = new_gender


me = Student("Marin", "History")
left = Student("Alessandro", "Informatics")
right = Student("Markian", "Biology")
   
print(left)   

left.set_age(22)
left.set_gender("M")

print(left)
"""
Exersise 3
Given a class Animal for each task test our changes 1) create two realistic instance of
Animals 2) print the name of each object 3) Change the amount of legs of one object
usin the dot notation 4) add a method setLegs() to set the legs of an object end repeat usin the 
method 5) Add a method getLegs( to return the amount of legs)
6) add a method amed printInfo() that print all atrributes of the Animal

"""

class Animal:

   def __init__(self,name: str, legs: int =0):
      self.name: str = name
      self.legs: int = self.get_legs(legs)


   def  set_legs(self, new_legs: int):
        if new_legs >= 0:
           self.legs = new_legs
        else:
           self.legs = 0  
      
   
   def get_legs(self) -> int:
        return self.legs



   def __str__(self) -> str:
        return f'{self.name.capitalize()}(legs{self.get_legs})

        
cane = Animal("cane", 4) 

print(cane)






class Student:

   all_grade: list[int] = []

   def __init__(self,name: str, grades: list[float] = [])
      self.name: str = name
      self.grade = grades
      self.all_grades += grades

   def bella(self):
      print (bella)

   @classmethod


   #9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
   #Restaurant should store two attributes: a restaurant_name and a cuisine_type.
   # Make a method called describe_restaurant() that prints these two pieces of 
   #information, and a method called open_restaurant() that prints a message 
   #indicating that the restaurant is open. Make an instance called restaurant f#
   .rom your class. Print the two attributes individually, and then call both methods
   


class Restaurant:

   def __init__(self,name: str, cuisine_type: str):
       self.name: str = name
       self.cuisine_type: str = cuisine_type
       self.set_number_served: int = self_number_served

       
   def describe_restaurant(self):
       print(f'Restaurant(name={self.name},' + f'cuisine={self.cuisine_type})')           

   def open_restaurant(self):
       print(f'Il restorante {self.name} è aperto')


   def set_number_served(self,new_number_served: int):
        self_number_served = new_number_served


      

