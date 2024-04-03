import math

def calculate_layouts(n):
    if n < 26:
        return 0
    return math.comb(n, 26) * math.factorial(26) * (26 ** (n - 26))

if __name__ == "__main__":
    n = int(input("Enter the number of letters (n): "))
    layouts = calculate_layouts(n)
    print("Number of possible layouts:", layouts)
