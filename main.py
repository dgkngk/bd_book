from stats import word_counter, char_counter, char_lister

import sys


def get_book_text(bookpath):
    with open(bookpath, 'r') as file:
        return file.read()
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    bookpath = sys.argv[1]

    print(f"============ BOOKBOT ============\nAnalyzing book found at {bookpath}...")
    book_text = get_book_text(bookpath)
    num_words = word_counter(book_text)
    num_chars = char_lister(char_counter(book_text))
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ch_dict in num_chars:
        print(f"{ch_dict['char']}: {ch_dict['count']}")
    print("============= END ===============")
    