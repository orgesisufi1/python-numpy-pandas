import numpy as np

animals = np.array(['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Zebra', 'Monkey'], dtype=str)

animal_height = np.array([5.3, 4.4, 8.2, 9.5, 5.9, 3.7])

view_arr = animals.view()
animals[0] = 'Panther'
print("Original array: ", animals)
print("")
print("View method: ", view_arr)
print("")

copy_arr = animal_height.copy()
animal_height[0] = 4.1
print("Original array:  ", animal_height)
print("")
print("Copied array: ", copy_arr)
print("")

updated_height = animal_height.reshape(2,3)
print("Reshaped array: \n", updated_height)
print("")
print("Flattened array: ", updated_height.flatten())
print("")

animal_counts = np.array([4.5, 2.4, 5.6, 4.2, 3.7])
new_animal_counts = np.array([3.5, 6.2, 4.2, 5.2, 4.4])
new_array = np.concatenate((animal_counts, new_animal_counts))
print("Animal_counts: ", animal_counts)
print("New animal count: ", new_animal_counts)
print("Concatenate: ", new_array)