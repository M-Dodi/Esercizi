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
