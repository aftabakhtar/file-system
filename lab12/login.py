"""
Check the user entered credentials to validate.
Returns boolean based on correction of the entered
credentials.
"""
import csv


def validate_login(username, password):
    """
    Checks if the username and password entered are
    correct.
    Takes username and password strings.
    returns a boolean
    """
    with open('users.csv') as csv_file:
        user_data = csv.reader(csv_file, delimiter=',')

        for data_row in user_data:
            if username == data_row[0] and password == data_row[1]:
                return True

    return False
