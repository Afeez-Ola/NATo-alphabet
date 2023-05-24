import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for index, row in nato_data_frame.iterrows()}


def nato_spelling():
    nato_letters = ""
    try:
        word = input("Enter your word: ").upper()
        nato_letters = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_spelling()
    print(nato_letters)


nato_spelling()
