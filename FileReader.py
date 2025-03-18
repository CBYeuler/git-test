import csv

# List of punctuation characters
lookFor = [".", ",", "!", "?", "(", ")", "[", "]", "{", "}"]

words_data = []   # Stores words (without punctuation)
punctuation_data = []  # Stores punctuation only

with open("test.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    
    for row in reader:
        cleaned_row = []
        punctuations_row = []
        
        for cell in row:
            words_only = ''.join(char for char in cell if char not in lookFor)  # Remove punctuation
            punctuations_only = ''.join(char for char in cell if char in lookFor)  # Keep only punctuation
            
            if words_only.strip():  # Avoid empty strings
                cleaned_row.append(words_only)
            
            if punctuations_only.strip():  # Avoid empty strings
                punctuations_row.append(punctuations_only)

        words_data.append(cleaned_row)  # Store clean words
        punctuation_data.append(punctuations_row)  # Store punctuation

# Write cleaned words to output.csv
with open("output.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(words_data)

# Write extracted punctuation to punctuation.csv
with open("punctuation.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(punctuation_data)

print("Words saved to 'output.csv', Punctuation saved to 'punctuation.csv'.")

