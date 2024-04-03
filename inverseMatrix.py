def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def matrix_modinv(matrix, mod):
    n = len(matrix)
    determinant = det(matrix, n) % mod
    if determinant == 0:
        raise Exception('Modular inverse does not exist')
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
    cols = int(input("Number of columns: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} separated by space: ").split()))
        if len(row) != cols:
            print("Error: Number of elements in each row must match the number of columns.")
            return None
        matrix.append(row)
    return matrix

def main():
    mod = int(input("Enter the modulus: "))
    matrix = get_matrix_from_input()
    if matrix is not None:
        try:
            inverse = matrix_modinv(matrix, mod)
            print("Inverse matrix:")
            for row in inverse:
                print(row)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
