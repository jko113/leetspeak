translation = {
    'A': '4',
    'E': '3',
    'G': '6',
    'I': '1',
    'O': '0',
    'S': '5',
    'T': '7',
}

sentence = input("What's your sentence? ")
sentence = sentence.upper()

result = ""

for letter in sentence:
    if letter in translation:
        result += translation[letter]
    else:
        result += letter

print (result.lower())

#eliminated comments