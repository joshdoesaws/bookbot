with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    file_contents = file_contents.lower()
    book_length = file_contents.split()
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(len(book_length)) + " words found in this document")
    
    char_dict = {}

    for i in file_contents:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1

    char_list = [{'char': char, 'count': count} for char, count in char_dict.items() if char.isalpha()]
    char_list.sort(reverse=True, key=lambda x: x['count'])
    
    for i in char_list:
        print(f"The '{i['char']}' character was found {i['count']} times")

    print("--- End report ---")

    

