morseCodes = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.----.': "'",
    '-.-.--': '!',
    '-..-.': '/',
    '-.--.': '(',
    '-.--.-': ')',
    '.-...': '&',
    '---...': ':',
    '-.-.-.': ';',
    '-...-': '=',
    '.-.-.': '+',
    '-....-': '-',
    '..--.-': '_',
    '.-..-.': '"',
    '...-..-': ',',
    '.--.-.': '@'
}

def decodeBits(bits):
    bits = bits.strip('0')
    min_length = float('inf')
    max_length = 0
    i = 0
    while i < len(bits):
        if bits[i] == '1':
            j = i + 1
            while j < len(bits) and bits[j] == '1':
                j += 1
            min_length = min(min_length, j - i)
            i = j
        else:
            j = i + 1
            while j < len(bits) and bits[j] == '0':
                j += 1
            max_length = max(max_length, j - i)
            i = j
    
    unit_length = min(min_length, max_length)
    
    morse_code = ''
    i = 0
    while i < len(bits):
        if bits[i] == '1':
            j = i + unit_length
            while j < len(bits) and bits[j] == '1':
                j += unit_length
            morse_code += '.' if j - i <= unit_length else '-'
            i = j
        else:
            j = i + unit_length
            while j < len(bits) and bits[j] == '0':
                j += unit_length
            morse_code += ' ' * (j - i)
            i = j
    return morse_code


def decodeMorse(morseCode):
    list1 = morseCode.split('.')
    str1 = ''.join(list1)
    list2 = str1.split('-')
    unit = min(len(string) for string in list2)
    decoded_message = ''
    words = morseCode.split('       ' * unit)
    for word in words:
        letters = word.split(' ' * unit)
        print(letters)
        for letter in letters:
            if letter in morseCodes:
                decoded_message += morseCodes[letter]
        decoded_message += ' '
    return decoded_message.strip()


bits = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
morse_code = decodeBits(bits)
print(morse_code)
decoded_message = decodeMorse(morse_code)
print(decoded_message)
