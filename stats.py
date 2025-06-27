def get_words(text):
    words = text.split()
    return words

def count_words(text):
    number_of_words = len(get_words(text))
    return number_of_words

def count_characters(text):
    characters = {}
    for char in text.lower():
        if char not in characters:
            characters[f"{char}"] = 1
        else:
            characters[f"{char}"] = characters[f"{char}"] + 1
    return characters

def sort_on(items):
    return items["num"]

def sort_dictionary(dic_characters, count_characters):
    sorted_dictionary = []
    for char in dic_characters:
        if char.isalpha():
            sorted_dictionary.append({"char": char, "num": dic_characters[char]})
    sorted_dictionary.sort(reverse = True, key = sort_on)
    return sorted_dictionary