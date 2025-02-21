import numpy as np

test_scores = np.array([85, 92, 78, 90, 88, 76, 95, 89, 83, 91])

scores_mean = test_scores.mean()
print("Mean score of the students: ", scores_mean)
print(" ")

passed = np.array([], dtype=int)
for score in test_scores:
    if score >= 80:
        passed = np.append(passed, score)
print("Scores of students who passed: ",passed)
print(" ")

reshape_array = test_scores.reshape(2,5)
print("2x5 array")
print(reshape_array)
print(" ")

print("First five students from the reshaped array: ",reshape_array[0])
print(" ")

print("Highest score: ", np.max(test_scores))
print("Lowest score: ", np.min(test_scores))

