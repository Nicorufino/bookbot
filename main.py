import sys
from stats import count_words
from stats import count_characters
from stats import sort_char_dictionary


def main(args):
    #Exit the program if the number of arguments is incorrect
    if (len(args) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = get_book_text(args[1])
    num_words = count_words(book)
    sorted_results = sort_char_dictionary(count_characters(book))
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_results:
        if (dictionary["char"].isalpha()):
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")

def get_book_text(path: str):
    with open(path) as f:
        return f.read()
    
main(sys.argv)