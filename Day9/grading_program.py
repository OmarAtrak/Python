student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}



for itemKey in student_scores:
    if student_scores[itemKey] > 90 and student_scores[itemKey] <= 100:
        student_grades[itemKey] = "Outstanding"
    elif student_scores[itemKey] > 80 and student_scores[itemKey] <= 90:
        student_grades[itemKey] = "Exceeds Expectations"
    elif student_scores[itemKey] > 70 and student_scores[itemKey] <= 80:
        student_grades[itemKey] = "Acceptable"
    elif student_scores[itemKey] <= 70:
        student_grades[itemKey] = "Fail "

print(student_grades)