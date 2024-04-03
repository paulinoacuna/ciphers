def encrypt(plaintext, k):
    ciphertext = ''
    for char in plaintext.upper():
        if  char.isalpha():
            number = ord(char)
            number = (number - ord('A') + k) % 26 + ord('A')
            ciphertext += chr(number)
        else:
            ciphertext += char
    return ciphertext

def decrypt(texto_cifrado, k):
    return encrypt(texto_cifrado, -k)

def main():
    plaintext = input("Introduce el mensaje a cifrar: ")
    k = int(input("Introduce el parámetro k para cifrar: "))

    ciphertext = encrypt(plaintext, k)
    print("Mensaje cifrado:", ciphertext)

    ciphertextInput = input("Introduce el mensaje cifrado a descifrar: ")
    kInput = int(input("Introduce el parámetro k para descifrar: "))

    decryptedMessage = decrypt(ciphertextInput, kInput)
    print("Mensaje descifrado:", decryptedMessage)

if __name__ == "__main__":
    main()