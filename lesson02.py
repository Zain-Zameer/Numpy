import numpy as np 

# zero dimensional array
zeroDimensional = 20
print(np.array(zeroDimensional))

# one dimensional array
oneDimensional = [1,2,3,4,5]
print(np.array(oneDimensional))

# two dimensional array
my2DimenionalList = [
    [1,2,3,4],
    [5,6,7,8]
]
print(np.array(my2DimenionalList))

# three dimensional array
print("\n3 Dimentional array: ")
my3DimenionsionalList = [
    [
    [1, 2, 3],
    [4, 5, 6]
    ],

    [
    [1, 2, 3], 
    [4, 5, 6]
    ]
]
print(np.array(my3DimenionsionalList))

print("Checking number of dimensions:\n")
zeroDime = np.array(46)
oneDime = np.array(oneDimensional)
twoDime = np.array(my2DimenionalList)
threeDime = np.array(my3DimenionsionalList)
print(zeroDime.ndim)
print(oneDime.ndim)
print(twoDime.ndim)
print(threeDime.ndim)

# pre defining array dimensions
arr = np.array([1,2,2,4,5,6],ndmin = 5)
print("\n"+str(arr))
print(arr.ndim)