# -------------------------------------------------------
# Week 3 - Activity 1 File Reader
# Author: Benjelyn Reves Patiag
# Date Created: 2-Dec-2025
# Description: File Reader
# -------------------------------------------------------



class FileReader:


    def __init__(self, filename):
        self.filename = filename
        self.content = ""

    def read_file(self):
        """Reads the entire file content and stores it."""
        try:
            # Try UTF-8 first (best for modern files)
            with open(self.filename, "r", encoding="utf-8") as file:
                self.content = file.read()

        except UnicodeDecodeError:
            print("UTF-8 failed. Retrying using 'latin-1' encoding...")
            # latin-1 never fails, but some characters may look odd.
            with open(self.filename, "r", encoding="latin-1") as file:
                self.content = file.read()

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        else:
            print("File read successfully!\n")


    def count_stars(self):
        """Returns the number of '*' characters in the file."""
        if not self.content:
            return 0
        return self.content.count("*")


# ============================
# Main Program
# ============================

if __name__ == "__main__":
    # Ask user for file name
    filename = r"C:\Users\benje\PycharmProjects\YCCIA_2511\demo_file.txt" # input("Enter file path (e.g. D:/Benj/MSE/MSE800/Term1/demo_file.txt): ")

    # Create object
    reader = FileReader(filename)

    # Read the file
    reader.read_file()

    # Print file contents
    #reader.print_content()

    # Count '*' characters
    star_count = reader.count_stars()
    print(f"\nNumber of '*' characters in the file: {star_count}")
