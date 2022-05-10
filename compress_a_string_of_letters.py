#For example an input of "aaabbbbbccccaacccbbbaaabbbaaa"
#would compress to "3a5b4c2a3c3b3a3b3a"

#if previous index (or next one) is equal to then add to a concatination
# then use len to add the number
# not sure yet how to replicate the letter in ir also


string_input_for_compression = input ("Please enter string for compression: ")

number_in_string = len(string_input_for_compression) - 1
print (number_in_string)


first_concat = ""
first_letter = ""
location = ""
for index in range (0, len (string_input_for_compression), 1):
    first_letter = string_input_for_compression [0]
    if string_input_for_compression [index] == first_letter:
        first_concat += string_input_for_compression [index]
    else:
        location = index
        break
number_in_first_concat = len (first_concat)
print (f"{number_in_first_concat}{first_letter}")

second_concat = ""
for index in range (location, len (string_input_for_compression), 1):
    first_letter = string_input_for_compression [location]
    if string_input_for_compression [index] == first_letter:
        second_concat += string_input_for_compression [index]
    else:
        location = index
        break
number_in_second_concat = len (second_concat)
print (f"{number_in_second_concat}{first_letter}")


#now I need to create a loop that runs through this code indefintely until there are no more characters in the string.



while number_in_string != location:
    current_concatination = ""
    for index in range (location, len(string_input_for_compression), 1):
        first_letter = string_input_for_compression [location]
        if string_input_for_compression [index] == first_letter:
            current_concatination += string_input_for_compression [index]
        else:
            location = index
            break
    number_in_current_concat = len (current_concatination)
    print (f"{number_in_current_concat}{first_letter}")




def compressing_a_string ():
    string_input_for_compression = input ("Please enter string for compression: ")
    compressed_string = ""
    final_index_number = ""
    location = 0
    while final_index_number != location:
        current_concatination = ""
        number_in_current_concatination = ""
        for index in range (location, len (string_input_for_compression), 1):
            current_character = string_input_for_compression [location]
            if string_input_for_compression [index] == current_character:
                current_concatination += string_input_for_compression [index]
            else:
                location = index
                break
        number_in_current_concatination = len (current_concatination)
        compressed_string += (f"{number_in_current_concatination}{current_character}")
    current_concatination = ""
    number_in_current_concatination = ""
    final_index_number = len(string_input_for_compression[index-1])
    for index in range (location, len (string_input_for_compression), 1):
        current_character = string_input_for_compression [location]
        if string_input_for_compression [index] == current_character:
            current_concatination += string_input_for_compression [index]
        else:
            break
    number_in_current_concatination = len (current_concatination)
    compressed_string += (f"{number_in_current_concatination}{current_character}")
    return compressed_string

print (compressing_a_string ())
