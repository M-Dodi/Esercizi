# Dato un intero col_number restituisce il suo corrispondente titolo di colonna come 
#ad esempio compare su un foglio Excel

def convert_to_title(col: int) -> str:
    title = ""
    col -= 1
    while col > 0:
        reminder = col % 26
        title = chr(ord('A') + reminder) + title
        col //= 26
    return title
column_number = 52
print(f"Column {column_number} correspond to title: {convert_to_title(column_number)}") 



#Data una lista nums di n elementi, restituisce l'elemento che compare n/2 volte

def majority_element(nums: list[int]) -> int:

    count_dict = {} # dictionary to store count of elements

    for num in nums:   # count the occurrences of each elem
        if num in count_dict: count_dict[num] += 1
        else:
            count_dict[num] = 1
    majority_count = max(count_dict.values())
    for num, count in count_dict.items():
            if count == majority_count:
                return num        

input_nums = [3, 4, 5, 3, 7, 4, 3]
print(f"L'elemento più usato è: {majority_element(input_nums)}")




#Dato una lista di numeri spostare gli zeri alla fine della lista mantenendo l'ordine dei numeri originali

def move_zeroes(nums: list[int]):
    
    for i in range (len(nums)):
     if nums[i] == 0: 
        x = nums.pop(i)
        nums.append(x)
    return nums
input_nums = [0, 1, 0, 3, 12]

print(f"La nuova lista è: {move_zeroes(input_nums)}")
          




def visit_tree(tree: dict[int, list[int]], n: int):
    print(n)

    left_child, right_child = tree[n]   

    if left_child != None:
        visit_tree(tree, left_child)
    if right_child != None:
        visit_tree(tree, right_child)   

tree ={1:[2,3], 2:[4,5], 3:[None,None], 4:[None,None], 5:[None,None]} 

visit_tree(tree, 1)


def visiting_tree_iterative(tree: dict[int, list[int]], root: int):
    
    stack: list[int] = [root]

    while stack: # while len(stack) != 0
        curr_node = stack.pop(0)
        
        
        if curr_node:
            print(curr_node)
            
            left_child, right_child = tree[curr_node]
            
            if left_child:
                stack.append(left_child)
            if right_child:
                stack.append(right_child)

tree ={1:[2,3], 2:[4,5], 3:[None,None], 4:[None,None], 5:[None,None]} 

visiting_tree_iterative(tree, 1)
