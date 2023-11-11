import pandas

data = pandas.read_csv('squirrel_data.csv')   # creating dataframe from csv file
# print(data)

# Now from the above data frame select the column 'Primary Fur Color' :
list_of_primary_fur_colour =  data["Primary Fur Color"].to_list()
print(list_of_primary_fur_colour)

# Now from the above color list find how many times a color is repeated
dict_colors ={}
for color in list_of_primary_fur_colour:
    #if it is already in the dict then just increase the count by 1
    if color in dict_colors:
        dict_colors[color] += 1
    # if color is not already in the dict then add this color in the dict
    else:
        dict_colors[color] = 1

print(dict_colors)
print(pandas.to)
