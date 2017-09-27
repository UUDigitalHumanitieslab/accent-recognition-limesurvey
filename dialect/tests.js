QUnit.test("Calculate the score", function (assert) {

    answers = {
        "Q1": {
            lat: 1,
            lng: 1
        },
        "Q2": {lat: 50, lng: 3},
        "Q3": {lat: 50, lng: 3}
    };

    givenAnswers = {
        "Q1": {
            lat: 1,
            lng: 1
        },
        "Q2": {lat: 50, lng: 2.5},
        "Q3": {lat: 60, lng: 2.5}
    };
    settings = {
        "goodAnsRange": 20,
        "totallyWrong": 100
    };

    result = calculateScore(answers, givenAnswers, settings);
    expected = 6.05;
    assert.ok(Math.abs(result - expected) < 0.1, `${result} appr. equals ${expected}`)
});

QUnit.test("Calculate the score with 70km = 7", function(assert){
    answers = {
    "Q1": {
      lat: 52.091801,
        lng:5.114656
    }
    };

    givenAnswers = {
        "Q1": {
            lat: 52.384455,
            lng: 6.030658
        }
    };
    settings = {
        "goodAnsRange": 20,
        "totallyWrong": 185
    };
    result = calculateScore(answers, givenAnswers, settings);
    expected = 7;
    assert.ok(Math.abs(result - expected) < 0.1, `${result} appr. equals ${expected}`)
});

function testCalculateScoreOneAns(ans, givenAns, expected, settings, assert) {
    result = calculateScoreOneAns(ans, givenAns, settings);
    assert.ok(Math.abs(result - expected) < 0.1, `${result} appr. equals ${expected}`)

}

QUnit.test("Calculate score one function", function (assert) {

    settings = {
        "goodAnsRange": 20,
        "totallyWrong": 100
    };

    cases = [
        [
            {"lat": 1, "lng": 1},
            {"lat": 1, "lng": 1},
            10
        ],
        [
            {"lat": 50, "lng": 3},
            {"lat": 50, "lng": 2.9},
            10
        ],
        [
            {"lat": 50, "lng": 3},
            {"lat": 50, "lng": 2.5},
            8, 125
        ],
        [
            {"lat": 50, "lng": 3},
            {"lat": 60, "lng": 2.5},
            0
        ],
    ];

    for (c in cases) {
        ans = cases[c][0];
        givenAns = cases[c][1];
        testCalculateScoreOneAns(ans, givenAns, cases[c][2], settings, assert)
    }

});

QUnit.test("Calculate score from groups", function (assert) {
        answers = {
            1: {
                "Q1": {
                    lat: 1,
                    lng: 1
                },
                "Q2": {lat: 50, lng: 3},
                "Q3": {lat: 50, lng: 3}
            },

            2: {},
            3: {},
            4: {}

        };

        givenAnswers = {
            1:{
               "Q1": {
                lat: 1,
                lng: 1
            },
            "Q2": {lat: 50, lng: 2.5},
            "Q3": {lat: 60, lng: 2.5}
            }

        };
        settings = {
            "goodAnsRange": 20,
            "totallyWrong": 100
        };

        group = 1;

        result = calculateScoreFromGroups(answers, givenAnswers, group, settings);
        expected = 6.05;
        assert.ok(Math.abs(result - expected) < 0.1, `${result} appr. equals ${expected}`)
    }
);

QUnit.test("Parse a lon, lat string", function(assert){
    s = '{"lat": 5.6, "lng": 10.9}';
    expected = {
        lat: 5.6,
        lng: 10.9
    };

    result = parseLonLatString(s);
    console.log(expected)
    console.log(result)
    assert.ok(expected["lng"] == result["lng"])
    assert.ok(expected["lat"] == result["lat"])

})