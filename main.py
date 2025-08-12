from stats import get_num_chars, get_num_words, sort_chars
import sys


def get_book_text(filepath):
    """
    Returns the text in a file
    """
    with open(filepath) as f:
        return f.read()
    return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    num_words = get_num_words(get_book_text(filepath))
    sorted_chars = sort_chars(get_num_chars(get_book_text(filepath)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")


main()
