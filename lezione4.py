def substract(x:float,y:float) -> float:
    
    print(f"x={x}, y={y}")
    return x - y

x = 3
y = 5
out = substract(x,y)
print(f'La diff è {out}')


#write a function check_value() witch takes a number as argument
#using if/else should print wether the number is bigger smaller or equal to 5



def check_value(number: int):
    if number > 5:
        print(f"{number} è più grande di 5")
    elif number < 5:
        print(f"{number} è più piccolo di 5")
    else:
        print(f"{number} è uguale a 5")        

check_value(4)
check_value(7)
check_value(5)

#write a function print_numbers(), which takes a list of numbers
#as argument using a for loop, print each number one by one

def print_numbers(numbers_list):
    for number in numbers_list:
        print(number)

print_numbers([1,2,3,4,5])