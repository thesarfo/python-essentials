# define the grade point values for each grade
grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "E": 0.0
}

# define a function to calculate the GPA
def calculate_gpa(grades):
    total_grade_points = 0
    total_credits = 0
    for grade, credits in grades.items():
        total_grade_points += grade_points[grade] * credits
        total_credits += credits
    if total_credits == 0:
        return 0
    else:
        return round(total_grade_points / total_credits, 2)

# example usage
grades = {"A": 3, "A": 3, "A": 3, "A": 3, "A": 3}
gpa = calculate_gpa(grades)
print("Your GPA is:", gpa)
