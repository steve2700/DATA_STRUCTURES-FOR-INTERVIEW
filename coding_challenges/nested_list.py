if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Sort the list of students by their grades
    sorted_students = sorted(students, key=lambda x: x[1])
    
    # Find the second lowest grade
    second_lowest_grade = sorted(set([student[1] for student in sorted_students]))[1]
    
    # Find the names of the students with the second lowest grade
    second_lowest_students = sorted([student[0] for student in sorted_students if student[1] == second_lowest_grade])
    
    # Print the names of the students with the second lowest grade
    for student in second_lowest_students:
        print(student)

