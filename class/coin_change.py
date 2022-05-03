# #function (parameters)
# #var (coins)
# #   quarters
# #   dimes
# #   pennies
# #conditional statement 
# #   if statement 
# #loop 
# #   for or whie loop 
# #print statement 


# def coin_change(amount):
#     #start at 0 becuase we're incrememting by 1 
#     dollars = 0
#     quarter = 0 
#     dime = 0 
#     nickel = 0 

#     while amount >= 100:
#         quarter += 1
#         amount -= 100
#     while amount >= 25:
#         quarter += 1
#         amount -= 25
#     while amount >= 10:
#         dime += 1 
#         amount -= 10
#     while amount >= 5:
#         nickel += 1
#         amount -= 5
#     pennies = amount

#     return(f" Dollars: {dollars}, quarters: {quarter}, Dimes: {dime}, Nickels: {nickel}, Pennies: {pennies}") 
# print(coin_change(50))


