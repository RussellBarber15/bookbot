from stats import count_words
from stats import get_char_count
from stats import get_sorted_dicts
import sys

# takes path to file and returns the text in the file as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    #check if path was passed
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    #gather stats
    book_text_path = sys.argv[1]
    book_text = get_book_text(book_text_path)
    num_words = count_words(book_text)
    frequency = get_char_count(book_text)
    sorted_chars = get_sorted_dicts(frequency)
    #display
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_text_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
main()
    
