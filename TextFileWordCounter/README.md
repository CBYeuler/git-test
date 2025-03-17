Overview

This Python script counts the occurrences of each word in a text file. It reads the file, processes the text by converting it to lowercase, removes punctuation, and tracks word frequency using a dictionary.

Features

Reads a text file and counts the occurrences of each word.

Converts text to lowercase to ensure case-insensitive counting.

Strips common punctuation (e.g., .,!?()[]{}"') to avoid counting words incorrectly.

Uses a dictionary to store word frequencies efficiently.

How It Works

The script opens a text file (text.txt) in read mode.

It reads the file line by line.

Each line is converted to lowercase and split into words.

Punctuation is removed from words.

The script counts occurrences using a dictionary.

Finally, it prints the word frequencies.

Code Explanation

count_words(file_name)

Reads a file and creates a dictionary where:

Keys ==> Words from the file.

Values ==> Count of each word.

Removes punctuation before counting.

Example Usage

filename = "text.txt"
word_frequencies = count_words(filename)

for word, count in word_frequencies.items():
    print(f"{word}: {count}")

Sample Output

If text.txt contains:

Hello world! Hello Python.
Python is great.

The output would be:

hello: 2
world: 1
python: 2
is: 1
great: 1

Requirements

Python 3.x

A text file named text.txt in the same directory

Potential Improvements

Use collections.Counter for a more efficient approach.

Allow users to input a custom file name instead of a hardcoded text.txt.

Filter out common stopwords (e.g., "the", "is", "and").

Write results to a CSV or JSON file for further analysis.

License

This project is free to use and modify.