def get_words(text):
    words = text.split()
    return words

def count_words(text):
    number_of_words = len(get_words(text))
    return number_of_words

characters = {}
def count_characters(text):
    for char in text.lower():
        if char not in characters:
            characters[f"{char}"] = 1
        else:
            characters[f"{char}"] = characters[f"{char}"] + 1
    return characters