import numpy as np 

# myList = ["Jacob","Abdullah","Jamal","Fatima","Shahzain"]

# numpyArray = np.array(myList)

# for x in np.nditer(numpyArray):
#     print(x)

myList = [[1,2,3],[4,5,6],[7,8,9]]

numpyArray = np.array(myList)

for x in np.nditer(numpyArray):
    print(x)

# we can iterate through the numpy array using the nditer() method. like complex arrays like 2d or 3d arrays.