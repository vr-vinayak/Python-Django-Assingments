""" Write a Python program that analyzes a given dataset (in CSV format) named "data.csv" and performs the following tasks:
1.	Calculate the average value of salary.
2.	Find the minimum and maximum values of Age.
3.	Count the number of rows that satisfy the condition that “age is 28 and Gender is Female”"""

import pandas as pd
class DataAnalysis:
    def __init__(self, file) -> None:
        self.file =file
    
    # Calculate the average value of salary.
    def calc_avg_salary(self):
        data = pd.read_csv(self.file)
        salary_data = data['Salary'].mean()
        return {'average_salary': salary_data}
   
    # Find the minimum and maximum values of Age.
    def calc_min_max_age(self):
        data = pd.read_csv(self.file)
        min_age, max_age = data['Age'].min(), data['Age'].max()
        return {'min_age': min_age, 'max_age': max_age}
   
    #Count the number of rows that satisfy the condition that “age is 28 and Gender is Female”
    def _number_of_row(self):
        data = pd.read_csv(self.file)
        count = data.query("Age == 29 and Gender == 'Female'").shape[0] #shape[0] means rows, 1 for columns
        return {'total_rows': count} #as there is no female with age of 28, hence the count is 0.

data_obj = DataAnalysis(r'/Users/vinayakrao/Documents/Work/Assignment/assignment_3/data.csv')
print(data_obj.calc_avg_salary())