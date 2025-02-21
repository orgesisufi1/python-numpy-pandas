import numpy as np

#Empty array with 5 elements
empty = np.empty((5))
# print(empty)


#1D array of 10 elements containing ones
ones = np.ones(10, dtype='int32')
# print(ones)

#1D array of 10 elements containing zeros
zeros = np.zeros(10, dtype='int32')
# print(zeros)

#Identity matrix full of 0 but diagonal of 1
identity = np.identity(4, dtype='int32')
# print(identity)

#3x3 array filled with value of 7.5
arr = np.full((3,3), 7.5)
# print(arr)

#3x3 array filled with value of 3.14
arr1 = np.full((3,3), 3.14)
# print(arr1)

#create a 5x5 matrix that's filled with zeros everywhere, but has the value 9 on the main diagonal.
# 2 ways of filling the diagonal: 1. Indexing, 2.np.fill_diagonal
identity5 = np.identity(5, dtype='int32')
identity5[[0,1,2,3,4], [0,1,2,3,4]] = 9
# print(identity5)

identity5_1 = np.identity(5, dtype='int32')
np.fill_diagonal(identity5_1, 9)
# print(identity5_1)


#Trigonometry

#Create an array of angles in radians: [0, np.pi/6, np.pi/3, np.pi/2, np.pi]
radians = np.array([0, np.pi/6, np.pi/3, np.pi/2, np.pi])
#Calculate sine, cosine and tangent of radians
# print("Sine: ", np.sin(radians))
# print("Cosine: ", np.cos(radians))
# print("Tangent: ", np.tan(radians))


#Calculate the correlation between a and b.
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
# print(np.corrcoef(a,b)[0,1])


#Logical operations
array = np.array([True, False, True, False, True])
#Check if all alements in array are True
# print(np.all(array))
#Check if any alements in array is True
# print(np.any(array))