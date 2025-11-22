# MSE Week1 Benj
# Creating a table using Python with all required data types

# Data components
name = "Benjelyn Reves Patiag"                          # String
age = 39                                    # Integer
skills = ["Python", "SQL", "Power BI"]      # List
education = ("BS Computer Engineering", 2008)  # Tuple
contact_details = {                         # Dictionary
    "email": "benjelyn_reves@yahoo.com",
    "phone": "+64224998099"
}
certifications = {"MS", "EDM", "SQL"}  # Set (duplicates removed)

# Displaying data in a table format
print("Component\t\tData Type\tExample")
print("-" * 60)
print(f"Name\t\t\tString\t\t{name}")
print(f"Age\t\t\tInteger\t\t{age}")
print(f"Skills\t\t\tList\t\t{skills}")
print(f"Education\t\tTuple\t\t{education}")
print(f"Contact Details\tDictionary\t{contact_details}")

print(f"Certifications\tSet\t\t{certifications}")
