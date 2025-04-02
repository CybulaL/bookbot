def count_words(insert_text):
    return len(insert_text.split())


def sort_val(single_dikt):
    return single_dikt["num"]


def count_letters(insert_text):
    letter_dictionary={}
    insert_text=insert_text.lower()
    for i in range (0 ,len(insert_text)):
        if letter_dictionary.get(insert_text[i])==None:
            letter_dictionary[insert_text[i]]=1
        else:
            letter_dictionary[insert_text[i]]+=1
        
    return letter_dictionary
    


def letters_sorted(dikt): 
    lista2=[]   
    for iterator in dikt:
        newlist={"character" : iterator, "num": dikt[iterator]}
        lista2.append(newlist) # 2-key dict added to list each time

    lista2.sort(reverse=True, key=sort_val)
    return lista2



