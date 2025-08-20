README
File Read & Write Challenge with Error Handling
This project demonstrates basic file reading and writing in Python, including error handling and simple content modification.

How It Works
Prompts the user to enter the name of a text file to read.
Reads the content of the specified file.
Modifies the content by converting all text to uppercase.
Writes the modified content to a new file, preserving the original extension and appending _modified to the filename.
Handles errors such as missing files or read/write issues gracefully.
Usage
Place your input text file in the project directory.

Run the script:

Enter the filename when prompted (e.g., example.txt).

The modified file will be saved as example_modified.txt (or with the same extension as the input file).

Example
If you have a file named notes.txt:

Run the script and enter notes.txt.
The script creates notes_modified.txt with all content in uppercase.
Requirements
Python 3.x
Notes
The script only modifies the content by converting it to uppercase. You can change the modify_content function in index.py to implement other modifications.
Handles file not found and other I/O errors with user-friendly messages.
