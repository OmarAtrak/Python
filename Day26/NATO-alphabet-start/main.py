student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(f'{key} : {value}')
    pass

# print('-' * 20)

import pandas
student_data_frame = pandas.DataFrame(student_dict)


#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(f'{index} : {row}')
    #Access row.student or row.score
    # print(f'{index}. {row.student} : {row.score}')
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_phonetic_alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabet_data_frame.iterrows()}
# print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").replace(" ", "").upper()
list = [dict[letter] for letter in word]
print(list)

