# TODO create a list of all the line(name)
with open('./Input/Names/invited_names.txt') as name_file:
    list_of_names = name_file.readlines()  # readlines() returns the list of all the lines

# Get the content of the sample letter content
with open('./Input/Letters/starting_letter.txt') as start_letter:
    letter_content = start_letter.read()

# Run through the list of the names and keep using these names in the final letter after modifying the names
for i in range(len(list_of_names)):
    #Replace the '\n' in the name in the list generated and also strip for the left or right spaces in the names
    list_of_names[i] = list_of_names[i].replace('\n', '').strip()

    #creating output letters with [name] replaced by actual name
    with open(f"./output/ReadyToSend/letter_to_{list_of_names[i]}" , mode= 'w') as output_letter:
        final_letter_content = letter_content.replace('[name]',list_of_names[i])
        output_letter.write(final_letter_content)



# TODO: Create a letter using starting_letter.txt


# for each name in invited_names.txt


# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
