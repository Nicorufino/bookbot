from stats import count_words
from stats import count_characters

def main():
    book = get_book_text("/home/rufi/workspace/github.com/nicorufino/bookbot/books/frankenstein.txt")
    num_words = count_words(book)
    print(f"{num_words} words found in the document")
    print(count_characters(book))

def get_book_text(path: str):
    with open(path) as f:
        return f.read()
    
main()