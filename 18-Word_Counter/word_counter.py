def count_word(sentence: str) -> int:
    return len(sentence.split(" "))


while True:
    user_input = input("Input your sentense or command : ").strip()

    if user_input.lower() in ["exit", "quit", "q", "out", "leve"]:
        break
    else:
        print(f"Word count : {count_word(user_input)}")