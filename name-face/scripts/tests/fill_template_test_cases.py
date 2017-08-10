fill_template_test_cases = [
    {
        "template_ref": "tests/fill_templates/fill_test_1.mako",
        "json": {"questions": ["Q", "Q", "Q"], "survey_id": "1"},
        "output_location": "tests/result/fill_template/fill_test_1.txt",
        "expected_file_ref": "tests/expected/fill_template/fill_test_1.txt"
    },
    {
        "template_ref": "groups.mako",
        "json": {"questions": [ i for i in range(2)], "starting_group_id": 1001, "survey_id": "1"},
        "output_location": "tests/result/fill_template/groups.txt",
        "expected_file_ref": "tests/expected/fill_template/groups.txt"
    },
    {
        "template_ref": "questions.mako",
        "json": {"questions": [i for i in range(2)],
                 "question_js_file_ref": "https://localhost:3000/example_names.js",
                 "starting_question_id": 12996,
                 "starting_group_id": 1086,
                 "survey_id": 9,
                 "main_js_file_ref": "https://localhost:3000/main.js"
                 },
        "output_location": "tests/result/fill_template/questions.txt",
        "expected_file_ref": "tests/expected/fill_template/questions.txt"
    }


]