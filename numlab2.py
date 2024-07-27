import numpy as np
#convert the below list into numpy array then display the array
my_list = [1, 2, 3, 4, 5]

my_array = np.array(my_list)

print("NumPy Array:", my_array)



#convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.
my_list = [1, 2, 3, 4, 5]

my_array = np.array(my_list)

print("NumPy Array:", my_array)

print("First element:", my_array[0])
print("Last element:", my_array[-1])

multiplied_array = my_array * 2

print("Array after multiplying each element by 2:", multiplied_array)




#write a mumpy program to create a array of 10 zeros,10 ones, and 10 fives

zeros_array = np.zeros(10, dtype=int)
ones_array = np.ones(10, dtype=int)
fives_array = np.full(10, 5, dtype=int)

combined_array = np.concatenate((zeros_array, ones_array, fives_array))
print("Combined Array:", combined_array)



#write a numpy program to create a 3*3 matrix with values ranging from 2 to 10.
values = np.arange(2, 11)  # This creates an array [2, 3, 4, 5, 6, 7, 8, 9, 10]

matrix = values.reshape(3, 3)

print("3x3 Matrix:\n", matrix)