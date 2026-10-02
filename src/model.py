from pathlib import Path
import math

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


# Load the student data from the data folder.
project_folder = Path(__file__).resolve().parent.parent
csv_file = project_folder / "data" / "students.csv"
students = pd.read_csv(csv_file)

# Choose the information used to make predictions and the result to predict.
feature_columns = ["study_hours", "attendance", "previous_marks"]
X = students[feature_columns]
y = students["final_marks"]

# Split the data so we can test the model on data it did not train on.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train a Linear Regression model.
model = LinearRegression()
model.fit(X_train, y_train)

# Check how close the model's predictions are to the real marks.
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Student Final Marks Prediction")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared (R2) Score: {r2:.2f}")


def get_validated_input(prompt, minimum=None, maximum=None):
    """Ask again until the user enters a valid number in the allowed range."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not math.isfinite(value):
            print("Please enter a finite number.")
            continue
        if minimum is not None and value < minimum:
            print(f"The value must be at least {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"The value must be no more than {maximum}.")
            continue
        return value


# Enter information for a new student to get a prediction.
study_hours = get_validated_input("Enter study hours (0 or more): ", minimum=0)
attendance = get_validated_input(
    "Enter attendance (0 to 100): ", minimum=0, maximum=100
)
previous_marks = get_validated_input(
    "Enter previous marks (0 to 100): ", minimum=0, maximum=100
)

new_student = pd.DataFrame(
    [[study_hours, attendance, previous_marks]],
    columns=feature_columns,
)
predicted_marks = model.predict(new_student)

predicted_mark = predicted_marks[0]

if predicted_mark >= 90:
    grade = "A+"
elif predicted_mark >= 80:
    grade = "A"
elif predicted_mark >= 70:
    grade = "B"
elif predicted_mark >= 60:
    grade = "C"
elif predicted_mark >= 40:
    grade = "D"
else:
    grade = "F"

result = "Pass" if predicted_mark >= 40 else "Fail"

print(f"Predicted final marks: {predicted_mark:.2f}")
print(f"Grade: {grade}")
print(f"Result: {result}")

# Compare the model's predictions with actual marks from the test data.
plots_folder = project_folder / "plots"
plots_folder.mkdir(exist_ok=True)

plt.figure()
plt.scatter(y_test, predictions)
plt.title("Actual vs Predicted Final Marks")
plt.xlabel("Actual Final Marks")
plt.ylabel("Predicted Final Marks")
plt.tight_layout()
plt.savefig(plots_folder / "actual_vs_predicted_marks.png")
plt.show()