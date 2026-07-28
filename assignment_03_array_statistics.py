# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def main(): 
    store=[]
    numbers=int(input("Enter a number? "))
    for i in range(numbers):
        num=float(input("Enter a number: "))
        store.append(num)
    
    def sum():
        add=0
        for i in store:
            
             add= add + i
    
        return add
         
        
    def max():
        largest_num=store[0]
        for numbers in store:
            if numbers > largest_num:
                largest_num=numbers
        return largest_num

    def min():
       
        smallest_num=store[0]
        for numbers in store:
            if numbers < smallest_num:
                smallest_num=numbers
        return smallest_num
    
    sum=sum()
    
    def average():
        return sum/numbers
    
    print (f"Sum : {sum}\n")
    print (f"Max : {max()}\n")
    print (f"Min : {min()}\n")
    print (f"Average : {average()}")
    
        
main()
