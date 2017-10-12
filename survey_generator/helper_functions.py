import os
import re

def get_lines(file_ref):
    """
    Get the lines out of a file and puts it into a list
    :param file_ref:
    :return:
    """
    lines = []
    with open(file_ref, 'r') as f1:
        lines = [line for line in f1.readlines()]
    return lines

def create_folder(location):
    """
    Creates a folder at the given location
    """
    if not os.path.exists(location):
        os.makedirs(location)

def remove_white_lines(string):
    """
    removes all the white lines from a string and returns the result
    :param string:
    :return:
    """
    string = remove_leading_white_lines(string)
    expr = "\n\s*\n"
    string = re.sub(expr, "\n", string)

    return remove_trailing_white_spaces(string)


def remove_leading_white_lines(string):
    """
    Removes the leading white lines
    :param string:
    :return:
    """
    expr =  "^\s*\n"
    if re.match(expr, string):
        string = re.sub(expr, "", string)
        return remove_leading_white_lines(string)
    else:
        return string

def remove_trailing_white_spaces(string):
    """
    Removes the trailing white spaces
    :param string: A string from which the trailing white spaces should be removed
    :return:
    """
    if len(string) == 0:
        return string
    if string[len(string)-1] == " ":
        return remove_trailing_white_spaces(string[:-1])
    else:
        return string

