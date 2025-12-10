# ================================================================
# Week 3 - Activity 4 DBS
# Author: Benjelyn Reves Patiag
# Date Created: 11-Dec-2025
# Description: Develop a OOP project to develop a designed database from m W3-A3
# and show the number of students for MSE800 course
# and list all teachers name who are teaching MSE801.
# Includes: DROP TABLES to ensure latest schema, clean CREATE TABLE, insert and query sample data
# ================================================================

import sqlite3


# DATABASE CLASS
class Database:
    def __init__(self, db_name="YCCIA_MSE.db"):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            print("Database connected.")
        except Exception as e:
            print("Database connection error:", e)

    def drop_tables(self):
        """DROP all tables in order to avoid FK errors."""
        try:
            print("\nDropping all existing tables...")

            tables = ["Registers", "Teaches", "Course",
                      "Student", "Teacher", "Department"]

            for t in tables:
                self.cursor.execute(f"DROP TABLE IF EXISTS {t};")

            self.conn.commit()
            print("All old tables dropped.\n")

        except Exception as e:
            print("Error dropping tables:", e)

    def create_tables(self):
        """Create new tables following ERD exactly."""
        try:
            print("Creating fresh tables...")

            self.cursor.execute("""
                CREATE TABLE Student(
                    ID INTEGER PRIMARY KEY,
                    S_name VARCHAR,
                    S_email VARCHAR,
                    S_DateOfBirth DATE,
                    S_Phone INTEGER,
                    S_Address VARCHAR
                );
            """)

            self.cursor.execute("""
                CREATE TABLE Teacher(
                    T_ID INTEGER PRIMARY KEY,
                    T_name VARCHAR,
                    T_email VARCHAR,
                    T_Phone INTEGER,
                    T_Address VARCHAR
                );
            """)

            self.cursor.execute("""
                CREATE TABLE Department(
                    Dept_Id INTEGER PRIMARY KEY,
                    Dept_Title VARCHAR,
                    Dept_Location VARCHAR
                );
            """)

            self.cursor.execute("""
                CREATE TABLE Course(
                    code VARCHAR PRIMARY KEY,
                    Course_Title VARCHAR,
                    Course_desc VARCHAR,
                    Credit INTEGER,
                    Dept_Id INTEGER,
                    FOREIGN KEY(Dept_Id) REFERENCES Department(Dept_Id)
                );
            """)

            self.cursor.execute("""
                CREATE TABLE Registers(
                    ID INTEGER,
                    code VARCHAR,
                    FOREIGN KEY(ID) REFERENCES Student(ID),
                    FOREIGN KEY(code) REFERENCES Course(code)
                );
            """)

            self.cursor.execute("""
                CREATE TABLE Teaches(
                    T_ID INTEGER,
                    code VARCHAR,
                    FOREIGN KEY(T_ID) REFERENCES Teacher(T_ID),
                    FOREIGN KEY(code) REFERENCES Course(code)
                );
            """)

            self.conn.commit()
            print("Tables created successfully.\n")

        except Exception as e:
            print("Error creating tables:", e)


# ================================================================
# ENTITY CLASSES
# ================================================================

class Student:
    def __init__(self, db, ID, name, email, dob, phone, address):
        try:
            db.cursor.execute("""
                INSERT INTO Student VALUES (?, ?, ?, ?, ?, ?)
            """, (ID, name, email, dob, phone, address))
            db.conn.commit()
        except Exception as e:
            print(f"Error inserting student {name}:", e)


class Teacher:
    def __init__(self, db, T_ID, name, email, phone, address):
        try:
            db.cursor.execute("""
                INSERT INTO Teacher VALUES (?, ?, ?, ?, ?)
            """, (T_ID, name, email, phone, address))
            db.conn.commit()
        except Exception as e:
            print(f"Error inserting teacher {name}:", e)


class Department:
    def __init__(self, db, dept_id, title, location):
        try:
            db.cursor.execute("""
                INSERT INTO Department VALUES (?, ?, ?)
            """, (dept_id, title, location))
            db.conn.commit()
        except Exception as e:
            print(f"Error inserting department {title}:", e)


class Course:
    def __init__(self, db, code, title, desc, credit, dept_id):
        try:
            db.cursor.execute("""
                INSERT INTO Course VALUES (?, ?, ?, ?, ?)
            """, (code, title, desc, credit, dept_id))
            db.conn.commit()
        except Exception as e:
            print(f"Error inserting course {code}:", e)


# ================================================================
# RELATIONSHIP FUNCTIONS FOR THE QUERIES
# ================================================================

def register_student(db, stud_id, course_code):
    try:
        db.cursor.execute("INSERT INTO Registers VALUES (?, ?)", (stud_id, course_code))
        db.conn.commit()
    except Exception as e:
        print("Error registering student:", e)


def assign_teacher(db, teacher_id, course_code):
    try:
        db.cursor.execute("INSERT INTO Teaches VALUES (?, ?)", (teacher_id, course_code))
        db.conn.commit()
    except Exception as e:
        print("Error assigning teacher:", e)


# ================================================================
# MAIN PROGRAM
# ================================================================

def main():
    print("\n========== YCCIA_MSE DATABASE SYSTEM ==========\n")

    # Initialize Database
    db = Database()

    # Always refresh tables schema
    db.drop_tables()
    db.create_tables()

    # Insert Department
    Department(db, 10, "MSE Department", "Auckland")

    # Insert Courses
    Course(db, "MSE800", "Professional Software Development",
           "Coding + Projects", 4, 10)
    Course(db, "MSE801", "Research Methods",
           "Research fundamentals", 4, 10)

    # Insert Teachers
    Teacher(db, 1, "Dr. Mohammad Norouzifard", "mn@yoobee.com", 12345, "Auckland")
    Teacher(db, 2, "Dr. Saveeta Bai", "sb@yoobee.com", 23456, "Auckland")
    Teacher(db, 3, "Dr. Arun Kumar", "ak@yoobee.com", 34354, "Auckland")

    # Teacher Assignments
    assign_teacher(db, 1, "MSE801")
    assign_teacher(db, 1, "MSE800")
    assign_teacher(db, 2, "MSE800")
    assign_teacher(db, 3, "MSE801")

    # Insert Students
    Student(db, 101, "Benj", "benj@yoobee.com", "1986-01-01", 224123456, "Auckland")
    Student(db, 102, "Roxi", "Roxi@yoobee.com", "1986-02-01", 224123879, "Auckland")
    Student(db, 103, "Bert", "bert@yoobee.com", "1986-03-01", 224121234, "Auckland")
    Student(db, 104, "Eryl", "Eryl@yoobee.com", "1986-03-01", 224126789, "Auckland")
    Student(db, 105, "Sofia", "sofia@yoobee.com", "1986-03-01", 224124567, "Auckland")

    # Student Registrations
    register_student(db, 101, "MSE800")
    register_student(db, 102, "MSE800")
    register_student(db, 103, "MSE800")
    register_student(db, 104, "MSE800")
    register_student(db, 101, "MSE801")
    register_student(db, 102, "MSE801")
    register_student(db, 103, "MSE801")
    register_student(db, 105, "MSE801")

    # =============================================================
    # OUTPUT: Print all the created tables
    # =============================================================
    db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = db.cursor.fetchall()
    print("Tables Created:")
    print(tables)

    # =============================================================
    # OUTPUT 1: Students in MSE800
    # =============================================================

    db.cursor.execute("""
        SELECT s.ID, S_name, S_email, S_Phone
        FROM Student s
        JOIN Registers ON s.ID = Registers.ID
        WHERE Registers.code = 'MSE800';
    """)

    rows = db.cursor.fetchall()

    print("\nStudents in MSE800:")
    print("----------------------------------------------")

    for row in rows:
        id, name, email, phone = row
        print(f"ID: {id} | Name: {name} | Email: {email} | Phone: {phone}")

    print("TOTAL:", len(rows))


    # =============================================================
    # OUTPUT 2: Teachers teaching MSE801
    # =============================================================
    # db.cursor.execute("""
    #     SELECT T_name
    #     FROM Teacher
    #     JOIN Teaches ON Teacher.T_ID = Teaches.T_ID
    #     WHERE Teaches.code = 'MSE801';
    # """)
    # teachers_mse801 = [row[0] for row in db.cursor.fetchall()]
    #
    # print("\nTeachers assigned to MSE801:")
    # for t in teachers_mse801:
    #     print(" -", t)

    db.cursor.execute("""
        SELECT t.T_ID, t.T_name, t.T_email, t.T_Phone
        FROM Teacher t
        JOIN Teaches ON t.T_ID = Teaches.T_ID
        WHERE Teaches.code = 'MSE801';
    """)

    rows = db.cursor.fetchall()

    print("\nTeachers for MSE801:")
    print("----------------------------------------------")

    for row in rows:
        tid, name, email, phone = row
        print(f"ID: {tid} | Name: {name} | Email: {email} | Phone: {phone}")

    # ===========================
    # CLOSE DATABASE CONNECTION
    # ===========================
    db.conn.close()
    print("\nDatabase connection closed.")
    print("\n========== PROGRAM COMPLETE ==========\n")
# ================================================================
# RUN MAIN
# ================================================================
if __name__ == "__main__":
    main()
