"""
1. GESTIONALE PAGAMENTO
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del 
pagamento e si definiscano appropriati metodi get() e set(). L'importo non è un parametro da passare in input alla classe 
Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() 
che visualizza una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". Quando viene stampato,
 l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. 
Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. Si definisca 
inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 
5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per 
pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta 
di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito 
oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti
 e si invochi dettagliPagamento() per ognuno di essi.
"""

class Pagamento:

    def __init__(self) -> float:
        self.importo = 0.0

    def set_importo(self, importo: float):
        if isinstance(importo, float) and importo >= 0:
            self.importo = importo   

        else:
            print("L'importo deve essere un valore positivo di tipo float")     

    def get_importo(self) -> float:
        return self.importo
    
    def PaymentDetail(self):
        return f"Importo del pagamento: {self.importo:.2f} euro"
    

class PagamentoContanti(Pagamento):

    
    def PaymentDetails(self) -> float:
        return f"Pagamento in contanti : {self.importo} euro"
          
    def InPezziDa(self):
        
        importo_restante = self.importo
        banconote = [500, 200, 100, 50, 20, 10]
        monete = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
        pezzi = {}

        for banconota in banconote:
            quantita = importo_restante // banconota
        
            if quantita > 0:
                pezzi[f"{banconota} euro"] = quantita
                importo_restante -= quantita * banconota     


        for moneta in monete:
            quantita = int(importo_restante / moneta)
            if quantita > 0:
                pezzi[f"{moneta} euro"] = quantita
                importo_restante -= quantita * moneta
        


        return pezzi 
    

importo_da_pagare = 1234.56
pagamento = PagamentoContanti(importo_da_pagare)
pezzi_necessari = pagamento.InPezziDa()

for pezzo, quantita in pezzi_necessari.items():
    print(f"{pezzo}: {quantita}")


class PagamentoCartadiCredito(Pagamento):
    def __init__(self):
        super().__init__()



pagamento = Pagamento()
pagamento.set_importo(20.0)
print(pagamento.PaymentDetail())















