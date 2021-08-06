def characterCount(input_string):
    final_string = ""
    trimmed_string = "".join(input_string.split())

    for character in trimmed_string:
        if character.isdigit():
            continue
        if character in final_string:
            continue
        counter = trimmed_string.count(character)
        final_string += character + str(counter)

    return final_string

input_string = "aaa b ??c12"
print(characterCount(input_string))

#TEST SCENARIOS
    #Verify that the output is correct by inputting string with letters only
    #Verify that the white spaces are not counted by inputting string with white spaces
    #Verify that the numbers are skipped by inputting string that contains numbers
    #Verify that the output is correct by inputting string that contains special characters
