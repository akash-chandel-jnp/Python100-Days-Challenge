'''You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

Example Input
What is the Airspeed Velocity of an Unladen Swallow?
Example Output
{
'What': 4,
'is': 2,
'the': 3,
'Airspeed': 8,
'Velocity': 8,
'of': 2,
'an': 2,
'Unladen': 7,
'Swallow?': 8
}
Hint
Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.

You can get a list of the words in a string by using the .split() method: https://www.w3schools.com/python/ref_string_split.asp

To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.'''

# ============================================================ SOLUTION ===================================================
sentence = "The capital of India is NewDelhi but it is one of the most poluted city in the world"
words_list = sentence.split()
print(words_list)
words_dict = {word:len(word) for word in words_list}
print(words_dict)