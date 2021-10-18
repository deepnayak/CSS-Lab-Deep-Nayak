import random, math


def substitution(inputText, shift):
    encrypted = []
    decrypted = []
    for character in inputText:
        if character == ' ':
            encrypted.append('*')
        else:
            encrypted.append(chr(((ord(character) - ord('a') + shift)%26 + ord('a'))))

    for character in encrypted:
        if character == '*':
            decrypted.append(' ')
        else:
            decrypted.append(chr(((ord(character) - ord('a') - shift)%26 + ord('a'))))

    return ("".join(encrypted), "".join(decrypted))

def rot13(inputText):
    encrypted = []
    decrypted = []
    for character in inputText:
        if character == ' ':
            encrypted.append('*')
        else:
            encrypted.append(chr(((ord(character) - ord('a') + 13)%26 + ord('a'))))

    for character in encrypted:
        if character == '*':
            decrypted.append(' ')
        else:
            decrypted.append(chr(((ord(character) - ord('a') - 13)%26 + ord('a'))))

    return ("".join(encrypted), "".join(decrypted))

def vernam(inputText, key):
    ansInput = inputText.split(' ')
    superEnc = []
    superDec = []
    initial = 0
    for x in ansInput:
        buffer = []
        decrypted = []
        encrypted = []
        for character in x:
            buffer.append(ord(character) - ord('a'))

        for index, character in zip(range(len(key[initial:initial+len(x)])), key[initial:initial+len(x)]):
            buffer[index] += (ord(character) - ord('a'))
        encrypted = [chr(element%26 + ord('a')) for element in buffer]

        for keychar, character in zip(key[initial:initial+len(x)], encrypted):
            decrypted.append(chr((ord(character) - ord(keychar))%26 + ord('a')))

        superEnc.append("".join(encrypted))
        superDec.append("".join(decrypted))
        initial += (len(x)+1)

    return (" ".join(superEnc), " ".join(superDec))

def transpose(inputText, permLength, permOg = []):
    matrix = []
    perm1 = permOg
    if len(permOg) == 0:
        perm1 = [i for i in range(permLength)]
        random.shuffle(perm1)
    perm = [(perm1[i], i) for i in range(permLength)]
    perm.sort()
    # key1 = " ".join(perm)
    print("The key is", perm1)
    encrypted = []
    decrypted = []
    
    buffer = []
    cnt = 0
    for x in inputText:
        if cnt < permLength:
            buffer.append(x)
        else:
            matrix.append(buffer)
            cnt = 0
            buffer = []
            buffer.append(x)
        cnt += 1
    while len(buffer) != permLength:
        buffer.append('X')
    matrix.append(buffer)

    print("The matrix is:")
    for x in matrix:
        for y in x:
            print(y, end=' ')
        print()

    for i in perm:
        for j in range(len(matrix)):
            encrypted.append(matrix[j][i[1]])
    
    for i in matrix:
        for j in i:
            if j == 'X':
                break
            decrypted.append(j)
    
    return ("".join(encrypted), "".join(decrypted))

def doubleTranspose(inputText, permLength1, permLength2, permOg1 = [], permOg2 = []):
    matrix = []
    perm1 = permOg1
    if len(permOg1) == 0:
        perm1 = [i for i in range(permLength1)]
        random.shuffle(perm1)
    print("The first key is", perm1)
    perm = [(perm1[i], i) for i in range(permLength1)]
    perm.sort()
    encrypted1 = []
    encrypted2 = []
    decrypted = []
    
    buffer = []
    cnt = 0
    for x in inputText:
        if cnt < permLength1:
            buffer.append(x)
        else:
            matrix.append(buffer)
            cnt = 0
            buffer = []
            buffer.append(x)
        cnt += 1
    while len(buffer) != permLength1:
        buffer.append('X')
    matrix.append(buffer)
    
    print("The matrix is:")
    for x in matrix:
        for y in x:
            print(y, end=' ')
        print()

    for i in perm:
        for j in range(len(matrix)):
            encrypted1.append(matrix[j][i[1]])
    matrix1 = matrix
    matrix = []
    buffer = []
    cnt = 0
    perm1 = permOg2
    if len(permOg2) == 0:
        perm1 = [i for i in range(permLength2)]
        random.shuffle(perm1)
    perm = [(perm1[i], i) for i in range(permLength2)]
    perm.sort()
    # key2 = " ".join(perm)
    print("The second key is", perm1)
    for x in "".join(encrypted1):
        if cnt < permLength2:
            buffer.append(x)
        else:
            matrix.append(buffer)
            cnt = 0
            buffer = []
            buffer.append(x)
        cnt += 1
    while len(buffer) != permLength2:
        buffer.append('X')
    matrix.append(buffer)
    
    print("The matrix is:")
    for x in matrix:
        for y in x:
            print(y, end=' ')
        print()

    for i in perm:
        for j in range(len(matrix)):
            encrypted2.append(matrix[j][i[1]])
    
    for i in matrix1:
        for j in i:
            if j == 'X':
                break
            decrypted.append(j)
    
    return ("".join(encrypted1), "".join(encrypted2), "".join(decrypted))
        




print("~~~~~~~~~~~~~~~~Experiment 1 - Deep Nayak~~~~~~~~~~~~~~~~")
print("Choose the cryptography method:")
print("1. Substitution")
print("2. ROT13")
print("3. Transpose")
print("4. Double Transpose")
print("5. Verman Cipher")

choice = int(input())

if choice == 1:
    print("Enter plain text to be encrypted: ")
    inputText = input()
    print("Enter number of position shift: ")
    shift = int(input())

    (encrypted, decrypted) = substitution(inputText, shift)

    print("The encrypted message is", encrypted)
    print("The decrypted message is", decrypted)

elif choice == 2:
    print("Enter plain text to be encrypted: ")
    inputText = input()

    (encrypted, decrypted) = rot13(inputText)

    print("The encrypted message is", encrypted)
    print("The decrypted message is", decrypted)

elif choice == 3:
    print("Enter plain text to be encrypted: ")
    inputText = input()
    print("Enter the length of the key")
    perm = int(input())

    (encrypted, decrypted) = transpose(inputText=inputText, permLength=perm)

    print("The encrypted message is", encrypted)
    print("The decrypted message is", decrypted)

    
elif choice == 4:
    print("Enter plain text to be encrypted: ")
    inputText = input()
    print("Enter the length of the first key")
    perm1 = int(input())

    print("Enter the length of the second key")
    perm2 = int(input())

    (encrypted1, encrypted2, decrypted) = doubleTranspose(inputText=inputText, permLength1=perm1, permLength2=perm2)

    print("The first encrypted message is", encrypted1)
    print("The second encrypted message is", encrypted2)
    print("The decrypted message is", decrypted)

elif choice == 5:
    print("Enter plain text to be encrypted: ")
    inputText = input()
    print("Enter the key of same length as plain text:")
    key = input()
    while len(inputText) != len(key):
        print("Length of key is not correct\nPlease try again:")
        key = input()

    (encrypted, decrypted) = vernam(inputText, key)

    print("The encrypted message is", encrypted)
    print("The decrypted message is", decrypted)
