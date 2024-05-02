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


# Dato un itero x , restituisce True se x è palindromo è False altrimenti

def is_palindrome(x):
    x_str = str(x)
    return x_str == x_str[::-1]


x = 12345
print(f"L'intero{x} è palindromo? {is_palindrome(x)}")
