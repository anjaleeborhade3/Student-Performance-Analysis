from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# Find students.csv in the data folder at the project root.
project_folder = Path(__file__).resolve().parent.parent
csv_file = project_folder / "data" / "students.csv"

# Load the student data from the CSV file.
students = pd.read_csv(csv_file)

print("Student Performance Analysis")

print("\nStudent data:")
print(students)

print("\nBasic statistics:")
print(students.describe())

numeric_columns = [
	"study_hours",
	"attendance",
	"previous_marks",
	"final_marks",
]
summary = students[numeric_columns].agg(["mean", "min", "max"])
summary = summary.rename(index={"mean": "Average", "min": "Minimum", "max": "Maximum"})

print("\nExploratory Data Analysis")
print(f"Number of students: {students.shape[0]}")
print(f"Number of columns: {students.shape[1]}")
print("\nAverage, minimum, and maximum values:")
print(summary)
print("\nMissing values in each column:")
print(students.isnull().sum())

print("\nAverage study hours:", students["study_hours"].mean())
print("Average attendance:", students["attendance"].mean())
print("Average final marks:", students["final_marks"].mean())

top_student = students.loc[students["final_marks"].idxmax()]
print("\nStudent with the highest final marks:")
print(top_student["student_name"], "-", top_student["final_marks"])

# Create a folder for the graph image files.
plots_folder = project_folder / "plots"
plots_folder.mkdir(exist_ok=True)

# Study hours compared with final marks.
plt.figure()
plt.scatter(students["study_hours"], students["final_marks"])
plt.title("Study Hours vs Final Marks")
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.savefig(plots_folder / "study_hours_vs_final_marks.png")

# Attendance compared with final marks.
plt.figure()
plt.scatter(students["attendance"], students["final_marks"])
plt.title("Attendance vs Final Marks")
plt.xlabel("Attendance")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.savefig(plots_folder / "attendance_vs_final_marks.png")

# Previous marks compared with final marks.
plt.figure()
plt.scatter(students["previous_marks"], students["final_marks"])
plt.title("Previous Marks vs Final Marks")
plt.xlabel("Previous Marks")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.savefig(plots_folder / "previous_marks_vs_final_marks.png")

# Compare the average previous marks with the average final marks.
average_previous_marks = students["previous_marks"].mean()
average_final_marks = students["final_marks"].mean()

plt.figure()
plt.bar(
    ["Previous Marks", "Final Marks"],
    [average_previous_marks, average_final_marks],
)
plt.title("Average Previous Marks vs Average Final Marks")
plt.xlabel("Marks Type")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig(plots_folder / "average_previous_vs_final_marks.png")

plt.show()