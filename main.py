def get_noc_from_dict(dict):
    return 1

def create_report_from_list(ls):
    return 1


def create_list_of_dicts(dict):
    list_of_char_dicts = []
    for char in dict:
        list_of_char_dicts.append({char:dict[char]})
    return list_of_char_dicts
    

def unique_char_count(text):
    uniq_char_dict = {}

    for char in text:
        if char != " " and char.isalpha():
            if char.lower() not in uniq_char_dict:
                uniq_char_dict.update({char.lower():1})
            else:
                uniq_char_dict.update({char.lower() : uniq_char_dict[char.lower()]+1})
    return uniq_char_dict
            



def count_words(text):
    words = text.split()
    return len(words)


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(word_count)
        print(unique_char_count(file_contents))




main()

    

