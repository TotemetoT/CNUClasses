import numpy as np

#Numpy Array Creation from Lists
print ("NumPy Array Creation from Lists")
list1 = [0, 1, 2]
list2 = [2, 3, 4]
arr_1d = np.array(list1)
print("arr_1d = ", arr_1d)
print("arr_1d.shape = ", arr_1d.shape)
print("len(arr_1d) = ", len(arr_1d))
arr_2d = np.array([list1, list2])
print("arr_2d = ", arr_2d)
print("arr_2d.shape = ", arr_2d.shape)
print("len(arr_2d) = ", len(arr_2d))
print("\n\n\n\n")

#NumPy Array Creation within a range
print ("NumPy Array Creation within a range")
x = np.linspace(0, 3, num=30)
print("x = ", x, "\n|x|= ", len(x))

x2 = np.arange(0, 3, 0.1)
print("x2 = ", x2, "\n|x2|= ", len(x2))

print("\n\n\n\n")

#Numpy Empty Array Creation
print ("NumPy Empty Array Creation")
arr_1d = np.zeros([5])
print("arr_1d = ", arr_1d)
arr_2d = np.zeros([5, 2])
print("arr_2d = ", arr_2d)
arr_3d = np.zeros([5, 2, 3])
print("arr_3d = ", arr_3d)
print("\n\n\n\n")

#NumPy Overridden Operators
print ("NumPy Overridden Operators")
arr1 = np.ones([5])
print("arr1 = ", arr1)
arr1 *= 5
print("arr1 = ", arr1)
arr1 += 3
print("arr1 = ", arr1)
arr2 = np.arange(0, 5, 1)
print("arr2 = ", arr2)
arr3 = arr1+arr2
print ("arr3 = ", arr3)
print("\n\n\n\n")

#Numpy Mathematical Operations and Sum
print ("NumPy Mathematical Operations and Sum")
arr1 = np.arange(0, 5, 1)
print("arr1 = ", arr1)
print("sum(arr1) = ", sum(arr1))
arr1 = np.sqrt(arr1)
print("arr1 = ", arr1)
arr2 = np.array([[1, 2, 3], [3, 4, 5]])
print("sum(arr2) = ", sum(arr2))
print("\n\n\n\n")

#Numpy logical indices
print ("Numpy logical indices")
degrees = np.arange(0, 365, 10)
rads = arr1 * (np.pi/180)
cosine_values = np.cos(arr1)
print("cosine values = ", cosine_values)
negative_logical = cosine_values < 0
print("less_than_one_logical = ", negative_logical)
negative_values = cosine_values[negative_logical]
print("less_than_one_values = ", negative_values)
