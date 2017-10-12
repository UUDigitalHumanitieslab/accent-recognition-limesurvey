"""
    Functions to transform the entries
"""
import json

def create_mapping(start_number, end_number):
    """
    Creates a dict containing the mapping between old questions and new questions
    example: v1004 -> v1
    :param start_number: the number to start with
    :return:
    """
    mapping = {}
    for i in range(end_number - start_number + 1):
        mapping["vr{}".format(start_number + i)] = "v{}".format(i+1)
    return mapping


def parse_entry(entry):
    """
        parses one entry:
        it removes redundant info:

        converts the following information:
            -vrxxx to vx
        Adds the following info:
            -vx_group
    :param entry: one entry of the survey
    :return: a new dictionary with the added info
    """
    new_ans = old_ans_to_new(entry)
    groups = add_groups(new_ans)
    new_entry = {**new_ans, **groups}
    remove_redundant_info(new_entry)
    return new_entry


def old_ans_to_new(entry):
    """
        Transforms the vrxxxx to vrx and adds vx_group to the entry
        (where x is a digit)
    :param entry:
    :return:
    """
    new_entry = {}
    mapping = create_mapping(1004, 10018)
    for (k,v) in entry.items():
        if "vr1" in k:
            new_entry[mapping[k]] = v
        else:
            new_entry[k] = v
    return new_entry

def add_groups(entry):
    """
    Adds the group to the entries
    :param entry:
    :return:
    """
    result = {}
    group_dict = json.loads(entry["intro"])
    print(group_dict)
    for (k, v) in group_dict.items():
        result["{}_group".format(k)] = v["group"]
    return result
def remove_redundant_info(entry):
    """
    Removes the redundant info:
        -intro
        -submitdate
        -lastpage
        -startlanguage
        -score
        -vrxxxxx
    :param entry:
    :return:
    """
    remove_keys = [
        "intro",
        "submitdate",
        "lastpage",
        "startlanguage",
        "Score",
    ]
    for key in remove_keys:
        if key in entry:
            del entry[key]




