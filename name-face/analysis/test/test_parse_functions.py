import unittest
from parse_functions import *

class TestParseFunctions(unittest.TestCase):
    def setUp(self):
        self.entry_1 = {'Eindvraag': 'Nee', 'Geslacht': 'vrouw', 'vr1017': 'Rinske', 'vr1013': 'Iris', 'opleiding': 'Other',
                   'vr1005': 'Sanne',
                   'intro': '{ "v5":{ "group":"B","answers":["Francisca","Hester","Malou","Gwen"]},"v12":{ "group":"A","answers":["Romy","Denise","Naomi","Sharon"]},"v4":{ "group":"A","answers":["Lex","Jort","Wout","Jip"]},"v15":{ "group":"B","answers":["Laura","Nynke","Maria","Jill"]},"v11":{ "group":"A","answers":["Pauline","Willemijn","Annemarie","Marissa"]},"v9":{ "group":"B","answers":["Anne","Maaike","Elisabeth","Joyce"]},"v1":{ "group":"B","answers":["Daan","Jelle","Willem","Mike"]},"v8":{ "group":"B","answers":["Ward","Jelte","Markus","Scott"]},"v3":{ "group":"A","answers":["Rens","Sem","Luc","Joep"]},"v14":{ "group":"B","answers":["Lana","Rinske","Theresia","Yentl"]},"v13":{ "group":"A","answers":["Jaap","Boris","Freek","Mart"]},"v2":{ "group":"B","answers":["Sanne","Femke","Kim","Johanna"]},"v7":{ "group":"A","answers":["Anyck","Valérie","Marie","Inez"]},"v6":{ "group":"A","answers":["Nadine","Amanda","Sabrina","Cynthia"]},"v10":{ "group":"A","answers":["Iris","Floor","Lieke","Vera"]}}',
                   'vr1007': 'Wout', 'lastpage': '19', 'vr1012': 'Anne', 'Score': '', 'vr1010': 'Valérie',
                   'vr1015': 'Sharon', 'startlanguage': 'en', 'vr1018': 'Nynke', 'leeftijd': '35',
                   'opleiding[other]': 'WO DUITSLAND', 'vr1016': 'Freek', 'id': '73', 'vr1009': 'Sabrina',
                   'vr1011': 'Ward', 'vr1014': 'Willemijn', 'vr1006': 'Joep', 'vr1004': 'Jelle', 'Geslacht[other]': '',
                   'submitdate': '1980-01-01 00:00:00', 'vr1008': 'Hester'}
        self.expected_entry = {
            'id': '73',
            'Geslacht': 'vrouw',
            'v1': 'Jelle',
            'v2': 'Sanne',
            'v3': 'Joep',
            'v4': 'Wout',
            'v5': 'Hester',
            'v6': 'Sabrina',
            'v7': 'Valérie',
            'v8': 'Ward',
            'v9': 'Anne',
            'v10': 'Iris',
            'v11': 'Willemijn',
            'v12': 'Sharon',
            'v13': 'Freek',
            'v14': 'Rinske',
            'v15': 'Nynke',
            'Geslacht[other]': '',
            'leeftijd': '35',
            'opleiding[other]': 'WO DUITSLAND',
            'opleiding': 'Other',
            'v1_group': 'B', 'v2_group': 'B', 'v3_group': 'A', 'v4_group': 'A', 'v5_group': 'B', 'v6_group': 'A',
            'v7_group': 'A', 'v8_group': 'B', 'v9_group': 'B', 'v10_group': 'A', 'v11_group': 'A',
            'v12_group': 'A', 'v13_group': 'A', 'v14_group': 'B', 'v15_group': 'B'
        }

    def test_parse_entry(self):
        self.maxDiff = None
        entry = parse_entry(self.entry_1)
        self.assertEqual(entry, self.expected_entry)


    def test_create_mapping(self):
        mapping = create_mapping(1004, 1010)
        expected = {
            "vr1004":"v1",
            "vr1005":"v2",
            "vr1006":"v3",
            "vr1007":"v4",
            "vr1008":"v5",
            "vr1009":"v6",
            "vr1010":"v7",
        }
        self.assertEqual(mapping, expected)

    def test_old_ans_to_new(self):
        old_ans = {
            "vr1004": "Jelle",
            "vr1005": "Sanne",
            "vr1006": "Joep",
        }
        expected_ans = {
            "v1": "Jelle",
            "v2": "Sanne",
            "v3": "Joep",
        }
        ans = old_ans_to_new(old_ans)
        self.assertEqual(ans, expected_ans)

    def test_add_group(self):
        entry = {
            "intro": '{"v5":{ "group":"B","answers":["Francisca","Hester","Malou","Gwen"]},"v12":{ "group":"A","answers":["Romy","Denise","Naomi","Sharon"]},"v4":{ "group":"A","answers":["Lex","Jort","Wout","Jip"]}}'
        }
        expected = {
            "v5_group": "B",
            "v12_group": "A",
            "v4_group": "A",
        }

        result = add_groups(entry)
        self.assertEqual(result, expected)

