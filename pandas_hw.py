import pandas as pd

    
names = []
scores = []

def student_data():
    for i in range(5):
        names.append(input(f"Enter name for student {i+1}: "))
        scores.append(int(input(f"Enter score for student {i+1}: ")))

student_data()
print("\nStudent Scores")


series=pd.Series(scores,index=names)
print(series)

