from persona import Persona

class Paziente(Persona):
   
    def __init__(self, first_name, last_name,idCode):
        super().__init__(first_name, last_name)

        self.idCod = idCode

    def setidCode(self, idCode):
        self.idCode = idCode
             
        
    def  getidCode(self):  
        return self.idCod

    def patientInfo(self):
        return f"Paziente: {self.first_name} {self.last_name}\nID: {self.idCode}"

