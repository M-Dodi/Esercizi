from typing import Tuple


class Persona:

    def __init__(self,name: str, cognome: str, data_di_nascita: str, genere: str) -> None:

        self.nome: str = name
        self.cognome: str = cognome
        self.data_di_nascita: str = data_di_nascita
        self.genere: str = genere
    
    def calcola_eta(self) ->int:
        return 10

persona_1: Persona = Persona(name="Flavio", cognome="Giorgi",
                             data_di_nascita="24/12/94",
                             genere="Maschio")


class Dipendente(Persona):
    def __init__(self, name: str, cognome: str, data_di_nascita: str, genere: str,ore_lavorate: int) -> None:
        
        super().__init__(name, cognome, data_di_nascita, genere)
        self.ore_lavorate: int = ore_lavorate
    
    def calcola_stipendio(self)->float:
        
        return 500


dipendente_1: Dipendente = Dipendente(name="Flavio", cognome="Giorgi",
                                data_di_nascita="24/12/94",
                                genere="Maschio"ore_lavorate=500)


class Professore(Dipendente):
    def __init__(self, name: str, cognome: str, data_di_nascita: str, genere: str, ore_lavorate: int) -> None:
        
        super().__init__(name, cognome, data_di_nascita, genere, ore_lavorate)

        self.materia_insegnata: str = materia_insegnata
        self.ore_di_lezione: str = ore_di_lezione

    def __str__(self)->


print(persona_1.calcola_eta())



print(dipendente_1.nome)
print(dipendente_1.calcola_eta())
print(dipendente_1.calcola_stipendio())

professore_1: Professore = Professore(name="Flavio", cognome="Giorgi",
                             data_di_nascita="24/12/94",
                             genere="Maschio"ore_lavorate=500,materia_insegnata="python"
                             ore_di_lezione=1000)




class Animal:

    def __init__(self, species: str, age: int):

       self.specie: str = species
       self.age: int = age

    def speak(self):
        pass



class Person(Animal):

    def __init__(self, name: str, surname: str,age: int, cf: str ):
        super().__init__(name, "Homo Sapiens", age)
        
        self.name: str = name
        self.surname: str = surname
        self.age: int = age
        self.cf: str = cf

    def speak(self) -> str:
        return f'Ciao mi chiamo {self.name} ed ho {self.age}.'




    def __str__(self) -> str:
        return f'{self.name.capitalize()} {self.surname.capitalize()}(cf={self.cf})'\
            +f', age={self.age}'\
            +f', cf={self.cf}'





class Student(Person):

    def __init__(self, name: str, age: int, cf: str):
        super().__init__(name, age, cf)


class Cat(Animal):
    def __init__(self,specie, name: str, age: int):
        super().__init__("Felidae", age)

        self.name = name

    def __str__(self) -> str:
        return f'Cat(name={self.name})'



