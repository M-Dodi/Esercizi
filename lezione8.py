#--1-- You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the 
#number of elements in nums1 and nums2 respectively. Write a function to merge nums1 and nums2 into a single array sorted
#in non-decreasing order.
#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
#To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and 
#the last n elements are set to 0 and should be ignored. nums2 has a length of n.




def merge(nums1, m, nums2, n):
    
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Copy remaining elements from nums2 (if any)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)        




# --2--Given a string s which consists of lowercase or uppercase letters, write a function that returns the 
#length of the longest palindrome that can be built with those letters. Letters are case sensitive, for example,
# "Aa" is not considered a palindrome here.


def longest_palindrome(s: str) -> int:
    from collections import Counter  # to search occurrences

    letter_counts = Counter(s)   # is a dictionary with caracters as keys and values their counts 
    length = 0                    # will hold the total palindrome we are serching
    odd_count_found = False       # is a bolean flag to track the odd count caracters
   
   
    for count in letter_counts.values():   # looping through the count value in our dictionary
        if count % 2 == 0:
            length += count                # we add the even counts  
        else:
            odd_count_found = True         # here we adjust the odd count - 1 to mantain symmetry
            length += count - 1
    
    if odd_count_found:                     # at least one odd count caracter we add it to the length(center)
        length += 1
    
    return length                


print(longest_palindrome("abccccdd"))



#--3 --Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the
# functions of a normal stack (push, top, pop, and empty).
#Implement the MyStack class:

#- push(x: int) -> None: Pushes element x to the top of the stack.
#- pop() -> None Removes the element on the top of the stack and returns it.
#- pop() -> None Returns the element on the top of the stack.
#- empty() -> None Returns true if the stack is empty, false otherwise.


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        # Append the new element to the end of the list
        self.stack.append(x)

    def pop(self) -> int:
        # Pop the last element (which is the top of the stack)
        return self.stack.pop()

    def top(self) -> int:
        # Peek at the last element without removing it
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

# Example usage:
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())  # Returns 2
print(myStack.pop())  # Removes and returns 2
print(myStack.empty())  # Returns False










#--5--Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.
#An input string is valid if: 
    #Open brackets must be closed by the same type of brackets.
    #Open brackets must be closed in the correct order.
    #Every close bracket has a corresponding open bracket of the same type.


def is_valid_parenthesis(s: str) -> bool:
    open_parenthesis = 0     #initialize counter for each type
    open_braces = 0
    open_brackets = 0
    
    for char in s:
        if char == '(':
            open_parenthesis += 1   #if opening sign count +1
        elif char == ')':           
            open_parenthesis -= 1    #if closing sign count -1
        
        elif char == '{':
            open_braces += 1
        elif char == '}':
            open_braces -= 1
            
        elif char == '[':
            open_brackets += 1
        elif char == ']':
            open_brackets -= 1
    
    return open_parenthesis == 0 and open_braces == 0 and open_brackets == 0    #if all counters are zero is a valid  string   


print(is_valid_parenthesis("([)]"))




