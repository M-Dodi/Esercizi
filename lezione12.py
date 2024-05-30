"""
Sistema di Prenotazione Cinema
Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso 
film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
"""

class Film:

    def __init__(self,title: str, duration: str) -> None:
    
        self.title = title
        self.duration = duration
        


class Sala:

    def __init__(self,numero_sala: int, film_in_programma: str, posti_totali:
                  int,):

        self.numero_sala = numero_sala
        self.film_in_programma = film_in_programma
        self.posti_totali = posti_totali
        self.posti_prenotati = 0

    def prenota_posti(self, num_posti: int):
        
        if self.posti_prenotati + num_posti <= self.posti_totali:
            self.posti_prenotati += num_posti

            return f"Prenotazione confermata per {num_posti}."

        else:
            return f"Spiacenti, non ci sono abbastanza posti disponibili."

    def posti_disponibili(self): 

        return self.posti_totali - self.posti_prenotati

class Cinema:
    def __init__(self):

        self.sale = []

    def aggiungi_sala(self,sala: int):
        self.sale.append(sala)     

    def prenota_film(self,title_film: str, num_posti: int):
        for sala in self.sale:
            if sala.film_in_programma == title_film:
                return Sala.prenota_posti(num_posti)
        return  "Film non trovato"
    

cinema = Cinema()
film = Film("Avengers: Endgame", "3 ore")
sala1 = Sala(1, "film", 100)
cinema.aggiungi_sala(1)

titolo_film_desiderato = "Avengers: Endgame"
num_posti_desiderati = 5
risultato_prenotazione: str = cinema.prenota_film(titolo_film_desiderato, num_posti_desiderati)
print(risultato_prenotazione)
