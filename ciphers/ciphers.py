class cipher():
    def ceaser(text, key, mode):
        if mode == "encrypt":
            # Initialize an empty string to store the encrypted text
            ciphertext = ""
            # Loop through each character in the plaintext
            for char in text:
                # Check if the character is an alphabet
                if char.isalpha():
                    # Calculate the shifted ASCII value by adding the key
                    shift = ord(char) + key
                    # Check if the character is a lowercase alphabet
                    if char.islower():
                        # If the shifted ASCII value exceeds "z", subtract 26 to wrap around
                        if shift > ord("z"):
                            shift -= 26
                        # Add the shifted character to the ciphertext
                        ciphertext += chr(shift)
                    # Check if the character is an uppercase alphabet
                    elif char.isupper():
                        # If the shifted ASCII value exceeds "Z", subtract 26 to wrap around
                        if shift > ord("Z"):
                            shift -= 26
                        # Add the shifted character to the ciphertext
                        ciphertext += chr(shift)
                # If the character is not an alphabet, add it to the ciphertext as is
                else:
                    ciphertext += char
            # Return the encrypted text
            return ciphertext

        else:
            # Initialize an empty string to store the decrypted text
            plaintext = ""
            # Loop through each character in the ciphertext
            for char in text:
                # Check if the character is an alphabet
                if char.isalpha():
                    # Calculate the shifted ASCII value by subtracting the key
                    shift = ord(char) - key
                    # Check if the character is a lowercase alphabet
                    if char.islower():
                        # If the shifted ASCII value is less than "a", add 26 to wrap around
                        if shift < ord("a"):
                            shift += 26
                        # Add the shifted character to the plaintext
                        plaintext += chr(shift) 
                    # Check if the character is an uppercase alphabet
                    elif char.isupper():
                        # If the shifted ASCII value is less than "A", add 26 to wrap around
                        if shift < ord("A"):
                            shift += 26
                        # Add the shifted character to the plaintext
                        plaintext += chr(shift)
                # If the character is not an alphabet, add it to the plaintext as is
                else:
                    plaintext += char
            # Return the decrypted text
            return plaintext


    def vigenere(text, key, mode):
        if mode == "encrypt":
            # Initialize an empty string to store the encrypted message
            ciphertext = ""
            no_cipher_counter = 0
            # Convert the plaintext into a list of characters
            text_list = list(text)
            # Loop through each character in the plaintext
            for i, c in enumerate(text_list):
                # If the character is an alphabetic character
                if c.isalpha():
                    # Calculate the shift value by converting the key character to uppercase, 
                    # finding its ordinal value, subtracting the ordinal value of 'A', 
                    # and taking the modulo 26 to wrap around the alphabet
                    shift = ord(key[(i - no_cipher_counter) % len(key)].upper()) - ord('A')
                    # If the character is lowercase, add the shift value to its ordinal value 
                    # and convert back to a character
                    if c.islower():
                        ciphertext += chr((ord(c.upper()) - ord('A') + shift) % 26 + ord('a'))
                    else:
                        # If the character is uppercase, add the shift value to its ordinal value 
                        # and convert back to a character
                        ciphertext += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
                # If the character is a digit
                elif c.isdigit():
                    # Add the shift value to its ordinal value 
                    # and convert back to a character
                    ciphertext += chr((ord(c) - ord('0') + shift) % 10 + ord('0'))
                # If the character is not an alphabetic or digit character, simply add it to the ciphertext
                else:
                    ciphertext += c
                    no_cipher_counter += 1
            # Return the encrypted message
            return ciphertext

        else:
            # Initialize an empty string to store the decrypted message
            plaintext = ""
            no_cipher_counter = 0
            # Convert the ciphertext into a list of characters
            text_list = list(text)
            # Loop through each character in the ciphertext
            for i, c in enumerate(text_list):
                # If the character is an alphabetic character
                if c.isalpha():
                    # Calculate the shift value by converting the key character to uppercase, 
                    # finding its ordinal value, subtracting the ordinal value of 'A', 
                    # and taking the modulo 26 to wrap around the alphabet
                    shift = ord(key[(i - no_cipher_counter) % len(key)].upper()) - ord('A')
                    # If the character is lowercase, subtract the shift value from its ordinal value 
                    # and convert back to a character
                    if c.islower():
                        plaintext += chr((ord(c.upper()) - ord('A') - shift) % 26 + ord('a'))
                    else:
                        # If the character is uppercase, subtract the shift value from its ordinal value 
                        # and convert back to a character
                        plaintext += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
                # If the character is a digit
                elif c.isdigit():
                    # Subtract the shift value from its ordinal value 
                    # and convert back to a character
                    plaintext += chr((ord(c) - ord('0') - shift) % 10 + ord('0'))
                # If the character is not an alphabetic or digit character, simply add it to the plaintext
                else:
                    plaintext += c
                    no_cipher_counter += 1
            # Return the decrypted message
            return plaintext



    def rail_fence(text, key, mode):
        if mode == "encrypt":
            # Create 2D list with dimensions key * length of text 
            rails = [[None] * len(text) for _ in range(key)]
            # Initialize rail number and direction as 0 and 1 respectively
            rail_num, direction = 0, 1
            # Iterate over each character in the text
            for i, char in enumerate(text):
                # Assign the character to the current rail
                rails[rail_num][i] = char
                # If the rail number is at the bottom rail, change direction to upward
                if rail_num == 0:
                    direction = 1
                # If the rail number is at the top rail, change direction to downward
                elif rail_num == key - 1:
                    direction = -1
                # Change the rail number based on the direction
                rail_num += direction
            # Flatten the 2D list of rails into a 1D list of characters
            result = [char for rail in rails for char in rail if char]
            # Join the list of characters into a single string
            return "".join(result)

        else:
            # Create a list of empty lists with length equal to the key
            rails = [[] for _ in range(key)]
            # Initialize rail number and direction as 0 and 1 respectively
            rail_num, direction = 0, 1
            # Iterate over the length of the text
            for i in range(len(text)):
                # Append the index of each character to the corresponding rail
                rails[rail_num].append(i)
                # If the rail number is at the bottom rail, change direction to upward
                if rail_num == 0:
                    direction = 1
                # If the rail number is at the top rail, change direction to downward
                elif rail_num == key - 1:
                    direction = -1
                # Change the rail number based on the direction
                rail_num += direction
            # Initialize a list of None with length equal to the length of the text
            result = [None] * len(text)
            # Initialize the count to keep track of the current character in the text
            count = 0
            # Iterate over the rails
            for rail_num in range(key):
                # Iterate over the indices in each rail
                for i in rails[rail_num]:
                    # Assign the corresponding character from the text to the result
                    result[i] = text[count]
                    # Increment the count to get the next character in the text
                    count += 1
            # Join the list of characters into a single string
            return "".join(result)


    def autokey(text, key, mode):
        if mode == "encrypt":
            # The key is generated based on the plaintext
            key = key + text
            # Initialize an empty string to store the encrypted message
            ciphertext = ""
            # Convert the plaintext into a list of characters
            text_list = list(text)
            # Loop through each character in the plaintext
            for i, c in enumerate(text_list):
                # If the character is an alphabetic character
                if c.isalpha():
                    # Calculate the shift value by converting the key character to uppercase, 
                    # finding its ordinal value, subtracting the ordinal value of 'A', 
                    shift = ord(key[i].upper()) - ord('A')
                    # If the character is lowercase, add the shift value to its ordinal value 
                    # and convert back to a character
                    if c.islower():
                        ciphertext += chr((ord(c.upper()) - ord('A') + shift) % 26 + ord('a'))
                    else:
                        # If the character is uppercase, add the shift value to its ordinal value 
                        # and convert back to a character
                        ciphertext += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
                # If the character is a digit
                elif c.isdigit():
                    # Calculate the shift by the ordinal of the key digit, subtracting the ordinal value of '0'
                    shift = ord(key[i]) - ord('0')
                    # Add the shift value to its ordinal value 
                    # and convert back to a character
                    ciphertext += chr((ord(c) - ord('0') + shift) % 10 + ord('0'))
                # If the character is not an alphabetic or digit character, simply add it to the ciphertext
                else:
                    ciphertext += c
            # Return the encrypted message
            return ciphertext

        else:
            # Initialize an empty string to store the decrypted message
            plaintext = ""
            key_len =  len(key)
            # Loop through each character in the ciphertext
            for i, c in enumerate(text):
                # Calculate the shift value by converting the key character to uppercase, 
                # finding its ordinal value, subtracting the ordinal value of 'A', 
                shift = ord(key[i].upper()) - ord('A')
                # If the character is an alphabetic character
                if c.isalpha():
                    # If the character is lowercase, subtract the shift value from its ordinal value 
                    # and convert back to a character
                    if c.islower():
                        plaintext += chr((ord(c.upper()) - ord('A') - shift) % 26 + ord('a'))
                    else:
                        # If the character is uppercase, subtract the shift value from its ordinal value 
                        # and convert back to a character
                        plaintext += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
                # If the character is a digit
                elif c.isdigit():
                    # Calculate the shift by the ordinal of the key digit, subtracting the ordinal value of '0'
                    shift = ord(key[i]) - ord('0')
                    # Subtract the shift value from its ordinal value 
                    # and convert back to a character
                    plaintext += chr((ord(c) - ord('0') - shift) % 10 + ord('0'))
                # If the character is not an alphabetic or digit character, simply add it to the plaintext
                else:
                    plaintext += c
                # If we have processed all characters of the original key, start using the ciphertext as the key
                if i >= key_len - 1:
                    key += plaintext[i - key_len + 1]
            # Return the decrypted message
            return plaintext




    def playfair(text, key, mode):
        if mode == "encrypt":
            # Remove spaces from plaintext and key
            text = text.replace(" ", "")
            # Remove whitespace and convert to uppercase
            text = text.upper().replace("J", "I")
            # Add bogus letter if there are duplicate letters
            text = x_duplicates(text)
            # Add padding if necessary (plaintext length should be even)
            if len(text) % 2 != 0:
                text += "X"
            # Create a 5x5 matrix using the key
            matrix = create_matrix(key)
            ciphertext = ""
            # Iterate over pairs of characters
            for i in range(0, len(text), 2):
                # Get the pair of characters
                a, b = text[i], text[i+1]
                # Find the row and column of each character in the matrix
                row1, col1 = find_char(matrix, a)
                row2, col2 = find_char(matrix, b)
                # Handle characters in the same row
                if row1 == row2:
                    col1 = (col1 + 1) % 5
                    col2 = (col2 + 1) % 5
                # Handle characters in the same column
                elif col1 == col2:
                    row1 = (row1 + 1) % 5
                    row2 = (row2 + 1) % 5
                # Handle all other cases
                else:
                    col1, col2 = col2, col1
                # Add the encrypted characters to the ciphertext
                ciphertext += matrix[row1][col1] + matrix[row2][col2]
            return ciphertext

        else:
            # Remove whitespace and convert to uppercase
            text = text.upper().replace("J", "I")
            key = remove_duplicates(key)
            matrix = create_matrix(key)
            plaintext = ""
            # Iterate over pairs of characters
            for i in range(0, len(text), 2):
                a, b = text[i], text[i+1]
                row1, col1 = find_char(matrix, a)
                row2, col2 = find_char(matrix, b)
                # Handle characters in the same row
                if row1 == row2:
                    col1 = (col1 - 1) % 5
                    col2 = (col2 - 1) % 5
                # Handle characters in the same column
                elif col1 == col2:
                    row1 = (row1 - 1) % 5
                    row2 = (row2 - 1) % 5
                # Handle all other cases
                else:
                    col1, col2 = col2, col1
                plaintext += matrix[row1][col1] + matrix[row2][col2]
            return plaintext


    #the beaufort cipher function
    def beaufort(plaintext, key):
        # Initialize an empty string to store the ciphertext
        ciphertext = ""
        # Initialize a counter to keep track of how many characters are not encrypted
        no_cipher_counter = 0
        # Loop through each character in the plaintext
        for i, char in enumerate(plaintext):
            # Calculate the shift value by taking the ordinal value of the corresponding character 
            # in the key and subtracting the ordinal value of 'A'
            shift = ord(key[(i - no_cipher_counter) % len(key)].upper())
            # If the character is an uppercase letter
            if char.isupper():
                # Encrypt the character by subtracting its ordinal value from the shift value, 
                # taking the result mod 26, and adding the ordinal value of 'A' to get the ciphertext character
                ciphertext += chr((shift - ord(char)) % 26 + ord('A'))
            # If the character is a lowercase letter
            elif char.islower():
                # Encrypt the character by subtracting the uppercase ordinal value of the character from the shift value, 
                # taking the result mod 26, and adding the ordinal value of 'a' to get the ciphertext character
                ciphertext += chr((shift - ord(char.upper())) % 26 + ord('a'))
            # If the character is a digit
            elif char.isdigit():
                # Encrypt the character by subtracting its ordinal value from the shift value, 
                # taking the result mod 10, and adding the ordinal value of '0' to get the ciphertext character
                ciphertext += chr((shift - ord(char)) % 10 + ord('0'))
            # If the character is not an alphabetic or digit character, do not encrypt it
            else:
                ciphertext += char
                no_cipher_counter += 1
        # Return the ciphertext
        return ciphertext


def create_matrix(key):
    # Remove spaces from the key and convert it to uppercase
    key = key.replace(" ", "")
    key = key.upper()
    # Replace "J" with "I" in the key
    key = key.replace("J", "I")
    # Create an empty list to hold the matrix
    matrix = []
    # Remove duplicate characters from the key
    key = remove_duplicates(key)
    # Define the alphabet (excluding "J")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # Add the key to the matrix, one character at a time
    for char in key: 
        # Check if the character is already in the matrix
        if char not in matrix:
            # If not, add it to the matrix
            matrix.append(char)
    # Add the remaining characters from the alphabet to the matrix
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    # Reshape the matrix to a 5x5 grid
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    # Return the completed matrix
    return matrix

def find_char(matrix, char):
    # Find the position of a character in the matrix
    for i, row in enumerate(matrix):
        if char in row:
            j = row.index(char)
            return i, j

# Removes all duplicates from a string while preserving the order of the characters, and returns the result.
def remove_duplicates(s):
    # Create two empty strings to keep track of seen characters and the final result
    seen, result = "", ""
    # Loop through each character in the input string
    for char in s:
        # If the character has not been seen before, add it to both seen and result strings
        if char not in seen:
            seen += char
            result += char
    # Return the final result string with duplicates removed
    return result

#Adds an bugus lettre "x" between consecutive duplicate letters in the text.
def x_duplicates(s):
    result = ""
    prev_char = None
    for char in s:
        if char == prev_char:
            result += "X"
        result += char
        prev_char = char
    return result


texts = {
    "description" : {
        "ceaser": "The Caesar cipher is a simple encryption technique. To use it, start by selecting a shift value for the cipher. Then, take each letter in the message and shift it forward by the specified number of positions in the alphabet",
        "vigenere": "The Vigenere Cipher is a polyalphabetic substitution cipher that makes use of numerous interconnected Caesar ciphers that are based on a word or phrase. The corresponding letter of the key determines the amount by which each letter of the plaintext is moved.",
        "rail_fence": "The Rail Fence Cipher is a transposition cipher that scrambles plaintext by writing it down a number of lines in a zigzag pattern, then reading it back in a different sequence. Its name comes from the zigzag pattern's resemblance to a fence.",
        "autokey": "An autokey cipher is a kind of polyalphabetic substitution cipher that creates a keystream for encryption using a keyword. The first plaintext character is encrypted using the keyword, and the following character is encrypted using that character as part of the key, and so on.",
        "playfair": "The playfair cipher uses a polygraphic substitution method where pairs of letters are encrypted using a square grid or matrix filled with 25 unique letters (I and J are usually combined into a single letter).",
        "beaufort": "The Beaufort cipher is a polyalphabetic substitution cipher, To encrypt a message, the key is repeated over the length of the message, and each letter in the message is shifted backwards by the corresponding letter in the key."
    },

    "key" : {
        "ceaser": "The Ceaser key Must be a number between 1 and 25",
        "vigenere": "The Vigenere key must be a text",
        "rail_fence": "The Rail Fence key must be a number greater than 2",
        "autokey": "The Autokey key must be a text",
        "playfair": "The Playfair key must be a text",
        "beaufort": "The Beaufort key must be a text"
    },
    
    "notes" : {
        "type": "type of cipher you want to use for Encryption",
        "plaintext": 'type the text you want to "encrypt/decrypt"',
        "mode": "Select the mode for encryption or decryption",
    }
}


