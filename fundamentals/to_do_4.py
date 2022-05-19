import random

# arr = [2,4,6,8,10]
# lis = []
# for new_arr in arr:
#     if len(arr) < arr :
#         lis([arr])

# poor Kenny 
# create a function for randomizing days
# create a for loop to set range 
# create if and else statement for each weather event 

def whatHappenedToday():
    for i in range(1, 100, 1):
        if i <= 10:
            print("Volcanoes")
        elif i <= 20:
            print("tsumani")
        else:
            return i

print(random(whatHappenedToday()) )