#Define functuon 
# add paramater 
# if statement (possibly)
# Function inside of function
# 

# def r_sigma(num):
#     if num>0:
#         print(num)
#         # calling function and sub by 1 and shows the total at bottom
#         return r_sigma( num - 1 ) + num
#     return 0

# print( r_sigma(5))

# Recursive Function
# Given num, return the product of ints from 1 up to num
# If less than 0 treat as 0. If not an int. 
# truncate. Experts tell us 0! is 1. rFact(3) = 6 (1*2*3).
# Also rFact(6.5) = 720 (1*2*3*4*5*6)


# def factorial(num: int):
#     if num == 0:
#         print(num)
#         return 1
#     return factorial( num - 1 ) * num


# print(factorial(6))