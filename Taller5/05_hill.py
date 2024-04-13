def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m

def matrix_modinv(matrix, mod):
    n = len(matrix)
    determinant = det(matrix, n) % mod
    adjoint_matrix = adjoint(matrix)
    inv_det = modinv(determinant, mod)
    inverse_matrix = [[((inv_det * adjoint_matrix[i][j]) % mod + mod) % mod for j in range(n)] for i in range(n)]
    return inverse_matrix

def det(matrix, n):
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for i in range(n):
            determinant += ((-1) ** i) * matrix[0][i] * det(submatrix(matrix, 0, i), n - 1)
        return determinant

def submatrix(matrix, row, col):
    return [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]

def adjoint(matrix):
    n = len(matrix)
    adjoint_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sign = 1 if (i + j) % 2 == 0 else -1
            adjoint_matrix[j][i] = sign * det(submatrix(matrix, i, j), n - 1)
    return adjoint_matrix

def get_matrix_from_input():
    print("Enter the elements of the matrix (one row at a time):")
    rows = int(input("Number of rows: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} separated by space: ").split()))
        matrix.append(row)
    return matrix

def encrypt(message, key):
    mod = 26
    key_mod_inv = matrix_modinv(key, mod)
    encrypted_text = ""
    for i in range(0, len(message), 2):
        char1 = ord(message[i]) - ord('A')
        char2 = ord(message[i + 1]) - ord('A')
        result = [0, 0]
        for j in range(2):
            result[j] += key[j][0] * char1 + key[j][1] * char2
            result[j] %= 26
        encrypted_text += chr(result[0] + ord('A')) + chr(result[1] + ord('A'))
    return encrypted_text

def decrypt(ciphertext, key):
    mod = 26
    key_mod_inv = matrix_modinv(key, mod)
    decrypted_text = ""
    for i in range(0, len(ciphertext), 2):
        char1 = ord(ciphertext[i]) - ord('A')
        char2 = ord(ciphertext[i + 1]) - ord('A')
        result = [0, 0]
        for j in range(2):
            result[j] += key_mod_inv[j][0] * char1 + key_mod_inv[j][1] * char2
            result[j] %= 26
        decrypted_text += chr(result[0] + ord('A')) + chr(result[1] + ord('A'))
    return decrypted_text

def main():
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
    if choice == 'E':
        plaintext = input("Enter the plaintext message: ").upper().replace(" ", "")
        key = get_matrix_from_input()
        encrypted_text = encrypt(plaintext, key)
        print("Encrypted message:", encrypted_text)
    elif choice == 'D':
        ciphertext = input("Enter the ciphertext: ").upper().replace(" ", "")
        key = get_matrix_from_input()
        decrypted_text = decrypt(ciphertext, key)
        print("Decrypted message:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()
