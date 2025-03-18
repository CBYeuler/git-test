Overview

This Python script reads a CSV file, extracts punctuation marks separately, and saves them in a new CSV file. It also creates a cleaned version of the original CSV file without punctuation. This is useful for text preprocessing in natural language processing (NLP) or data cleaning tasks.

Features

Reads a CSV file (test.csv).

Extracts punctuation marks from text data.

Saves cleaned text (without punctuation) to output.csv.

Saves extracted punctuation separately in punctuation.csv.

How It Works

Processing Steps

Opens test.csv and reads its content.

Iterates through each cell, separating words and punctuation.

Writes cleaned text (without punctuation) to output.csv.

Writes extracted punctuation to punctuation.csv.

Code Explanation

Key Functions

Punctuation Removal & Extraction

words_only = ''.join(char for char in cell if char not in lookFor)
punctuations_only = ''.join(char for char in cell if char in lookFor)

Removes punctuation from words.

Extracts punctuation separately.

CSV Writing

with open("output.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(words_data)

with open("punctuation.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(punctuation_data)

Writes cleaned words to output.csv.

Writes punctuation marks to punctuation.csv.

Example Usage

Input (test.csv)

Hello, world!
Python is fun. (Really?)

Output (output.csv)

Hello world
Python is fun Really

Output (punctuation.csv)

, !
. ()

Requirements

Python 3.x

CSV file (test.csv) in the same directory

Future Improvements

Add support for custom punctuation lists.

Allow file input from user arguments.

Implement a stopword remover for NLP tasks.

License

This project is free to use and modify.