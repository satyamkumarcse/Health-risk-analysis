Health Report Generator

A Python program that collects health information from multiple people and generates a simple health risk report for each person.

The program takes details like weight, height, blood pressure, and resting heart rate, then checks whether the values fall within healthy ranges. Based on the results, it assigns a risk category and displays a final summary report.

What the Program Does

* Takes health data input for multiple people
* Calculates BMI using weight and height
* Checks blood pressure values
* Checks resting heart rate
* Assigns a health risk category
* Displays a summary of all risk levels at the end

How to Run

Make sure Python is installed on your system.

Save the file as:

```bash id="8m2x5q"
health_report.py
```

Run the program using:

```bash id="4p7w1n"
python health_report.py
```

Inputs Required

For each person, the program asks for:

* Weight in kilograms
* Height in metres
* Systolic blood pressure
* Diastolic blood pressure
* Resting heart rate in BPM

Health Checks Performed

BMI Categories

* Below 18.5 -> Underweight
* 18.5 to 24.9 -> Normal
* Above 24.9 -> Overweight

Blood Pressure Check

* Systolic 90-120 and diastolic 60-80 -> Normal
* Below normal range -> Low BP
* Above normal range -> High BP

Resting Heart Rate Check

* 60 to 100 BPM -> Normal
* Below 60 -> Low heart rate
* Above 100 -> High heart rate

Risk Levels

Low Risk

All health values are within the healthy range.

Medium Risk

One health value is outside the healthy range.

High Risk

Two or more health values are outside the healthy range.

Purpose of the Project

This project was built to practice:

* Python fundamentals
* Conditional statements
* Loops
* Functions and calculations
* Working with user input
* Simple health data analysis

It is a beginner-friendly project that demonstrates how programming can be used to process and analyze real-world data.
