def modify_content(text):
    # Example modification: convert to uppercase and add line numbers
    lines = text.splitlines()
    return "\n".join(f"{i+1}: {line.upper()}" for i, line in enumerate(lines))

def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as infile:
            original_content = infile.read()
            print("✅ File read successfully.")

        modified_content = modify_content(original_content)

        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)
            print(f"✅ Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: Permission denied. You don't have access to read/write this file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
