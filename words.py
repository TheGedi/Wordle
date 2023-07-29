def main():
    file_path = "words.txt"
    o_file_path = "valid_words.txt"
    five_letters = []

    with open(file_path, "r") as f:
        for line in f.readlines():
            words = line.strip()
            five_letters.append(words)

    with open(o_file_path, "w") as f:
        for word in five_letters:
            f.write(word + "\n")


if __name__ == "__main__":
    main()