def print_fibonacci(n):
    """PART A: Generates and prints the first N terms of the Fibonacci sequence."""
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    a, b = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(str(a))
        a, b = b, a + b

    print("Fibonacci sequence:", " ".join(sequence))


def is_fibonacci(target):
    """PART B: Determines whether a number belongs to the Fibonacci sequence."""
    if target < 0:
        return False

    a, b = 0, 1
    while a < target:
        a, b = b, a + b

    return a == target


def main():
    # --- PART A ---
    n = int(input("How many terms? "))
    print_fibonacci(n)

    print()  # Empty line for formatting

    # --- PART B ---
    target = int(input("Enter a number to check: "))
    if is_fibonacci(target):
        print(f"{target} is a Fibonacci number.")
    else:
        print(f"{target} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()