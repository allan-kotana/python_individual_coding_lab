import csv
import sys
import os


def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    assignments = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)


def evaluate_grades(data):
    """
    Evaluates the grades and prints the final result.
    """
    print("\n--- Processing Grades ---")

    if len(data) == 0:
        print("No grade data found.")
        return

    total_weight = 0
    formative_weight = 0
    summative_weight = 0
    total_grade = 0
    formative_grade = 0
    summative_grade = 0
    failed_formatives = []

    for item in data:
        score = item['score']
        weight = item['weight']
        group = item['group']

        if score < 0 or score > 100:
            print(f"Invalid score found for {item['assignment']}.")
            return

        total_weight += weight
        total_grade += score * weight / 100

        if group == "Formative":
            formative_weight += weight
            formative_grade += score * weight / 100
            if score < 50:
                failed_formatives.append(item)
        elif group == "Summative":
            summative_weight += weight
            summative_grade += score * weight / 100

    if total_weight != 100 or formative_weight != 60 or summative_weight != 40:
        print("Invalid weights. Total must be 100, Formative 60, and Summative 40.")
        return

    formative_percent = formative_grade / formative_weight * 100
    summative_percent = summative_grade / summative_weight * 100
    gpa = total_grade / 100 * 5.0

    print(f"Final Grade: {total_grade:.2f}%")
    print(f"GPA: {gpa:.2f}")
    print(f"Formative Average: {formative_percent:.2f}%")
    print(f"Summative Average: {summative_percent:.2f}%")

    if formative_percent >= 50 and summative_percent >= 50:
        print("Status: PASSED")
    else:
        print("Status: FAILED")

    if len(failed_formatives) > 0:
        highest_weight = failed_formatives[0]['weight']
        for item in failed_formatives:
            if item['weight'] > highest_weight:
                highest_weight = item['weight']

        print("Resubmission option(s):")
        for item in failed_formatives:
            if item['weight'] == highest_weight:
                print(f"- {item['assignment']}")
    else:
        print("No formative resubmission needed.")


if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
