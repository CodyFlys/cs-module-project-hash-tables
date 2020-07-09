def no_dups(s):
    # make a answer variable to store words that are no duplicates
    answer = []

    # making a list of words aka (split)
    words = s.split(' ')
    # ["spam", "cat", "spam"]

    # making a dictionary from a list using fromkeys and passing in our list (this should remove dupes)
    dictionary = dict.fromkeys(words)
    # we now have a dictionary of the words without any duplicates in them
    for key in dictionary.keys():
        # for every key(aka word) in the dictionary
        answer.append(key)
        # append the key(aka word) to our answer array that is empty to begin with

        # adds spaced back into the answer
    return ' '.join(answer)




    # for word in words:
    # # check if each word is not in dictionary
    #     if word not in myDictionary:
    #         # if it isn't, we set word = 1
    #         myDictionary[word] = 1
    #     else:
    #         # if it is it will increment += 1 counting.
    #         myDictionary[word] += 1
    # # return the dictionary
    #     for each in myDictionary:
    #         print(each)
    # return myDictionary

    # new_answer = []
    # for word in words:
    #     if word not in new_answer:
    #         new_answer.append(word)
    #     print(new_answer)
        

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))