#A word, phrase, or sequence that reads the same backward as forward
#"madam"
#Write code that takes a user input and checks to see if it is a Palindrome and reports the result

user_input_palindrome_checker = input ("Please enter a word or phrase. We will check if it is written the same forward and backward. ")
reversed_input_palindrome_checker = ""
for index in range (len(user_input_palindrome_checker) -1, -1, -1):
    reversed_input_palindrome_checker += user_input_palindrome_checker [index]
if user_input_palindrome_checker == reversed_input_palindrome_checker:
    print ("Congrats! This is a Palindrome!")
else:
    print ("This is not a Palindrome")