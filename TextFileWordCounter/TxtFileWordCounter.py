
import os
print("Current Working Directory:", os.getcwd())


def count_words(file_name):
    word_count = {}
    with open(file_name,"r",encoding="utf-8") as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                word = word.strip(".,!?()[]{}\"'")
                if word:
                    word_count[word] = word_count.get(word,0) + 1
            

    return word_count


filename = "text.txt"
word_frequencies = count_words(filename)

# Print word frequencies
for word, count in word_frequencies.items():
    print(f"{word}: {count}")

