import numpy as np 

# Reverse 
# arr = ["10", "12", "140", "56"]
# print("Before", arr)

# arr.reverse()
# print("After:", arr)

# Rotate
# array = np.arange(12).reshape(3,4)
# print("Original array : \n", np.roll(array, 1))

# Filter Range 
# # set an array 
# nums = ["11", "21", "85", "32", "50", "70"]
# # set function to return elements between min and max
# print (max(nums))
# print (min(nums))
# a = np.arange(nums["11", "21", "85", "32", "50", "70"])
# print(np.clip(a, 11, 85))

#merge list
list1 = ["10", "20", "30"]
list2 = ["15", "25", "35"]

list3 = [item for sublist in zip(list1, list2) for item in sublist]

print(list3)