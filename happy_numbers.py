#a happy number is a number defined by the following process: starting with any positive integer
#replace the number by the sum of the squares of its digits
#and repeat the process until the number equals 1
#an example of a happy number is 19
#write a method that determines if a number is happy or sad


happy_number = "19"
split_numbers = []
for character in happy_number:
    split_numbers.append (character)
split_numbers = [int(number) for number in split_numbers]
print (split_numbers)
first_number = split_numbers.pop(0)
second_number = split_numbers.pop()
new_number = (first_number * first_number) + (second_number * second_number)
print (new_number)

new_number = str(new_number)
for character in new_number:
    split_numbers.append (character)
split_numbers = [int(number) for number in split_numbers]
print (split_numbers)
