def decrypt(grid_size, rotation_direction, holes, encrypted_message):
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    if rotation_direction == 1:
        num_rotations = 4 
    else:
        num_rotations = 2 

    encrypted_index = 0
    for _ in range(num_rotations):
        for row in range(grid_size):
            for col in range(grid_size):
                if (row, col) in holes:
                    grid[row][col] = encrypted_message[encrypted_index]
                    encrypted_index += 1

        if rotation_direction == 1:
            holes = rotate_anticlockwise(holes)
        else:
            holes = rotate_clockwise(holes)

    decrypted_message = ''
    for row in grid:
        decrypted_message += ''.join(row)

    return decrypted_message

def encrypt(grid_size, rotation_direction, holes, message):
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    hole_index = 0

    for i in range(4):
        for row in range(grid_size):
            for col in range(grid_size):
                if (row, col) in holes:
                    if hole_index < len(message):
                        grid[row][col] = message[hole_index]
                        hole_index += 1

        if rotation_direction == 1:
            grid = rotate_clockwise(grid)
        else:
            grid = rotate_anticlockwise(grid)

    encrypted_message = ''
    for row in grid:
        encrypted_message += ''.join(row)

    return encrypted_message

def rotate_clockwise(grid):
    return [list(row) for row in zip(*grid[::-1])]

def rotate_anticlockwise(grid):
    return [list(row) for row in zip(*grid)][::-1]

def main():
    grid_size = int(input("Enter grid size: "))
    rotation_direction = int(input("Enter rotation direction (1 for clockwise, 0 for anticlockwise): "))
    holes_input = input("Enter holes as row,column pairs separated by spaces (e.g., '0,0 1,1'): ")
    holes = [(int(pair.split(',')[0]), int(pair.split(',')[1])) for pair in holes_input.split()]
    message = input("Enter message: ")

    mode = input("Enter 1 to decrypt or any other key to encrypt: ")

    if mode == "1":
        decrypted_message = decrypt(grid_size, rotation_direction, holes, message)
        print("Decrypted message:", decrypted_message)
    else:
        encrypted_message = encrypt(grid_size, rotation_direction, holes, message)
        print("Encrypted message:", encrypted_message)

if __name__ == "__main__":
    main()
