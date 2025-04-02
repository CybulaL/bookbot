import sys
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents =f.read()

    return file_contents

from stats import count_words
from stats import count_letters
from stats import letters_sorted


def main(bookpath):
    zmienna=get_book_text(bookpath)    
    #print (f"{count_words(zmienna)} words found in the document")
    #print(count_letters(zmienna))
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(zmienna)} total words")
    print("--------- Character Count -------")
    dic_list=letters_sorted(count_letters(zmienna))
    for dic in dic_list:
        if dic["character"].isalpha()==True:
            print(f"{dic["character"]}: {dic["num"]}")




    print("============= END ===============")

arg_list=sys.argv

print(arg_list)

if len(arg_list)==2:
    main(arg_list[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


#main(bookpath)