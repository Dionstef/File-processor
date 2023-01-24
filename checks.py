import numpy as np


# Base class for other exceptions
class Error(Exception):
    pass


class IncorrectSumOfWeights(Error):
    pass


class DataReadingError(Error):
    pass


# Checks if the sum of weights in each field is equal to 1
# Input: list with dictionaries, Raises: IncorrectSumOfWeights If the test fails
def check_weights_sum(student_list):
    tol = 1e-3

    for student in student_list:
        sum_weights = 0
        for weight_value in student['weights'].values():
            sum_weights += weight_value

        if not np.isclose(sum_weights, 1, rtol=0, atol=tol):
            msg = f"ERROR: Sum of weights of student {student['name']} is not equal to 1"
            raise IncorrectSumOfWeights(msg)

    return True


# Checks if the data have been read correctly
# Input: list with dictionaries, Raises: DataReadingError If the test fails
def check_reading(student_list):
    for student in student_list:
        for key, value in student.items():

            if type(value) is dict:  # check if the value is dictionary (true for weights and grades)
                for inner_dict_key, inner_dict_value in value.items():
                    if type(inner_dict_key) is float:  # check first if it is float
                        if np.isnan(inner_dict_key):
                            msg = f"ERROR: Nan value in line {student}"
                            raise DataReadingError(msg)
                    if type(inner_dict_value) is float:
                        if np.isnan(inner_dict_value):
                            msg = f"ERROR: Nan value in line {student}"
                            raise DataReadingError(msg)

            if type(key) is float:  # check first if it is float
                if np.isnan(key):
                    msg = f"ERROR: Nan value in line {student}"
                    raise DataReadingError(msg)

                if np.isnan(value):
                    msg = f"ERROR: Nan value in line {student}"
                    raise DataReadingError(msg)

    return True
