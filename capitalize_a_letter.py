#Write code that takes a string as input and capatilize the first letter of each word.
#Words will be seperated by only one space.
#"hello world" should be output as "Hello World"

input_word_or_phrase = input ("Please enter a word or phrase: ")
input_capitalized = input_word_or_phrase.title ()
print (input_capitalized)

input_word_or_phrase = input_word_or_phrase.capitalize ()
capital_input_string = ""
for index in range (0, len(input_word_or_phrase), 1):
    if input_word_or_phrase[index-1] == " ":
        capital_input_string += input_word_or_phrase[index].capitalize ()
    else:
        capital_input_string += input_word_or_phrase[index]
print (capital_input_string)