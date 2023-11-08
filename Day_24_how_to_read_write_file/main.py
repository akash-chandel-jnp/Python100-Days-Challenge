# # file = open("my_file.txt")
# with open("my_file.txt") as file: # with keyword is used to automatically close the file once its work is over
#     content = file.read()
#     print(content)
# # file.close()


# how to write a file by deleting the previous content of the file : use mode = 'w'  : i.e. write
with open("my_file.txt", mode='w') as file:  # if file does not exist , then it will be automatically created
    file.write("this is the new text to be added by deleting the previous")


# how to write(adding ) a file by NOT deleting the previous content of the file : use mode = 'a'  : i.e. append
with open("my_file.txt", mode='a') as file:  # if file does not exist , then it will be automatically created
    file.write("\nthis is the text to be append only without deleting")