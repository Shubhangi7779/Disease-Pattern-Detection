# Disease Pattern Detection - Based on Python Syllabus (File Handling & CSV)

import csv

def analyze_diabetes_data(filename):
    total_patients = 0
    diabetic_count = 0
    non_diabetic_count = 0
    
    try:
        # Unit 5: Working with CSV Files & Exception Handling
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            print("--- Reading Disease Dataset ---")
            for row in csv_reader:
                total_patients += 1
                # Checking the 'Outcome' column for patterns
                if int(row['Outcome']) == 1:
                    diabetic_count += 1
                else:
                    non_diabetic_count += 1
                    
        # Displaying Results
        print(f"\nTotal Patients Analyzed: {total_patients}")
        print(f"Diabetic Patients Pattern Found: {diabetic_count}")
        print(f"Non-Diabetic Patients: {non_diabetic_count}")
        
        # Writing results to a summary file (File Handling: Writing Text Files)
        with open('analysis_report.txt', 'w') as report_file:
            report_file.write("Disease Pattern Detection Report\n")
            report_file.write(f"Total Patients: {total_patients}\n")
            report_file.write(f"Diabetic Count: {diabetic_count}\n")
            report_file.write(f"Non-Diabetic Count: {non_diabetic_count}\n")
        print("\nReport successfully saved to 'analysis_report.txt'!")

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    analyze_diabetes_data('diabetes.csv')