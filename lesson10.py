import numpy as np 

myList = [[1,2,3],[4,5,6],[7,8,9]]
myArray = np.array(myList)

# for x in np.nditer(myArray,flags=['buffered'],op_dtypes=['S']):
#     print(x)
# This will change the data type while iterating only not changing the origional data types


# for x in np.nditer(myArray[:,::2]):
#     print(x)
# thats how we can perform slicing through numpy arrays

# for x in np.nditer(myArray,op_flags=['readwrite']):
#     print(x)

# for id,x in np.ndenumerate(myArray):
#     print(id,x)
# This will print the index of the element and the element itself