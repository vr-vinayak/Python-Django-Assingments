""" Write a Python program that analyzes a given dataset (in CSV format) named "data.csv" and performs the following tasks:
1.	Calculate the average value of salary.
2.	Find the minimum and maximum values of Age.
3.	Count the number of rows that satisfy the condition that “age is 28 and Gender is Female”"""

class DataAnalysis:
    def __init__(self, file):
        self.file = file
    
    # Read CSV file and return a list of dictionaries
    def read_csv(self):
        with open(self.file, 'r') as f:
            lines = f.readlines()
            header = lines[0].strip().split(',')
            data = [line.strip().split(',') for line in lines[1:]]
            data_dicts = [dict(zip(header, row)) for row in data]
            return data_dicts
    
    # Calculate the average value of salary
    def calc_avg_salary(self):
        data_dicts = self.read_csv()
        total_salary = 0
        num_entries = len(data_dicts)
        
        for entry in data_dicts:
            total_salary += float(entry['Salary'])
        
        if num_entries > 0:
            average_salary = total_salary / num_entries
        else:
            average_salary = 0
        
        return {'average_salary': average_salary}
   
    # Find the minimum and maximum values of Age
    def calc_min_max_age(self):
        data_dicts = self.read_csv()
        if data_dicts:
            ages = [int(entry['Age']) for entry in data_dicts]
            min_age = min(ages)
            max_age = max(ages)
        else:
            min_age = 0
            max_age = 0
        
        return {'min_age': min_age, 'max_age': max_age}
   
    # Count the number of rows that satisfy the condition that “age is 28 and Gender is Female”
    def count_rows_with_condition(self):
        data_dicts = self.read_csv()
        count = sum(1 for entry in data_dicts if entry['Age'] == '28' and entry['Gender'] == 'Female')
        return {'total_rows': count}

data_obj = DataAnalysis('<file_path>')
print(data_obj.calc_avg_salary())
print(data_obj.calc_min_max_age())
print(data_obj.count_rows_with_condition())
