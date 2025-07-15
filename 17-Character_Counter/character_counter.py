def count_character(sentence: str) -> int:
    return len(sentence.replace(" ", ""))


main_loop = True
while main_loop:
    user_input = input("Input your sentense or command : ").strip()

    if user_input.lower() in ["exit", "quit", "q", "out", "leve"]:
        main_loop = False
    else:
        print(f"Character count (excluding spaces): {count_character(user_input)}")

