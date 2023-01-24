# student class
class Student:
    def __init__(self, name, age, class_name, field, grades, weights, **kwargs):
        self.name = name
        self.age = age
        self.class_name = class_name
        self.field = field
        self.grades = grades
        self.weights = weights
        self.details = kwargs

    # function for calculating weighted average grade of student
    def get_weighted_average_grade(self):
        wt_average_grade = 0
        for index, key in enumerate(self.grades):
            wt_average_grade += list(self.grades.values())[index] * list(self.weights.values())[index]

        return wt_average_grade

    # function for calculating simple average grade of student
    def get_average_grade(self):
        average_grade = 0
        for grade in self.grades.values():
            average_grade += grade

        average_grade /= len(self.grades)  # divide by the number of courses to get the average

        return average_grade

#  function for calculating the average of each class and each field.
#  Input: list of students
#  Returns: 2 dictionaries with class and field (weighted) averages
def calculate_class_average(student_list):
    class_averages = {}
    field_averages = {}
    for student in student_list:
        if student.class_name not in class_averages:
            class_averages[student.class_name] = student.get_average_grade()
        else: #if class already in dictionary, add the grade of the student
            class_averages[student.class_name] += student.get_average_grade()

        if student.field not in field_averages:
            field_averages[student.field] = student.get_weighted_average_grade()
        else: #if field already in dictionary, add the grade of the student
            field_averages[student.field] += student.get_weighted_average_grade()

    # divide by the number of students in each class and field to get the average
    for class_name in class_averages.keys():
        class_averages[class_name] /= sum(s.class_name == class_name for s in student_list)

    for field in field_averages.keys():
        field_averages[field] /= sum(s.field == field for s in student_list)

    #  round the number to 2 decimals
    class_averages = {key: round(class_averages[key], 2) for key in class_averages}
    field_averages = {key: round(field_averages[key], 2) for key in field_averages}

    return class_averages, field_averages
