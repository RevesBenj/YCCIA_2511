# ================================================================
# Week 3 - Activity 5 Simple Clinic DBS (Python OOP + SQLite)
# Author: Benjelyn Reves Patiag
# Date Created: 12-Dec-2025
# Description: Design an ER diagram based on the provided scenario for a clinic and develop an OOP project
# that meets the following requirements:
# List the full information of all patients who are classified as seniors in the clinic (age > 65 years).
# Display the total number of doctors who specialise in ophthalmology.
# ================================================================


import sqlite3
from datetime import datetime


# ============================================================
# DATABASE CLASS
# ============================================================
#  This is a simple digital clinicB system that stores:
#     ✔ Departments
#     ✔ Doctors
#     ✔ Patients
#     ✔ Appointments
class Database:
    # Handles all database objects operations (connect, drop, create).

    def __init__(self, db_name="clinicB.db"):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.cursor.execute("PRAGMA foreign_keys = ON;")
            print("Database connected.\n")
        except Exception as e:
            print("Database connection error:", e)

    def drop_tables(self):
        # Refresh database by deleting all tables.
        try:
            tables = ["Appointment", "Doctor", "Patient", "Department"]
            for t in tables:
                self.cursor.execute(f"DROP TABLE IF EXISTS {t}")
            self.conn.commit()
            print("Tables dropped.\n")
        except Exception as e:
            print("Error dropping tables:", e)

    def create_tables(self):
        #  clinicB-related tables creation
        try:
            self.cursor.execute("""
                CREATE TABLE Department (
                    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dept_name TEXT NOT NULL
                );
            """)

            self.cursor.execute("""
                CREATE TABLE Doctor (
                    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    specialty TEXT NOT NULL,
                    phone TEXT,
                    dept_id INTEGER,
                    FOREIGN KEY(dept_id) REFERENCES Department(dept_id)
                );
            """)

            self.cursor.execute("""
                CREATE TABLE Patient (
                    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    date_of_birth TEXT NOT NULL,
                    phone TEXT,
                    address TEXT
                );
            """)

            self.cursor.execute("""
                CREATE TABLE Appointment (
                    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER NOT NULL,
                    doctor_id INTEGER NOT NULL,
                    appointment_datetime TEXT,
                    reason TEXT,
                    FOREIGN KEY(patient_id) REFERENCES Patient(patient_id),
                    FOREIGN KEY(doctor_id) REFERENCES Doctor(doctor_id)
                );
            """)

            self.conn.commit()
            print("Tables created.\n")

        except Exception as e:
            print("Error creating tables:", e)


# ============================================================
# ENTITY CLASSES
# ============================================================
class Department:
    # Creates a department record.
    def __init__(self, db, dept_name):
        try:
            db.cursor.execute(
                "INSERT INTO Department (dept_name) VALUES (?)",
                (dept_name,))
            db.conn.commit()
        except Exception as e:
            print("Department insert error:", e)


class Doctor:
    # Creates a doctor record.
    def __init__(self, db, first_name, last_name, specialty, phone, dept_id):
        try:
            db.cursor.execute("""
                INSERT INTO Doctor (first_name, last_name, specialty, phone, dept_id)
                VALUES (?, ?, ?, ?, ?)
            """, (first_name, last_name, specialty, phone, dept_id))
            db.conn.commit()
        except Exception as e:
            print("Doctor insert error:", e)


class Patient:
    # Creates a patient record:
    def __init__(self, db, first_name, last_name, dob, phone, address):
        try:
            db.cursor.execute("""
                INSERT INTO Patient (first_name, last_name, date_of_birth, phone, address)
                VALUES (?, ?, ?, ?, ?)
            """, (first_name, last_name, dob, phone, address))
            db.conn.commit()
        except Exception as e:
            print("Patient insert error:", e)


# ============================================================
# SUPPORT FUNCTION — AGE CALCULATOR
# ============================================================
def calculate_age(dob):
    # Converts date of birth into age. Age calculation from date of birth
    try:
        birth = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        return today.year - birth.year - \
               ((today.month, today.day) < (birth.month, birth.day))
    except Exception:
        return 0


# ============================================================
# MAIN PROGRAM LOGIC
# ============================================================
def main():
    try:
        db = Database()
        db.drop_tables()
        db.create_tables()

        # ----------------------------------------------------
        # INSERT SAMPLE DATA
        # ----------------------------------------------------
        Department(db, "Ophthalmology")
        Department(db, "General Medicine")
        Department(db, "Pediatrics")
        Department(db, "Dermatology")

        Doctor(db, "Clark", "Kent", "Ophthalmologist", "0912345678", 1)
        Doctor(db, "Benjamin", "Reeves", "Ophthalmologist", "0999988877", 1)
        Doctor(db, "Rob", "Cruz", "Ophthalmologist", "09943588877", 1)
        Doctor(db, "Anna", "Tan", "Ophthalmologist", "0992388877", 1)
        Doctor(db, "Clark", "King", "General Practitioner", "0988776655", 2)
        Doctor(db, "Clark", "King", "Dermatology", "0988776655", 2)
        Doctor(db, "Clark", "Kent", "Pediatrics", "0912345678", 1)

        Patient(db, "Bennie", "Lim", "1954-04-15", "021234567", "Auckland")
        Patient(db, "Jose", "Marith", "1955-08-20", "0911122233", "Singapore")
        Patient(db, "Piolo", "Milby", "1987-02-10", "099887766", "Philippines")
        Patient(db, "Ralph", "Winny", "1959-01-20", "0911122233", "Singapore")
        Patient(db, "Dolphy", "Cobe", "1990-02-10", "099887766", "Philippines")
        Patient(db, "Marrie", "Santiago", "1956-08-20", "0911122233", "Singapore")
        Patient(db, "Kris", "Danny", "1986-02-10", "099887766", "Philippines")

        # # ----Begin------------------------------------------------
        # # LIST ALL PATIENTS
        # # ----------------------------------------------------
        # print("=== LIST OF ALL PATIENTS ===")
        # try:
        #     db.cursor.execute("SELECT * FROM Patient")
        #     for row in db.cursor.fetchall():
        #         print(row)
        # except Exception as e:
        #     print("Error listing patients:", e)
        #
        # # ----------------------------------------------------
        # # LIST ALL DOCTORS
        # # ----End------------------------------------------------
        # print("\n=== LIST OF ALL DOCTORS ===")
        # try:
        #     db.cursor.execute("SELECT doctor_id, first_name, last_name, specialty FROM Doctor")
        #     for row in db.cursor.fetchall():
        #         print(row)
        # except Exception as e:
        #     print("Error listing doctors:", e)



        # ----------------------------------------------------
        # LIST SENIOR PATIENTS (AGE > 65)
        # ----------------------------------------------------
        print("\n=== SENIOR PATIENTS (Age > 65) ===")
        try:
            db.cursor.execute("SELECT * FROM Patient")
            for row in db.cursor.fetchall():
                pid, fname, lname, dob, phone, address = row
                age = calculate_age(dob)
                if age > 65:
                    print(f"{pid} | {fname} {lname} | Age {age} | Phone {phone}")
        except Exception as e:
            print("Error retrieving senior patients:", e)

        # ----------------------------------------------------
        # COUNT DOCTORS SPECIALIZING IN OPHTHALMOLOGY
        # ----------------------------------------------------
        print("\n=== OPHTHALMOLOGY DOCTORS: ===")
        try:
            db.cursor.execute("""
                SELECT first_name, last_name FROM Doctor
                WHERE specialty = 'Ophthalmologist'
            """)
            ophthalmologists = db.cursor.fetchall()

            for d in ophthalmologists:
                print("Doctor:", d[0], d[1])

            print("\nTotal Ophthalmologists:", len(ophthalmologists))

        except Exception as e:
            print("Error counting ophthalmologists:", e)

        db.conn.close()
        print("\nProgram finished.\n")

    except Exception as e:
        print("Unexpected program error:", e)


if __name__ == "__main__":
    main()
