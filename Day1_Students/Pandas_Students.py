import pandas as pd 

#Read The File
df = pd.read_csv("students.csv")
#Print First Five Row
print(df.head(5))

#Top 5 Students With Highest Marks
print(df.sort_values(by = 'Marks' , ascending = False).head(5))

#Avgerage Marks Per Subject
print(df.groupby('Subject')['Marks'].mean())

#Student With Marks Greater Then 85
print(df[df['Marks'] > 85])

