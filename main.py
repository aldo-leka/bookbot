from stats import get_num_words, get_chars_usage, sort_usages
import sys

def main(book_path: str):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_usage = get_chars_usage(text)
    sorted = sort_usages(chars_usage)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for usage in sorted:
        if usage["char"].isalpha():
            print(f"{usage["char"]}: {usage["num"]}")
    print("============= END ===============")


def get_book_text(path: str) -> str:
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()

    return file_contents


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

main(book_path)