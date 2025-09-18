import numpy as np


# 1D Array
array_1d = np.array([0, 20, 30, 40, 50, 60])
print("1D array:", array_1d)
print("Slice [2:]:", array_1d[2:])
print("Slice [3:5]:", array_1d[3:5])
print("Element [-4]:", array_1d[-4])
print("Reversed array:", array_1d[::-1])
print("Dimension of array_1d:", array_1d.ndim)
y = array_1d.copy()
print("type of y: ", type(y))
z = array_1d.view()
print("type of z: ", type(z))

# sum 2D array
array_2d = np.array([[0, 20, 30],[40, 50, 60]])
print("2D array:", array_2d)
print("[0][1]", array_2d[0][1])
print("[1][1]", array_2d[1][1])
print("[0][2]", array_2d[0][2])
print("Sum of all elements:", sum(array_2d))
print("Dimension of array_2d:", array_2d.ndim)


# 3d array
array_3d = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])
print("[0][0][0]:", array_3d[0][0][0])
print("[0][1][2]:", array_3d[0][1][2])
print("[1][1][2]:", array_3d[1][1][2])

arr_3d = np.array(array_3d)
print("Dimension of array_3d:", arr_3d.ndim)