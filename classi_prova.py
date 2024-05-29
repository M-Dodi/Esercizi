from typing import Tuple

a: tuple = (1, 2)

class Persona:
    
    def __init__(self, 
                 name: str, 
                 cognome: str, 
                 data_di_nascita: str,
                 genere: str) -> None:
        
        self.nome: str = name
        self.cognome: str = cognome
        self.data_di_nascita: str = data_di_nascita
        self.genere: str = genere
        
    def calcola_eta(self)->int:
        
        return 10
    
    
    
persona_1: Persona = Persona(name="Flavio", 
                             cognome="Giorgi", 
                             data_di_nascita="24/12/94", 
                             genere="Maschio")


class Dipendente(Persona):
    
    def __init__(self, 
                 name: str, 
                 cognome: str, 
                 data_di_nascita: str, 
                 genere: str,
                 ore_lavorate: int) -> None:
        super().__init__(name, cognome, data_di_nascita, genere)
        self.ore_lavorate: int = ore_lavorate

        
    def calcola_stipendio(self)->float:
        
        return 500.0

    def __str__(self) -> str:
        return super().__str__()


dipendente_1: Dipendente = Dipendente(name="Flavio", 
                             cognome="Giorgi", 
                             data_di_nascita="24/12/94", 
                             genere="Maschio",
                             ore_lavorate=500)



class Professore(Dipendente):
    
    def __init__(self, 
                 name: str, 
                 cognome: str, 
                 data_di_nascita: str, 
                 genere: str, 
                 ore_lavorate: int,
                 materia_insegnata: str,
                 ore_di_lezione: int) -> None:
        super().__init__(name, cognome, data_di_nascita, genere, ore_lavorate)
        
        self.materia_insegnata: str = materia_insegnata
        self.ore_di_lezione: int = ore_di_lezione
        
    def __str__(self) -> str:
        return super().__str__()

print(persona_1.calcola_eta())

print(dipendente_1.ore_lavorate)
print(dipendente_1.nome)
print(dipendente_1.calcola_eta())
print(dipendente_1.calcola_stipendio())



professore_1: Professore = Professore(name="Flavio", 
                             cognome="Giorgi", 
                             data_di_nascita="24/12/94", 
                             genere="Maschio",
                             ore_lavorate=500,
                             materia_insegnata="Python",
                             ore_di_lezione=1000)

print(professore_1.ore_di_lezione)








class Person:
    
    def __init__(self, 
                 name: str, 
                 surname: str, 
                 birth_date: str, 
                 birth_place: str, 
                 gender: str) -> None:
       
       self._name: str = name 
       self._surname: str = surname
       self._birth_date: str = birth_date
       self._birth_place: str = birth_place
       self._gender: str = gender
       self._ssn: str = None
       
       self.compute_ssn()
        
        
    def get_ssn(self) -> str:
        """
        This function returns the ssn value
        input: none
        return: self._ssn : str, the function returns the ssn value       
        """
        
        return self._ssn
    
    def set_ssn(self, ssn: str) -> None:
        """
        This function set the ssn
        input: ssn : str, the parameter contains the user's snn
        return: None
        """
        
        raise Exception("You cannot modify the ssn number!")

    def get_name(self) -> str:
        """
        This function returns a person's name
        input: none
        return: self._name : str, the function returns the person's name
        """
        
        return self._name
    
    def set_name(self, name: str) -> None:
        """
        This function set the attribute name
        input: name : str, the parameter contains the user's name
        return: None
        """
        
        self._name = name.lower()
        self._ssn = self.compute_ssn()
    
    def compute_ssn(self) -> None:
        """
        Check the ssn's correctness
        """
        
        first_three_name_char = self._name[:3]
        last_three_surname_char = self._surname[-3:]
        self._ssn = first_three_name_char.upper() + last_three_surname_char.upper()


class Dipendente(Person):
    
    def __init__(self, 
                 name: str, 
                 surname: str, 
                 birth_date: str, 
                 birth_place: str, 
                 gender: str,
                 ore_lavorate: int,
                 paga_oraria: float = 50) -> None:
        
        super().__init__(name, surname, birth_date, birth_place, gender)
        
        self.ore_lavorate: int  = ore_lavorate
        self.paga_oraria: float = paga_oraria
        self.full_time: bool = True
    
    def calcola_stipendio(self):
        
        return self.ore_lavorate * self.paga_oraria
        

class Professore(Dipendente):
    
    def __init__(self, 
                 name: str, 
                 surname: str, 
                 birth_date: str, 
                 birth_place: str, 
                 gender: str, 
                 ore_lavorate: int, 
                 paga_oraria: float = 50,
                 corso_1: int = 100,
                 corso_2: int = 50) -> None:
        
        super().__init__(name, surname, birth_date, birth_place, gender, ore_lavorate, paga_oraria)
    
        self.corso_1: int = corso_1
        self.corso_2: int = corso_2
        
    
    def calcola_orario_lezioni_totale(self):
        
        return self.corso_1 + self.corso_2
    
    def __str__(self) -> str:
        
        return f"Professor\n{self._surname}\n{self._name}"
    
    
    def __eq__(self, value: object) -> bool:
        
        return value.ore_lavorate == self.ore_lavorate
    
professore_1: Professore = Professore(name="Flavio", 
                          surname="Giorgi", 
                          birth_date="24/12/1994", 
                          birth_place="Rome", 
                          gender="Male",
                          ore_lavorate=0)

professore_2: Professore = Professore(name="Flavio", 
                          surname="Giorgi", 
                          birth_date="24/12/1994", 
                          birth_place="Rome", 
                          gender="Male",
                          ore_lavorate=100)

professore_1._surname #SBAGLIATO!!!!!!

print(professore_1 == professore_2)

print(str(professore_1))
#professore_1.get_surname() #CORRETTO!!!!
    
print(professore_1.calcola_stipendio())
 
        
dipente_1: Dipendente = Dipendente(name="Flavio", 
                          surname="Giorgi", 
                          birth_date="24/12/1994", 
                          birth_place="Rome", 
                          gender="Male",
                          ore_lavorate=100)

print(dipente_1.calcola_stipendio())



person_1: Person = Person(name="Flavio", 
                          surname="Giorgi", 
                          birth_date="24/12/1994", 
                          birth_place="Rome", 
                          gender="Male")

try:
    print(person_1.get_name())
except ValueError:
    print("Non puoi avere il nome perchè è schermato!")
#person_2: Person = Person(name="Valentino", surname="Rossi")

#print(person_1)

queue: list[Person] = [person_1]





from abc import ABC, abstractmethod

class AbcAnimal(ABC):


    @abstractmethod
    def verso():

        pass

    @abstractmethod
    def movimento(self):

        pass



class Cane(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super(). __init__()
   
        self.nome: str = nome
        self.velocità: float = 10.0 #m/s


    def verso(self):
        return print("Bau!")

    def movimento(self, t: int):
        return self.velocità * t
        



cane_1: Cane = Cane(nome="Pluto")        
cane_1.verso()
cane_1.movimento(t=10)

class Gatto(AbcAnimal):

    def __init__(self, nome: str) -> None:
        super(). __init__()

        self.nome = nome

    def verso(self) :
        return print("Miao")  


class ContoBancario:

    total_accounts = 0
    definizione: str = 'Conto Bancario'
    def __init__(self,iban, saldo, nome):

        self.iban = iban
        self.nome = nome
        self.saldo = saldo

        ContoBancario.total_accounts += 1
   
    def  deposito(self, importo):
        self.saldo += importo
        print(f'{importo}depositato. Il nuovosaldo è:{self.saldo}')

    def prelievo(self, importo):
        self.saldo -= importo
        print(f'{importo} prelevato. Il nuovo saldo è {self.saldo}')    


    @classmethod
    def get_total_accounts(cls):
        print(f'Account totali creati: {cls.total_accounts}')   


    @classmethod
    def get_type(cls):
            print(f'Type{cls.definizione}')
    @staticmethod
    def valida_account(iban):     

        if isinstance(iban, int) and len(str(iban)) == 10:
            print('iban valido')
            return True

        else:
            print('iban non valido')
            return False

account1 = ContoBancario(1234567890, 0, 'Alice')            
account2 = ContoBancario(9876543210, 1000, 'Bob')       
account1.deposito(500)
account1.prelievo(200)

account2.deposito(200)
account2.deposito(150)

ContoBancario.get_total_accounts()

ContoBancario.valida_account(1234567890)
ContoBancario.valida_account(3456789097)


from typing import Any

class Banca:

    def __init__(self,nome: str,simbolo: str) -> None:
        self.nome: str = nome
        self.simbolo: str = simbolo
        self.lista_filiali: list[Filiale] = []

    def numero_filiali(self) -> int:
        return len(self.lista_filiali)

    def aggiungi_filiale(self, filiale: Filiale):

        if self.simbolo in filiale.codice:

            self.lista_filiali.append(filiale)
        else:
            raise ValueError  ("Non è la stessa banca")  


class Filiale:
 
    filiali_create: int = 0
    @classmethod
    def totale_filiali_create(cls) -> int:
        return cls.filiali_create


    def __init__(self,codice: str, indirizzo: str,banca: Banca ) -> None:
        self.codice = codice
        self.indirizzo = indirizzo
        self.banca = banca


unicredit: Banca = Banca(nome="Unicredit", simbolo="UCG")
intesa: Banca = Banca(nome="Intesa San Paolo", simbolo="ISP")
filiale_unicredit_1: Filiale = Filiale(codice="UCG01", indirizzo="Via Sierra Nevada 01,Roma",
                                       banca=unicredit)
filiale_intesa_1 = Filiale = Filiale(codice="ISP01", indirizzo= "Via Roma60,Roma", banca=intesa) # type: ignore


unicredit.lista_filiali.append(filiale_unicredit_1)
intesa.lista_filiali.append(filiale_intesa_1)
print(filiale_unicredit_1.banca.nome)
print(intesa.numero_filiali())
print(Filiale.totale_filiali_create())













