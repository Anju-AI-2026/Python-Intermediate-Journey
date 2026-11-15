# Text File Word Counter

## 📌 Project Overview

A Python program that reads a text file and generates a text analysis report. It calculates the number of words, characters, characters without spaces, lines, and sentences.

The user can provide the path of any accessible UTF-8 text file.

## ✨ Features

- Reads text files using a user-provided file path.
- Counts total characters.
- Counts characters excluding whitespace.
- Counts words using regular expressions.
- Counts lines and sentences.
- Displays results in a formatted analysis report.
- Handles missing files and permission errors.
- Handles UTF-8 decoding errors and other file-related exceptions.

## 🧠 Concepts Practiced

- Python functions
- File handling
- `pathlib` module
- `re` (regular expressions) module
- Reading files with UTF-8 encoding
- Dictionaries
- List and dictionary processing
- String formatting
- Generator expressions
- Exception handling
- Text processing and analysis

## 🛠️ Technologies Used

- Python 3
- Python standard library

## ▶️ How to Run

Open a terminal in the repository directory and execute:

```bash
python intermediate_python_programs/04_text_file_word_counter.py
```

Enter the path of the text file when prompted.

For example:

```text
Enter the text file path: intermediate_python_programs/sample_text.txt
```

## 📊 Sample Output

```text
========================================
        TEXT FILE WORD COUNTER
========================================
Enter the text file path: sample_text.txt

TEXT ANALYSIS REPORT
----------------------------------------
Characters                    : 120
Characters Without Spaces     : 98
Words                         : 22
Lines                         : 4
Sentences                     : 3
----------------------------------------
```

*Note: The sample counts are illustrative. Actual results depend on the contents of the selected text file.*

## 🎯 Purpose

To develop practical file-handling and text-processing skills using Python's standard library, regular expressions, and exception handling.