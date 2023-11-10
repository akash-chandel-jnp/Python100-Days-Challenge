# # one way to csv data into list , but it still have the comma separated values
# with open('weather_data.csv','r') as w_data:
#     data = w_data.readlines()
#     print(data)


# # another way is to use  inbuilt csv module in python
# import csv
# with open('weather_data.csv', 'r') as w_data:
#     data = csv.reader(w_data) # this will an object having rows in the form of a list
#     # print each rows in this object
#     for row in data:
#         print(row)

''' Result will be like below.
['day', 'temp', 'condition']
['Monday', '12', 'Sunny']
['Tuesday', '14', 'Rain']
['Wednesday', '15', 'Rain']
['Thursday', '14', 'Cloudy']
['Friday', '21', 'Sunny']
['Saturday', '22', 'Sunny']
['Sunday', '24', 'Sunny']
'''
#
# # Challenge : create a list called temparatures[] which contains all the temparatures
# temperature = []
# with open('weather_data.csv', 'r') as w_data:
#     data = csv.reader(w_data)
#     for row in data:
#         temp_value = row[1]
#         if temp_value != 'temp' :
#             temperature.append(int(temp_value))
# print(temperature)

# Still this is a lot of work just to do simple task such as get the temp data
# There is a better way of working with csv data. which is using PANDA library

import pandas

data = pandas.read_csv('weather_data.csv')  # this is a dataframe
# print(data)

# print(data.to_dict())
# print(data.dtypes)

# In pandas every column is a series and the whole data(sheet) is a dataframe


# How to get hold of any column (series) in panda:
# step 1: first create a data frame of the given data using -->  pandas.read_csv('file_path) --> then save it under a variable name
data1 = pandas.read_csv('weather_data.csv')
# step 2: use 'column name inside square brackets  after df name to access columns:
# print(data1['day'])
print(data1.day)  # This also works as df creates attributes of the first rows names

print(type(data['temp']))  # data['temp'] is a series

temp_list = data['temp'].to_list()  # converts a series(a column) into a actual list
print(temp_list)

# chanllenge : Find the average temp of all the temperatures
# method 1: using python sum function
temp_sum = sum(temp_list)
avg_temp = round(temp_sum / len(temp_list), 2)
print(avg_temp)

# Using panda mean function:
temp_mean = data[
    'temp'].mean()  # first get access to the column whose means is to be found, then use mean() function in pandas.
print(temp_mean)

# Challenge : Find the max temp using pandas function
# step 1 get hold of the series and then on it apply the required function:
temp_max = data['temp'].max()
print(temp_max)

# How to get Row of data : df[condition for row] -> example : print the row for which day is Monday : print(data[data.day == 'Monday'])
print("\nRow having day as 'Monday")
print(data[data.day == 'Monday'])

# Challenge : Print the row to which has the highest temp :
# 1) find the highest temp
max_temp = data['temp'].max()
# 2)  use this to get the row having temp as max_temp
print("\nRow having max Temp is : ")
print(data[data.temp == max_temp])
