def decrypt_this(text):
    arr = text.split()
    sentence = []
    for word in arr:
        try:
            digit = chr(int(''.join(map(str,[int(s) for s in word if s.isdigit()]))))
        except:
            digit = ''
        try:
            lower = list(''.join(map(str, [str(s) for s in word if s.islower()])))
            lower[0],lower[-1] = lower [-1],lower[0]
            lower = ''.join(lower)
        except:
            lower = ''
        sentence.append(digit+lower)
    return ' '.join(sentence)

def encrypt_this(text):
    arr = text.split()
    sentence = []
    for word in arr:
        word = list(word)
        try:
            word[0], word[1], word[-1] = ord(word[0]), word[-1], word[1]
        except:
            word[0] = ord(word[0])
        sentence.append(''.join(map(str,word)))
    return ' '.join(sentence)


text = "A wise old owl lived in an oak"

"""
tests = [
    ("", ""),
    ("A wise old owl lived in an oak", "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
    ("The more he saw the less he spoke", "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
    ("The less he spoke the more he heard", "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
    ("Why can we not all be like that wise old bird", "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
    ("Thank you Piotr for all your help", "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"),
]

"""

print(encrypt_this(text))