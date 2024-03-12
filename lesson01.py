import numpy as np 

# creaing a numpy array of list
myList = [1,2,3,4,5,6,7,8,"Hello","I am","String inside list"]
myNumpyArray = np.array(myList)
print(type(myNumpyArray))
print(myNumpyArray)
# creating a numpy array of a tuple
myTuple = (1,2,3,4,5)
myNumpyArray2 = np.array(myTuple)
print(type(myNumpyArray2))
print(myNumpyArray2)

# If there is one string inside any other array object, numpy array will convert every element into string
myTuple2 = (1,2,3,4,5,"Hello","I am","Another String inside tuple")
myNumpyArray3 = np.array(myTuple2)
print(type(myNumpyArray3))
print(myNumpyArray3)
