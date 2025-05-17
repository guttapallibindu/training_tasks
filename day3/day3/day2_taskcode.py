# Menu-driven file handling program with basic exception handling

def write_file():
    try:
        filename = input("Enter the filename to write to (e.g., data.txt): ")
        content = input("Enter the content to write (use \\n for new lines): ")
        content = content.replace("\\n", "\n")  

        with open(filename, "w") as file:
            file.write(content + "\n")
        print(f"File '{filename}' written successfully.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to write to the file.")
    except ValueError:
        print("Error: Invalid value while writing to the file.")
    except TypeError:
        print("Error: Type mismatch while writing to the file.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def read_file():
    try:
        filename = input("Enter the filename to read (e.g., data.txt): ")
        with open(filename, "r") as file:
            print("Reading file contents:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except ValueError:
        print("Error: Invalid value while reading the file.")
    except TypeError:
        print("Error: Type mismatch while reading the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_file():
    try:
        filename = input("Enter the filename to append to (e.g., data.txt): ")
        content = input("Enter the content to append (use \\n for new lines): ")
        content = content.replace("\\n", "\n")
        with open(filename, "a") as file:
            file.write(content + "\n")
        print(f"Content appended to '{filename}' successfully.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to append to the file.")
    except ValueError:
        print("Error: Invalid value while appending to the file.")
    except TypeError:
        print("Error: Type mismatch while appending to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    while True:
        print("\nMenu:")
        print("1. Write a file")
        print("2. Read a file")
        print("3. Append a file")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice (1 to 4): "))
            if choice == 1:
                write_file()
            elif choice == 2:
                read_file()
            elif choice == 3:
                append_file()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception:
            print("An unexpected error occurred.")

if __name__ == "__main__":
    main()
