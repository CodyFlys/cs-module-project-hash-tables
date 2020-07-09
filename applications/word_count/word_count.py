# def word_count(s):
#     if len(s) == 0:
#         return {}
#     bad = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "'", "\\"]
#     for i in bad:
#         if i in s:
#             s = s.replace(i, "")
#     myDictionary = {}
#     answer = s.lower()
#     answer = answer.split()
#     counter = 1
#     for each in answer:
#         if each in myDictionary:
#             myDictionary[each] += 1
#         else:
#             myDictionary[each] = counter
#     return myDictionary

def word_count(s):
    # lowercase (s) and store it as answer
    answer = s.lower()
    # make a dictionary which is empty {}
    myDictionary = {}
    # make a bad set of chars to ignore
    bad = '":;,.-+=/\|[]{}()*^&'
    # for every character in our answer(our string)
    for char in answer:
        # check if the character is in the bad set
        if char in bad:
            # if it is in the bad set, we can use replace to override the answer
            # and replace the char with a empty spot. ("")
            answer = answer.replace(char, "")

    # this will split the answer up and store it as words like "Hello" "Cat"
    words = answer.split()
    # for every word in sentence
    for word in words:
        # check if each word is not in dictionary
        if word not in myDictionary:
            # if it isn't, we set word = 1
            myDictionary[word] = 1
        else:
            # if it is it will increment += 1 counting.
            myDictionary[word] += 1
    # return the dictionary
    return myDictionary

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))