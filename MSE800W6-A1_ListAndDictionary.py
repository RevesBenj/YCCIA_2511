# -------------------------------------------------------
# # Week 6 - Activity 1 Week 6 - Activity 1: List and dictionary data stucrture
# Author: Benjelyn Reves Patiag
# Date Created: 24-Jan- 2026
# W6-A1 – Part 1:
# Develop an object-oriented project that creates:
# a dictionary to store five students, using student ID as the key and student name as the value, and
# a second dictionary using student ID as the key and MSE800 score as the value.
#W6-A1 – Part 2:
#Combine the two dictionaries from Part 1 and generate a new dictionary that includes only students who passed (score ≥ 50%).
 # -------------------------------------------------------


class StudentManager:
    def __init__(self):
        # prepare empty dictionary
        # student id -> student name
        self.students = {}

        # student id -> student score
        self.scores = {}

    def add_student(self, student_id: int, name: str, score: int) -> None:
        # save student name using id
        self.students[student_id] = name

        # save student score using same id
        self.scores[student_id] = score

    def print_students(self) -> None:
        # print student id and name
        print("Students (ID -> Name):")
        for sid, name in self.students.items():
            print(f"ID: {sid}, Name: {name}")

    def print_scores(self) -> None:
        # print student id and score
        print("\nStudent Scores (ID -> Score):")
        for sid, score in self.scores.items():
            print(f"ID: {sid}, Score: {score}")

    def print_passed_students(self, pass_mark: int = 50) -> None:
        # zip used here
        # zip combine name and score together by order
        # first list = student names
        # second list = student scores
        print("\nPassed Students (Score >= 50):")

        for name, score in zip(self.students.values(), self.scores.values()):
            # check if student passed
            if score >= pass_mark:
                print(f"Name: {name}, Score: {score}")


# ---------------------------
# MAIN PROGRAM
# ---------------------------

# create object from StudentManager
manager = StudentManager()

# add students data
manager.add_student(1001, "Benj", 89)
manager.add_student(1002, "Bela", 92)
manager.add_student(1003, "Rob", 32)
manager.add_student(1004, "Bon", 88)
manager.add_student(1005, "Rend", 95)

# print students
manager.print_students()

# print scores
manager.print_scores()

# print passed students only using zip
manager.print_passed_students()
