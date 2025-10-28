import pandas as pd

student_data = {}

for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    score = float(input(f"Enter score for {name}: "))
    student_data[name] = score


scores= pd.Series(student_data)

average_score = scores.mean()
max_score = scores.max()
min_score = scores.min()
total_score = scores.sum()

print(f"Average Score: {average_score}")
print(f"Maximum Score: {max_score}")
print(f"Minimum Score: {min_score}")
print(f"Total Score: {total_score}")

ascending = scores.sort_values()
descending = scores.sort_values(ascending=False)

print(ascending)
print(descending)
