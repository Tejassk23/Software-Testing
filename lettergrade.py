def calculate_grade():
    marks = []
    total_marks = 0
    
    for i in range(5):
        subject_marks = float(input("Enter marks for subject {}: ".format(i + 1)))
        marks.append(subject_marks)
        total_marks += subject_marks
        
    percentage = total_marks / 5
    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'
        
    print("Percentage: {:.2f}%".format(percentage))
    print("Grade: {}".format(grade))

if __name__ == "__main__":
    calculate_grade()