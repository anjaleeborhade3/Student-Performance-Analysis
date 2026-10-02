# Student Performance Analysis

## Project Overview

This beginner-friendly project explores sample student results and uses a Linear Regression model to estimate a student's final marks. It combines basic data analysis, graphs, model evaluation, and an interactive prediction.

## Problem Statement

Students and teachers may want to understand how study hours, attendance, and previous marks relate to final marks. This project summarizes a small sample dataset and demonstrates how those inputs can be used to make a simple prediction.

## Objectives

- Load and inspect student data with Pandas.
- Summarize averages, minimums, and maximums.
- Visualize relationships between student features and final marks.
- Train and evaluate a Linear Regression model.
- Predict final marks, a grade, and pass/fail status for a new student.

## Features

- Prints the dataset, descriptive statistics, and missing-value counts.
- Reports average, minimum, and maximum values for numeric columns.
- Saves EDA and model evaluation graphs in `plots/`.
- Reports Mean Absolute Error (MAE) and R-squared (R2).
- Checks that interactive inputs are valid before making a prediction.
- Displays predicted marks, grade, and pass/fail result.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- scikit-learn

## Dataset Description

The model uses `data/students.csv`. It contains eight sample students and these columns:

| Column | Description | Used by model |
| --- | --- | --- |
| `student_name` | Student name | No |
| `study_hours` | Study time in hours | Yes |
| `attendance` | Attendance percentage | Yes |
| `previous_marks` | Previous marks out of 100 | Yes |
| `final_marks` | Final marks out of 100 | Target |

The names are lowercase in the CSV; `study_hours`, `attendance`, and `previous_marks` correspond to the requested Study_Hours, Attendance, and Previous_Marks features. The student name is not used to train the model.

## Project Structure

```text
Student_performance_analysis/
|-- data/
|   |-- students.csv
|   `-- student.csv
|-- notebooks/
|-- plots/
|-- src/
|   |-- analysis.py
|   `-- model.py
|-- .gitignore
|-- README.md
`-- requirements.txt
```

`data/student.csv` is the original sample file and is retained. Both scripts use `data/students.csv` as their shared input dataset.

## How the ML Model Works

1. The program loads the CSV with Pandas.
2. `study_hours`, `attendance`, and `previous_marks` are the input features (`X`). `final_marks` is the value to predict (`y`).
3. The data is split into training and testing parts. The model learns from the training data and is evaluated on the held-out test data.
4. `LinearRegression` learns a simple relationship between the three features and final marks.
5. The program asks for a new student's feature values and uses the trained model to estimate their final marks.
6. The estimate is assigned a grade: 90 or more is A+, 80 or more is A, 70 or more is B, 60 or more is C, 40 or more is D, and below 40 is F. A predicted mark of 40 or more is Pass; below 40 is Fail.

## Model Evaluation

- **MAE:** Mean Absolute Error is the average size of the prediction errors in marks. Lower is better.
- **R-squared (R2):** Describes how well the model's predictions fit the test results. A value closer to 1 is generally better; it can also be negative.
- **Actual vs Predicted plot:** Compares test-set predictions with the actual final marks.

This is a small example dataset, so its evaluation scores are for learning and should not be treated as proof that the model will predict real student results reliably.

## How to Install and Run

Open a terminal in the project folder. Create and activate a virtual environment, then install the packages:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the data analysis and graphs:

```powershell
python src/analysis.py
```

Run the model evaluation and interactive prediction:

```powershell
python src/model.py
```

Enter study hours as zero or greater. Attendance and previous marks must each be between 0 and 100. The graphs are saved in the `plots/` folder.

## Example Prediction

For study hours `3`, attendance `90`, and previous marks `80`, the sample model predicts about `84.76` marks, which is Grade `A` and a `Pass`. Evaluation values may change if the dataset or train/test split changes.

## Future Improvements

- Add more student records so model evaluation is more meaningful.
- Compare Linear Regression with other beginner-friendly models.
- Add charts for distributions and feature relationships.
- Build a simple form or web interface for predictions.
- Test how the model performs on a separate real-world dataset.