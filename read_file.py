import pandas as pd


# function for reading input file: parameters: path of file, returns the file in dataframe
def read_file(path):
    # read file into dataframe
    df = pd.read_excel(path, skiprows=[0])

    # rename grades and weights
    n_courses = df.columns.get_loc("weights") - df.columns.get_loc(
        "grades") - 1  # finds number of courses
    start_of_courses_col = df.columns.get_loc("grades") + 1  # finds the col number where the courses start
    end_of_data_col = df.columns.get_loc(
        "weights") + n_courses + 1  # finds  the col number where the data end

    pos_gd = [*range(start_of_courses_col, start_of_courses_col + n_courses)]
    col_name_gd = df.columns[pos_gd]
    [df.rename(columns={col_name_gd[i]: (col_name_gd[i] + '_grade')}, inplace=True)  # renames grades
     for i in range(len(pos_gd))]
    pos_wt = [*range(start_of_courses_col + n_courses + 1, end_of_data_col)]
    col_name_wt = df.columns[pos_wt]
    [df.rename(columns={col_name_wt[i]: (col_name_wt[i][:len(col_name_wt[i]) - 2] + '_weight')}, inplace=True)
     for i in range(len(pos_wt))]  # renames weights

    # remove unused rows and columns
    df.drop(df.iloc[:, end_of_data_col:], inplace=True, axis=1)  # removes extra columns
    df.drop(columns=["grades", "weights"], inplace=True)  # removes grade and weight columns

    # convert file into list of dictionaries
    list_dict = df.to_dict('records')

    # create courses and weights keys
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
