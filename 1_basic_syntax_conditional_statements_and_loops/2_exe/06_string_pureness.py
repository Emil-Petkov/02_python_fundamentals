def check_for_pure_tex(n_lines):
    for _ in range(n_lines):
        current_text = input()

        symbols = [".", ",", "_"]

        if any(symbol in current_text for symbol in symbols):
            print(f"{current_text} is not pure!")
        else:
            print(f"{current_text} is pure.")


n = int(input())
check_for_pure_tex(n)
