def mad_libs():
    print("Let's play Mad Libs!")
    print("Fill in the blanks:\n")

    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    plural_noun = input("Enter a plural noun: ")

    print("\nHere’s your story:")
    print(f"One day, a {adjective} {noun} decided to {verb} at the {place}.")
    print(f"It was quite the sight to see so many {plural_noun} cheering!")

if __name__ == "__main__":
    mad_libs()
