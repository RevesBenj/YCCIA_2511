# -------------------------------------------------------
# Week 3 - Activity 2 Append the text
# Author: Benjelyn Reves Patiag
# Date Created: 6-Dec-2025
# Description: Develop an OOP-based solution to continue W3-A1 by adding an "End of File" message to your project. Once completed, Share your updated code.
# -------------------------------------------------------



class FileReader:


    def __init__(self, filename):
        self.filename = filename
        self.content = ""

    def read_file(self):
        """Reads the entire file content and stores it."""
        try:
            # need to encode UTF-8 first for modern file
            with open(self.filename, "r", encoding="utf-8") as file:
                self.content = file.read()

        except UnicodeDecodeError:
            print("UTF-8 failed. Retrying using 'latin-1' encoding...")
            # latin-1 never fails, but some characters may look off :).
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

    def append_content(self):
        # Appends 'End of File' text to the end of the file.
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write("\nEnd of File")
            print("Successfully appended 'End of File' to the text file.")
        except Exception as e:
            print(f"Error while appending text: {e}")


# ============================
# Main Program
# ============================

if __name__ == "__main__":
    # find and set the file
    filename = r"C:\Users\benje\PycharmProjects\YCCIA_2511\demo_file.txt" # input("Enter file path (e.g. D:/Benj/MSE/MSE800/Term1/demo_file.txt): ")

    # Create object
    reader = FileReader(filename)

    # Print file contents + "End of File" message
    reader.append_content()

    # Count '*' characters
    star_count = reader.count_stars()
    print(f"\nNumber of '*' characters in the file: {star_count}")
