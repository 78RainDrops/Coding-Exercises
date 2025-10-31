students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# students = list(filter(lambda student: student[1] >= 90, students))
print(students)

high_student = []
for student in students:
    if student[1] >= 90:
        high_student.append(student)

print(high_student)
