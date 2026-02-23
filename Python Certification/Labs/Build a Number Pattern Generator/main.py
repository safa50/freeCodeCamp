def number_pattern(n):
    # Type check (exclude bool because bool is a subclass of int)
    if not isinstance(n, int) or isinstance(n, bool):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    parts = []
    for number in range(1, n + 1):
        parts.append(str(number))
    return " ".join(parts)

if __name__ == "__main__":
    print(number_pattern(4))    # expected: "1 2 3 4"
    print(number_pattern(1))    # expected: "1"
    print(number_pattern(0))    # expected: "Argument must be an integer greater than 0."
    print(number_pattern(3.5))  # expected: "Argument must be an integer value."
    print(number_pattern(True)) # expected: "Argument must be an integer value."
    print(number_pattern(False))# expected: "Argument must be an integer value."
    print(number_pattern("5"))  # expected: "Argument must be an integer value."
    print(number_pattern(-2))   # expected: "Argument must be an integer greater than 0."
    print(number_pattern(20))   # expected: "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"