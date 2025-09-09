def main():
    print("📄 Simple File Modifier with Error Handling")

    filename = input("Enter the name of the file to read: ").strip()

    if not filename:
        print("[Error] Filename cannot be empty.")
        return

    try:
        # Read the file
        with open(filename, 'r') as file:
            lines = file.readlines()
        if not lines:
            modified = [line.strip().upper() + '\n' for line in lines if line.strip()]

        # Write to new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified)

        print(f"[Success] Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("[Error] File not found.")
    except PermissionError:
        print("[Error] You don't have permission to read this file.")
    except Exception as e:
        print(f"[Error] Something went wrong: {e}")

if __name__ == "__main__":
    main()
