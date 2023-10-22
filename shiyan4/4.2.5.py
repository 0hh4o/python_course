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
    '...-..-': '$',
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
    
    rate = min(min_length, max_length)
    morse_code = ''
    morseCode = bits.replace('111'*rate, '-').replace('1'*rate, '.').replace('0000000'*rate, '   ').replace('000'*rate, ' ').replace('0'*rate, '')
    return morseCode

def decodeMorse(morseCode):
    morseCode = morseCode.split('   ')
    decodedMessage = []
    for word in morseCode:
        decodedWord = []
        for letter in word.split(' '):
            decodedWord.append(morseCodes[letter])
        decodedMessage.append(''.join(decodedWord))
    return ' '.join(decodedMessage)
bits = '11000000111000011'
morse_code = decodeBits(bits)
print(morse_code)
decoded_message = decodeMorse(morse_code)
print(decoded_message)
