from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name, last_name, age, specialization, parcel):
        
        super().__init__(first_name, last_name)
    
        self.specialization = None
        self.parcel = None
        self.setSpecialization(specialization)
        self.setParcel(parcel)

    
    def setSpecialization(self, specialization):
        if isinstance(specialization, str):
            self.specialization = specialization

        else:
            print("La specializzazione inserita non è una stringa!")


    def setParcel(self, parcel):

        if isinstance(parcel, float):
            self.parcel = parcel

        else:
            print("La parcella inserita non è un float!")


    def getSpecialisation(self): 
        return self.specialization


    def getParcel(self):
        return self.parcel
    

    def isAValidDoctor(self):
        if self.age > 30:
            print(f"{self.first_name} {self.last_name} is valid")


        else:
            print(f"{self.first_name} {self.last_name} is not valid!")    


    def doctorGreet(self):
        print(f"Ciao, sono il Dr.{self.last_name}. Piacere")


if __name__ == "__main__":
    pass