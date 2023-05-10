# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
new_dict = {row.letter: row.code for index, row in nato_data_frame.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = "thomas"
name_list = [name.upper() for name in user_name]
nato_spelling = [new_dict[letter] for letter in name_list if letter in list(new_dict.keys())]

print(nato_spelling)
