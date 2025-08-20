# index.py
# File Read & Write Challenge with Error Handling

import os

def modify_content(content):
    """Example modification: convert text to uppercase"""
    return content.upper()

def main():
    input_filename = input("Enter the filename to read: ").strip()
    
    # Try to read the file
    try:
        with open(input_filename, 'r', encoding="utf-8") as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
        return
    except Exception as e:
        print(f"❌ Error reading '{input_filename}': {e}")
        return

    # Modify the content
    modified_content = modify_content(content)

    # Preserve original extension, add _modified
    name, ext = os.path.splitext(input_filename)
    output_filename = f"{name}_modified{ext}" if ext else f"{name}_modified.txt"

    # Try to write the modified content
    try:
        with open(output_filename, 'w', encoding="utf-8") as outfile:
            outfile.write(modified_content)
        print(f"✅ Modified content written to '{output_filename}'.")
    except Exception as e:
        print(f"❌ Error writing to '{output_filename}': {e}")

if __name__ == "__main__":
    main()
