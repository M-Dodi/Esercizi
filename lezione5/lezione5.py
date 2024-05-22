#La funzione dovrebbe determinare se un elemento è presente in una lista.
#Un errore nell'implementazione porta a risultati inaspettati.

def find_element(lst: list[int], element: int):
    for item in lst:
     if item == element:
        return True
    return False 
     
print(find_element([1, 2, 3, 4, 5], 2))


# 2- Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

import operator

def frequency_dict(elements: list):

# Creating an empty dictionary
	freq = {}
	for item in elements:
            if item in freq:
               freq[item] += 1
            else:
                 freq[item] = 1 
        return freq


if __name__ == "__main__":
	elements = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
	frequency_dict(elements)

# 3. Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
#La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione 
#e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare 
#lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista


def rotate_list(list, k):
	# Loop through the range of n positions to rotate
	for i in range(k):
		# Remove the last element of the list and insert it at the beginning
		list.insert(0, list.pop())
	# Return the rotated list
	return list


my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(my_list, 7)
print(rotated_list) 




#4. Scrivi una funzione che ritorna il valore massimo, minimo e la 
#media di una lista di numeri interi.


import statistics



def list_statistics(numbers: list[int]) -> ...:


	if not numbers:
	 	raise ValueError("input list is empty")
 
    
my_list  =  [10, 5, 8, 12, 3] 
numbers = my_list
maximum = max(numbers) 
minimum = min(numbers)
sum = sum(numbers)
mean = sum / len(numbers) 
        
		
        

print(f"Maximum: {maximum}, Minimum: {minimum}, Mean: {mean}")

     
              
#6. Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore 
#arrotondato all'intero più vicino.

# Python program to get average of a list 
def Average(lst): 
    return sum(lst) / len(lst) 

# Driver Code 
lst = [15, 9, 55, 41, 35, 20, 62, 49] 
average = Average(lst) 

# Printing average of the list 
print("Average of the list =", round(average, 2)) 
