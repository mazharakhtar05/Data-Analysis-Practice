import pandas as pd 
import numpy as np

#Read The File
df = pd.read_csv("students.csv")

marks = df['Marks'].to_numpy()
print("Mean" , np.mean(marks))
print("Median" , np.median(marks))
print("Standard Deviation", np.std(marks))

