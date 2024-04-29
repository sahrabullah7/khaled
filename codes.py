def char_to_baudot(char):  # define function for char to baudot
    baudot_code = {  # dictionary
        ' ': '00000', 'A': '00011', 'B': '11010', 'C': '10010', 'D': '10100', 'E': '01000', 'F': '11001',
        'G': '10110', 'H': '01101', 'I': '00110', 'J': '11110', 'K': '11011', 'L': '00101', 'M': '10011',
        'N': '10000', 'O': '01110', 'P': '11101', 'Q': '10111', 'R': '01011', 'S': '01100', 'T': '00100', 
        'U': '11100', 'V': '11000', 'W': '01111', 'X': '10101', 'Y': '01010', 'Z': '10001'
    }
    return baudot_code.get(char.upper(), '')  # empty string for characters/ uppercase to char/ (.get) gets the value of the key
