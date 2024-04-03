def encrypt(plaintext, key):
    ciphertext = ''
    key = key.upper()
    keyIndex = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[keyIndex]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            keyIndex = (keyIndex + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    key = key.upper()
    keyIndex = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[keyIndex]) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            keyIndex = (keyIndex + 1) % len(key)
        else:
            plaintext += char
    return plaintext

def main():
    plaintext = input("Introduce el mensaje a cifrar: ")
    # t = int(input("Introduce el parámetro j para cifrar: "))
    key = input("Ingresa la clave: ").upper()

    ciphertext = encrypt(plaintext, key)
    print("Mensaje cifrado:", ciphertext)
    
    ciphertextInput = input("Introduce el mensaje cifrado a descifrar: ")
    # jInput = int(input("Introduce el parámetro j para descifrar: "))
    keyInput = input("Ingresa la clave: ").upper()

    decryptedMessage = decrypt(ciphertextInput, keyInput)
    print("Texto descifrado:", decryptedMessage)

if __name__ == "__main__":
    main()
    
