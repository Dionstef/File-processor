from read_file import *
from students import *
from checks import *

if __name__ == '__main__':
    # read excel file into a list of dictionaries
    input_list = read_file('student_grades.xlsx')

    try:
        # checks if there is NaN in the data. If not it raises DataReadingError
        check_if_nan(input_list)

        # checks if the grades and weights are numbers. If not it raises DataReadingError
        check_if_numbers(input_list)

        # checks if the sum of weights in each field is equal to 1. If not it raises IncorrectSumOfWeights error
        check_weights_sum(input_list)

    except Exception as e:
        print(e)
    else:
        # create list of student objects
        student_list = [Student(**s) for s in input_list]

        # for each student print its name, class and average grade
        print('{:<12s}  {:<12s}  {:<12s}'.format('name ', 'class ', 'weighted average grade'))
        for student in student_list:
            line_new = '{:<12s}  {:<12s}  {:<2.2f}'.format(student)
            print(line_new)

        # calculate and print the average of each class and field
        class_avg_dict, field_avg_dict = calculate_class_average(student_list)
        print('\nSimple average grade of each class: ')
        print(class_avg_dict)
        print('\nWeighted average grade of each field: ')
        print(field_avg_dict)
