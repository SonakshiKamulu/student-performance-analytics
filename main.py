
import pandas as pd
import numpy as np


# Read student details from the CSV file
def load_student_data():
    students = pd.read_csv("students.csv")
    return students


# Calculate total and average marks
def calculate_marks(students):
    subjects = ["Python", "Java", "Mathematics"]

    students["Total"] = students[subjects].sum(axis=1)
    students["Average"] = students[subjects].mean(axis=1)

    return students


# Give a grade according to the average marks
def find_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


# Check whether a student passed all subjects
def check_result(row):
    subjects = ["Python", "Java", "Mathematics"]

    for subject in subjects:
        if row[subject] < 40:
            return "Fail"

    return "Pass"


# Display the analysis results
def show_analysis(students):
    subjects = ["Python", "Java", "Mathematics"]

    print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 65)

    print("\nSTUDENT RECORDS")
    print(students.to_string(index=False))

    print("\nCLASS SUMMARY")
    print("-" * 65)
    print("Number of students:", len(students))
    print("Overall class average:",
          round(np.mean(students["Average"]), 2))

    print("\nSUBJECT-WISE AVERAGES")
    print("-" * 65)

    for subject in subjects:
        average = np.mean(students[subject])
        print(subject, "average:", round(average, 2))

    print("\nPASS AND FAIL SUMMARY")
    print("-" * 65)
    print("Students passed:", (students["Result"] == "Pass").sum())
    print("Students failed:", (students["Result"] == "Fail").sum())

    print("\nHIGHEST AND LOWEST AVERAGE")
    print("-" * 65)

    highest = students.loc[students["Average"].idxmax()]
    lowest = students.loc[students["Average"].idxmin()]

    print("Highest performer:", highest["Name"],
          "-", round(highest["Average"], 2))
    print("Lowest performer:", lowest["Name"],
          "-", round(lowest["Average"], 2))

    print("\nTOP 5 STUDENTS")
    print("-" * 65)

    top_students = students.nlargest(5, "Average")
    print(top_students[["Name", "Average", "Grade", "Result"]].to_string(
        index=False
    ))

    print("\nATTENDANCE SUMMARY")
    print("-" * 65)
    print("Average attendance:",
          round(np.mean(students["Attendance"]), 2), "%")


# Run the complete program
def main():
    students = load_student_data()

    students = calculate_marks(students)

    students["Grade"] = students["Average"].apply(find_grade)
    students["Result"] = students.apply(check_result, axis=1)

    show_analysis(students)


if __name__ == "__main__":
    main()
