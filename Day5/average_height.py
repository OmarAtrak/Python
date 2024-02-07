student_heights = "151 145 179".split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

students_number = 0
total_height = 0
for height in student_heights:
  total_height += height
  students_number += 1

average_height = round(total_height / students_number)
print(f"total height = {total_height}")
print(f"number of students = {students_number}")
print(f"average height = {average_height}")