#For example an input of "aaabbbbbccccaacccbbbaaabbbaaa"
#would compress to "3a5b4c2a3c3b3a3b3a"

#if previous index (or next one) is equal to then add to a concatination
# then use len to add the number
# not sure yet how to replicate the letter in ir also

def compressing_a_string ():
    string_input_for_compression = input ("Please enter string for compression: ")
    compressed_string = ""
    final_index_number = len (string_input_for_compression) - 1
    current_concatination = ""
    for index in range (0, len (string_input_for_compression), 1):
        current_character = string_input_for_compression [0]
        if string_input_for_compression [index] == current_character:
            current_concatination += string_input_for_compression [index]
        else:
            location = index
            break
    number_in_current_concatination = len (current_concatination)
    compressed_string += (f"{number_in_current_concatination}{current_character}")
    while final_index_number != index:
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
    return compressed_string

print (compressing_a_string ())