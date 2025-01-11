def count_words(str):
    str_list = str.split()
    return len(str_list)

def count_characters(str):
    count = {}
    for c in str.lower():
        if c not in count:
            count[c] = 0

        count[c] += 1
    
    return count

def sort_desc(my_dict):
    return dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

def main():
    book = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        num_chars = count_characters(file_contents)

    print(f"--- Begin report of {book} ---")
    
    print(f"{num_words} found in the document")
    for c in sort_desc(num_chars):
        if c.isalpha():
            print(f"The '{c}' character was found {num_chars[c]} times")

    print("--- End report ---")

main()