# write code that takes a string as input and returns the string reversed
#"Hello" will be returned as "olleH"

def reverse_user_input ():
    user_input_word_or_phrase = input ("Please enter a word or phrase: ")
    reversed_input_word_or_phrase = ""
    for index in range (len(user_input_word_or_phrase) -1, -1, -1):
        reversed_input_word_or_phrase += user_input_word_or_phrase [index]
    print (reversed_input_word_or_phrase)