import pandas as pd


# Function that calculates useful indices
# Input: dataframe, Return:s number of courses, start_of_courses_col, end_of_data_col
def calc_indices(df):
    n_courses = df.columns.get_loc("weights") - df.columns.get_loc(
        "grades") - 1  # finds number of courses
    start_of_courses_col = df.columns.get_loc("grades") + 1  # finds the col number where the courses start
    end_of_data_col = df.columns.get_loc(
        "weights") + n_courses + 1  # finds  the col number where the data end

    return n_courses, start_of_courses_col, end_of_data_col


# Function that creates courses and weights keys in list_dict.
# Input: list_dict, start_of_courses_col, n_courses, Returns: updated list_dict
def create_courses_and_weights_keys(list_dict, start_of_courses_col, n_courses):
    for student in list_dict:
        student['grades'] = {}
        for i in range(n_courses):
            student['grades'][list(student)[start_of_courses_col - 1]] = student[
                list(student)[start_of_courses_col - 1]]  # adds courses key to the new dictionary, no i is required
            # since the position is always the same due to the deletion of the key
            del student[list(student)[
                start_of_courses_col - 1]]  # removes the old key, no i is required

        student['weights'] = {}
        for i in range(n_courses):
            student['weights'][list(student)[start_of_courses_col - 1]] = student[
                list(student)[start_of_courses_col - 1]]  # adds weights key to the new dictionary, no i is required

            del student[list(student)[start_of_courses_col - 1]]  # removes the old key, no i is required

    return list_dict


# Function for reading input file.
# Input: path of file, Returns:  file in a list of dictionaries
def read_file_into_list(path):
    # read file into dataframe
    df = pd.read_excel(path, skiprows=[0])

    # calculate useful indices
    n_courses, start_of_courses_col, end_of_data_col = calc_indices(df)

    # remove unused rows and columns
    df.drop(df.iloc[:, end_of_data_col:], inplace=True, axis=1)  # removes extra columns
    df.drop(columns=["grades", "weights"], inplace=True)  # removes grade and weight columns

    # convert file into list of dictionaries
    list_dict = df.to_dict('records')

    # create courses and weights keys in list_dict
    list_dict = create_courses_and_weights_keys(list_dict, start_of_courses_col, n_courses)

    return list_dict
