#1-Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.


def trova_chiave_per_valore(dizionario: dict[str, int], valore: int) -> str:

    for chiave, val in dizionario.items():
        if val == valore:
            return chiave
    return None



#2- Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.

def classifica_numeri(lista: int) -> dict[str:list[int]]:

    risultato = {'pari': [], 'dispari': []}

    for number in lista:
        if number % 2 == 0:
           risultato['pari'].append(number)

        else:
            risultato['dispari'].append(number)
    
    return risultato

#3- Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi e il numero di 
#volte che devono essere rimossi come valori.

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]: # type: ignore

    for elemento, frequenza in da_rimuovere.items():
        while frequenza > 0 and elemento in lista:
            lista.remove(elemento)
            frequenza -= 1 
        return lista
    


#4- Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.


def aggrega_voti(registro: list[dict]) -> dict:
    # cancella pass e scrivi il tuo codice
   # input  voti  = [{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]
    #output  {'Alice': [90, 85], 'Bob': [75]}  
    nuovo_registro = {}

    
    for studente in registro:

        nome = studente['name']
        voto = studente ['voto']
    
        if nome in nuovo_registro:
            nuovo_registro[nome].append(voto)
            print(nuovo_registro[nome])

        else:
                nuovo_registro[nome] = [voto]
        
    return nuovo_registro

print(aggrega_voti([{'name': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))


#5- Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo 
#dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.


def applica_sconto(prodotti):

    prodotti_scontati = {}
    
    for prodotto, prezzo in prodotti.items():
        if prezzo > 20:
            prezzo_scontato = prezzo * 0.9
            prodotti_scontati[prodotto] = prezzo_scontato
    return prodotti_scontati

prodotti_scontati = applica_sconto(prodotti_originali)
print(prodotti_scontati)




#6- PARTE 1 Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo).
# La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
#PARTE 2
#Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il 
#dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.




def create_contact(name: str, email: str = None, telefono: int=None) -> dict: # type: ignore
    
    contatto = {'profile': name, 'email': email, 'telefono': telefono}

    return contatto

contatto1 = create_contact("Marco Cascio", "marco.cascio@unitelmasapienza.it")
print(contatto1)


#Esempio update_contact(dict, "mario rossi", tel = 3456788)


def update_contact(contatto: dict, name: str, email: str =None, telefono: int=None) -> dict: # type: ignore
    if contatto['profile'] == name:
        if  email:
            contatto['email'] = email
        if telefono:
            contatto['telefono'] = telefono
    
    return contatto

contatto1 = update_contact(contatto1,'Marco Cascio' telefono=33333333)

print(contatto1)









