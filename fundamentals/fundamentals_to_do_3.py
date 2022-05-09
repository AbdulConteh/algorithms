# biggie size 


# def makeItBig(arr):
#     arr = [-1, 3,-4,5,-6]
#     for i in arr:
#         if i > 0:
#             print("big")
#         else:
#             print(i)
#         new_arr = []
#         new_arr.append(arr)
#     return new_arr

# Print Low Return High

# def plrh():
#     arr = [1,2,3,4,5,6,7]
#     max_arr = max(arr)
#     min_arr = min(arr)
#     print(min_arr)
#     return(max_arr)

# print(plrh())

# Print One, Return Another 

# def pora():
#     arr = [9,8,7,6,5,4,3]
#     print(arr[5])
#     return arr[0]

# print(pora())

# # double vision 

# def dv():
#     arr = [2,4,8]
#     new_arr = []
#     for i in arr:
#         new_arr.append(i + i)
#     print(new_arr)

# print(dv())

# count positives 
def countPositives():
    arr = [-5, 2, 2, 2]
    for i in arr:
        if i > 0:
            arr[3] = sum(len(arr))



print(countPositives())
