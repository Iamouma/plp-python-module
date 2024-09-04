# file_handling_assignment.py

def main():
    try:
        # Task 1: File Creation
        with open("my_file.txt", 'w') as file:
            file.write("Hello, World!\n")
            file.write("Python is great.\n")
            file.write("Numbers: 123, 456, 789\n")
        print("File created and initial content written.")

        # Task 2: File Reading and Display
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("\nFile content after initial write:\n")
            print(content)

        # Task 3: File Appending
        with open("my_file.txt", 'a') as file:
            file.write("Appending this line.\n")
            file.write("Another line added.\n")
            file.write("Final line in the file.\n")
        print("Additional lines appended to the file.")

        # Re-read the file to display the updated content
        with open("my_file.txt", 'r') as file:
            updated_content = file.read()
            print("\nFile content after appending:\n")
            print(updated_content)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have the necessary permissions to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operations complete.")

if __name__ == "__main__":
    main()