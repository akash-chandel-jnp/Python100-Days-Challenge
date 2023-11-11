import pandas
# create a dataframe from scratch

data_dict = {
    "students" : ["Akash", "Anurag" , 'Abhishek' , 'Azam'],
    "scores" : [85, 80, 76,84]
}

# from the above dict create a dataframe:

data = pandas.DataFrame(data_dict)
print(data)

#convert into csv format
data.to_csv('new_data.csv')