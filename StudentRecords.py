import json
class StudentRecords:
    COURSES = "courses"
    NAME = "name"
    AGE = "age"
    NOT_IN_SYS_MSG = "Student is not in the system. Please initialize student."
    OPTIONS = "Please select between the following options:\n" \
              "1. ADD STUDENT TO RECORDS\n" \
              "2. ADD COURSE TO STUDENT'S RECORD\n" \
              "3. RETRIEVE STUDENT'S NAME\n" \
              "4. RETRIEVE STUDENT'S AGE\n" \
              "5. RETRIEVE STUDENT'S COURSE GRADE\n" \
              "6. EDIT STUDENT'S COURSE GRADE\n" \
              "7. REMOVE COURSE FROM STUDENT'S RECORD\n" \
              "8. REMOVE STUDENT FROM RECORDS\n" \
              "9. SAVE\n" \
              "10. EXIT\n"

    def __init__(self, output_stream, input_stream=None):
        self.stud_dict = {}
        if input_stream is not None:
            student_records = open(input_stream, "r")
            self.stud_dict = json.load(student_records)
            student_records.close()
        self.output_stream = output_stream


    def start(self):
        while True:
            option = input(self.OPTIONS)
            if option.isdigit():
                selection = int(option)
                if selection in {1, 2, 3, 4, 5, 6, 7, 8}:
                    student_id = input("Please enter student's ID\n")
                    if selection == 1:
                        name = input("Please enter student's name\n")
                        age = input("Please enter student's age\n")
                        if age == "":
                            self.add_student(name, student_id)
                        else:
                            self.add_student(name, student_id, age)
                    elif selection == 2:
                        course = input("Please enter course\n")
                        grade = input("Please enter student's grade\n")
                        if grade == "":
                            self.add_course(student_id, course)
                        else:
                            self.add_course(student_id, course, grade)
                    elif selection == 3:
                        student_name = self.get_student_name(student_id)
                        if student_name is not None:
                            print(student_name)
                    elif selection == 4:
                        student_age = self.get_student_age(student_id)
                        if student_age is not None:
                            print(student_age)
                    elif selection == 5:
                        course = input("Please enter course\n")
                        course_grade = self.get_course_grade(student_id, course)
                        if course_grade is not None:
                            print(course_grade)
                    elif selection == 6:
                        course = input("Please enter course\n")
                        grade = input("Please enter student's grade\n")
                        self.edit_course_grade(student_id, course, grade)
                    elif selection == 7:
                        course = input("Please enter course\n")
                        self.remove_course(student_id, course)
                    elif selection == 8:
                        self.remove_student(student_id)
                elif selection == 9:
                    self.save()
                elif selection == 10:
                    break
                else:
                    print("Invalid selection. Please try again.")
    def save(self):
        with open(self.output_stream, 'w') as outfile:
            json.dump(self.stud_dict, outfile)

    def add_student(self, name: str, student_id: str, age=None):
        if student_id in self.stud_dict:
            print("Student ID is already in system.\n")
            return
        if age is not None and not age.isdigit():
            print("Student age is invalid.\n")
            return
        course_dic = {}
        if age is not None:
            self.stud_dict[student_id] = {self.NAME: name, self.AGE: int(age),
                                          self.COURSES: course_dic}
        else:
            self.stud_dict[student_id] = {self.NAME: name, self.AGE: age,
                                          self.COURSES: course_dic}
        print("Student successfully added to records.\n")
        return

    def add_course(self, student_id: str, course: str, grade=None):
        if student_id not in self.stud_dict:
            print(self.NOT_IN_SYS_MSG)
            return
        if course in self.stud_dict[student_id][self.COURSES]:
            print("Course was already entered into student's file. To "
                  "update student course grade select EDIT COURSE GRADE.\n")
            return
        self.stud_dict[student_id][self.COURSES][course] = grade
        print("Course successfully added to student file.\n")
        return

    def get_course_grade(self, student_id: str, course: str):
        if student_id not in self.stud_dict:
            print(self.NOT_IN_SYS_MSG)
            return
        if course in self.stud_dict[student_id][self.COURSES]:
            if self.stud_dict[student_id][self.COURSES][course] is None:
                print("Student's course grade is not in the system.\n")
                return
            else:
                return self.stud_dict[student_id][self.COURSES][course]
        print("Course not found in student file.\n")
        return

    def get_student_age(self, student_id: str):
        if student_id not in self.stud_dict:
            print(self.NOT_IN_SYS_MSG)
            return
        if self.stud_dict[student_id][self.AGE] is None:
            print("Student's age not in system.\n")
            return
        return self.stud_dict[student_id][self.AGE]

    def get_student_name(self, student_id: str):
        if student_id not in self.stud_dict:
            print(self.NOT_IN_SYS_MSG)
            return
        return self.stud_dict[student_id][self.NAME]

    def edit_course_grade(self, student_id, course: str, grade: str):
        if student_id not in self.stud_dict:
            print(self.NOT_IN_SYS_MSG)
            return
        if course not in self.stud_dict[student_id][self.COURSES]:
            print("Course is not in student file.\n")
            return
        self.stud_dict[student_id][self.COURSES][course] = grade
        print("Grade successfully updated.\n")

    def remove_course(self, student_id, course: str):
        if student_id not in self.stud_dict:
            print(self.NOT_IN_SYS_MSG)
            return
        if course not in self.stud_dict[student_id][self.COURSES]:
            print("Course is not in student file.\n")
            return
        del self.stud_dict[student_id][self.COURSES][course]
        print("Course successfully removed from student's file.\n")

    def remove_student(self, student_id):
        if student_id not in self.stud_dict:
            print(self.NOT_IN_SYS_MSG)
            return
        del self.stud_dict[student_id]
        print("Student successfully removed from records.\n")
