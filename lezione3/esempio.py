reader = open("esempio.txt", encoding="utf-8")


# metodo veloce--------
with open(f"files/esempio.txt") as f:
        print(f)
#---------------------



try:
    reader.readline()
    print("Sono nella try")
    raise Exception("Eccezione")     
except Exception:
    print("Sono nella exclsept")   

finally:
    print("sono nella finally")           
    reader.close()



class ContexMenager:
    def __enter(self):
        print("Ciao sono nell enter")
        return self

    def __exit(self, exc_type, exc_value, traceback):
           
        if exc_type is not None:
                print("Eccezione")
        return False
      
with ContexMenager() as cm:
     print("ciao")
     print(cm)

