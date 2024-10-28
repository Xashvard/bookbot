def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words_in_book(text)
    letters = letter_count(text)
    sorted_letter_count = create_report(letters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print()

    for item in sorted_letter_count:
        if not item["letter"].isalpha():
            continue
        print(f"The {item['letter']} character was found {item['count']} times")
    
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words_in_book(btext):
    length = btext.split()
    return len(length)

def letter_count(btext):
    chars = {}
    converted_text = btext.lower()
    for c in converted_text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
    
def sort_on(x):
    return x["count"]

def create_report(dict):
    dict_list = [{"letter": key, "count": value} for key, value in dict.items()]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

main()