import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading the csv file
df1=pd.read_csv("Marks.csv")

#Total and Percenrtage Calculation
df1['Total']=df1.iloc[:,1:].sum(axis=1)
df1['Percentage']=(df1['Total']/300*100).round(2)

#Class topper And Subject wise Average
topper=df1.loc[df1['Total']==df1['Total'].max(),'Name']
print("Class Topper is:",topper)
print("\nSubject wise Average:\n",'Maths',df1['Math'].mean(),'\n','Science',df1['Science'].mean(),'\n','English',df1['English'].mean())

df1.to_csv("Result.csv",index=False)

#Data Visualization
df1.plot(x='Name',y=['Math','Science','English'],kind='bar')
plt.title('Subject wise Marks')
plt.xlabel('Students')
plt.ylabel('Marks')

#To display the plot
plt.show()

#Student Vs total marks
df1.plot(x='Name',y='Total',kind='bar',color='orange')
plt.title('Student vs Total Marks')

#To display the plot
plt.show()