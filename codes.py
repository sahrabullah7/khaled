def char_to_baudot(char):  # define function for char to baudot
    baudot_code = {  # dictionary
        ' ': '00000', 'A': '00011', 'B': '11010', 'C': '10010', 'D': '10100', 'E': '01000', 'F': '11001',
        'G': '10110', 'H': '01101', 'I': '00110', 'J': '11110', 'K': '11011', 'L': '00101', 'M': '10011',
        'N': '10000', 'O': '01110', 'P': '11101', 'Q': '10111', 'R': '01011', 'S': '01100', 'T': '00100', 
        'U': '11100', 'V': '11000', 'W': '01111', 'X': '10101', 'Y': '01010', 'Z': '10001'
    }
    return baudot_code.get(char.upper(), '')  # empty string for characters/ uppercase to char/ (.get) gets the value of the key

def baudot_to_char(baudot):   # define function for baudot to char
    baudot_code = {  # dictionary
        '00000': ' ', '00011': 'A', '11010': 'B', '10010': 'C', '10100': 'D', '01000': 'E', '11001': 'F',
        '10110': 'G', '01101': 'H', '00110': 'I', '11110': 'J', '11011': 'K', '00101': 'L', '10011': 'M',
        '10000': 'N', '01110': 'O', '11101': 'P', '10111': 'Q', '01011': 'R', '01100': 'S', '00100': 'T',
        '11100': 'U', '11000': 'V', '01111': 'W', '10101': 'X', '01010': 'Y', '10001': 'Z'
    }
    return baudot_code.get(baudot, '')  # empty string for baudot codes

def encrypt_phrase(phrase):   #  encrypt the text
    encrypted = ''
    for char in phrase:
        encrypted_char = char_to_baudot(char)
        if encrypted_char:  # a char not found in the dictionary
            encrypted += encrypted_char + ' '
        else:
            encrypted += '[try again] '
    return encrypted.strip()

def decrypt_phrase(encrypted):  # decrypt the encrypted text
    decrypted = ''
    baudot_list = encrypted.split() # get the massage and split it into seperate words 
    for baudot in baudot_list:
        decrypted_char = baudot_to_char(baudot)
        if decrypted_char: # a char not found in the dictionary
            decrypted += decrypted_char
        else:
            decrypted += '[try again]'
    return decrypted
