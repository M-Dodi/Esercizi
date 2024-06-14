class Persona:
    def __init__(self,first_name, last_name) -> None:
       
       if isinstance(first_name, str) and isinstance(last_name, str):
       
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age = 0

       else:
         self .first_name = None
         self.last_name = None
         self.age = None
         print("Errore: Il nome o il cognome inserito non è una stringa!")


    def setName(self, first_name):
       if isinstance(first_name, str):
          self.first_name = first_name

       else:  
          print("Errore: Il nome inserito non è una stringa")


    def setLastName(self, last_name):
       if isinstance(last_name, str):
          self.last_name = last_name

       else:
          print("Errore: Il cognome inserito non è una stringa")


    def setAge(self, age):
       if isinstance(age, int):
          self.age = age

       else:
          print("Errore: L'età deve essere un numero")


    def getName(self):
       return self.first_name
    
    def getLastName(self):
       return self.last_name
    
    def getAge(self):
       return self.age
    
    def greet(self):
       print(f"Ciao, sono {self.first_name} {self.last_name}! 
             Ho {self.age} anni!")

       
            


