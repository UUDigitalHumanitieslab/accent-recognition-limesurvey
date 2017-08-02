import os
def get_lines(file_ref):
    lines = []
    with open(file_ref, 'r') as f1:
        lines = [line for line in f1.readlines()]
    return lines

def create_folder(location):
    if not os.path.exists(location):
        os.makedirs(location)