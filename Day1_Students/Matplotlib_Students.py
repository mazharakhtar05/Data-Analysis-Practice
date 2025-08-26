import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("students.csv")
avg_marks = df.groupby('Subject')['Marks'].mean()
plt.bar(avg_marks.index, avg_marks.values , color = 'skyblue')
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.title("Subject Wise Average Marks")
plt.show()
