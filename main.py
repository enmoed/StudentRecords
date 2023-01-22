from StudentRecords import StudentRecords

def main():
    directory = input("Please enter filepath of student records "
                      "if it already exists. Otherwise select enter.\n")
    output_directory = input("Please enter output filepath.\n")
    if directory == "":
        directory = None
    student_records = StudentRecords(output_directory, directory)
    student_records.start()

if __name__ == '__main__':
    main()
