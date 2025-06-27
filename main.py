import sys
from stats import count_words
from stats import count_characters
from stats import sort_dictionary

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(sys.argv[1])

    num_words = count_words(text)
    # print(f"{num_words} words found in the document")

    # print(count_characters(text))

    character_list_sorted = sort_dictionary(count_characters(text), num_words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in character_list_sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()