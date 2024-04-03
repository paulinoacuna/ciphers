def generateMatrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = ""

    key = key.replace(" ", "")
    key = ''.join(dict.fromkeys(key))

    for char in key.upper():
        if char not in matrix:
            matrix += char

    for char in alphabet:
        if char not in matrix:
            matrix += char

    return matrix

def playfairEncrypt(message, matrix):

    message = message.replace(" ", "").upper()
    messagePairs = [message[i:i+2] for i in range(0, len(message), 2)]

    # Añadir 'X' si hay una letra solitaria al final
    if len(messagePairs[-1]) == 1:
        messagePairs[-1] += 'X'

    cipherText = ""
    for pair in messagePairs:
        char1, char2 = pair[0], pair[1]
        row1, col1 = divmod(matrix.index(char1), 5)
        row2, col2 = divmod(matrix.index(char2), 5)

        if row1 == row2:  # fila
            cipherText += matrix[row1 * 5 + (col1 + 1) % 5]
            cipherText += matrix[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:  # columna
            cipherText += matrix[((row1 + 1) % 5) * 5 + col1]
            cipherText += matrix[((row2 + 1) % 5) * 5 + col2]
        else:  # ninguna
            cipherText += matrix[row1 * 5 + col2]
            cipherText += matrix[row2 * 5 + col1]

    return cipherText


def playfairDecrypt(message, matrix):

    message = message.upper()
    messagePairs = [message[i:i+2] for i in range(0, len(message), 2)]

    plainText = ""
    for pair in messagePairs:
        char1, char2 = pair[0], pair[1]
        row1, col1 = divmod(matrix.index(char1), 5)
        row2, col2 = divmod(matrix.index(char2), 5)

        if row1 == row2:  # fila
            plainText += matrix[row1 * 5 + (col1 - 1) % 5]
            plainText += matrix[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:  # columna
            plainText += matrix[((row1 - 1) % 5) * 5 + col1]
            plainText += matrix[((row2 - 1) % 5) * 5 + col2]
        else:   # ninguna
            plainText += matrix[row1 * 5 + col2]
            plainText += matrix[row2 * 5 + col1]

    return plainText

def print_matrix(matrix):
    for i in range(5):
        print(" ".join(matrix[i*5:i*5+5]))


def main():
    mode = int(input("Ingrese 0 para encriptar o 1 para desencriptar: "))
    message = input("Ingrese el mensaje a cifrar: ")
    key = input("Ingrese la clave: ")

    matrix = generateMatrix(key)
    print("Matriz generada:")
    for i in range(5):
        print(" ".join(matrix[i*5:i*5+5]))

    if mode == 0:
        cipherText = playfairEncrypt(message, matrix)
        print("Mensaje cifrado:", cipherText)

    elif mode == 1: 
        plainText = playfairDecrypt(message, matrix)
        print("Mensaje descifrado:", plainText)


if __name__ == "__main__":
    main()
