student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
def student_scores_to_grade (scores):
            grades={}
            for student,score in scores.items():
                if score >= 90:
                    grade = 'A'
                elif score >= 80:
                    grade = 'B'
                elif score >= 70:
                    grade = 'C'
                elif score >= 60:
                    grade = 'D'
                else:
                    grade ='F'
                student  
                grades[student]= grade
            return grades
students_grades = student_scores_to_grade(student_scores)
            
print (students_grades)
            