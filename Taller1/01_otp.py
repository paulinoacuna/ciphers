def textToNumbers(text):
    numbers = []
    for char in text.upper():
        if char.isalpha():
            number = ord(char) - ord('A')
            numbers.append(number)
    return numbers


def numbersToText(numbers):
    text = ""
    for num in numbers:
        character = chr(num + ord('A'))
        text += character
    return text

def encrypt(plaintext, key):
    plaintextNums = textToNumbers(plaintext)
    keyNums = textToNumbers(key)

    if len(plaintextNums) != len(keyNums):
        raise ValueError("La longitud de la clave debe ser igual a la del mensaje")

    ciphertextNums = []
    for p, k in zip(plaintextNums, keyNums):
        encrypted_num = (p + k) % 26
        ciphertextNums.append(encrypted_num)

    return numbersToText(ciphertextNums)

def decrypt(ciphertext, key):
    ciphertextNums = textToNumbers(ciphertext)
    keyNums = textToNumbers(key)

    if len(ciphertextNums) != len(keyNums):
        raise ValueError("La longitud de la clave debe ser igual a la del texto cifrado")

    plaintextNums = [] 
    for c, k in zip(ciphertextNums, keyNums):
        decrypted_num = (c - k) % 26
        plaintextNums.append(decrypted_num)

    return numbersToText(plaintextNums)

def main():

    plaintext = input("Ingrese el mensaje a cifrar: ")
    key = input("Ingrese la clave: ")

    ciphertext = encrypt(plaintext, key)
    print("Mensaje cifrado:", ciphertext)

    ciphertextInput = input("Ingrese el mensaje cifrado: ")
    keyInput = input("Ingrese la clave: ")

    decryptedMessage = decrypt(ciphertextInput, keyInput)
    print("Mensaje descifrado:", decryptedMessage)

if __name__ == "__main__":
    main()