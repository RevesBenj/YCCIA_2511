# MSE Week1
# Creating a table using Python with all required data types

# Data components
name = "John Doe"                          # String
age = 28                                    # Integer
skills = ["Python", "SQL", "Power BI"]      # List
education = ("BSc Computer Science", 2020)  # Tuple
contact_details = {                         # Dictionary
    "email": "john.doe@example.com",
    "phone": "+123456789"
}
certifications = {"Azure", "AWS", "Azure"}  # Set (duplicates removed)

# Displaying data in a table format
print("Component\t\tData Type\tExample")
print("-" * 60)
print(f"Name\t\t\tString\t\t{name}")
print(f"Age\t\t\tInteger\t\t{age}")
print(f"Skills\t\t\tList\t\t{skills}")
print(f"Education\t\tTuple\t\t{education}")
print(f"Contact Details\tDictionary\t{contact_details}")
print(f"Certifications\tSet\t\t{certifications}")