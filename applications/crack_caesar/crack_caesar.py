with open('ciphertext.txt','r') as f_open:
    data = f_open.read()

myKey = {
    "H": "A",
    "R": "F",
    "I": "K",
    "X": "P",
    "A": "U",
    "S": "Z",
    "Z": "B",
    "J": "G",
    "G": "L",
    "K": "Q",
    "M": "V",
    "Y": "C",
    "D": "H",
    "L": "M",
    "U": "R",
    "B": "W",
    "W": "D",
    "P": "I",
    "C": "N",
    "N": "S",
    "Q": "X",
    "O": "E",
    "T": "J",
    "E": "O",
    "F": "T",
    "V": "Y"
}

def decoder(textFile):
    newText = textFile.split()
    for each in range(0, len(textFile)):
        for i in myKey:
            if i in textFile:
                answer = textFile.replace(i, myKey[i])
    return answer

print(decoder(data))