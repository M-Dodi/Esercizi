# Dato un itero x , restituisce True se x è palindromo è False altrimenti

def is_palindrome(x):
    x_str = str(x)
    return x_str == x_str[::-1]


x = 12345
print(f"L'intero{x} è palindromo? {is_palindrome(x)}")
