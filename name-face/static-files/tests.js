QUnit.test( "make selection", function( assert ) {
    var input = {
        "v1": {
            "A": [
                "a",
                "b",
                "c"
            ],
            "B": [
                "d",
                "e",
                "f"
            ],
            "realName": 'Daan'
        },
    }

    var output = makeSelection(input);
    var selectionV1 = output["v1"];
    assert.ok(selectionV1.group === "A" || selectionV1.group === "B");
    assert.deepEqual(selectionV1.answers, selectionV1.group === "A" ? ['Daan', 'a', 'b', 'c'] : ['Daan', 'd', 'e', 'f'])
});
var questions = {
        "v1": {
            "A": [
                "a",
                "b",
                "c"
            ],
            "B": [
                "d",
                "e",
                "f"
            ],
            "realName": 'Daan'
        },
        "v2": {
            "A": [
                "a",
                "b",
                "c"
            ],
            "B": [
                "d",
                "e",
                "f"
            ],
            "realName": 'Bert'
        },
    };

    var answers = {
        "v1": "a",
        "v2": "Bert"
    };

QUnit.test( "format selection", function(assert){
    var input = {
            "A": [
                "a",
                "b",
                "c"
            ],
            "B": [
                "d",
                "e",
                "f"
            ],
            "realName": 'Daan'
        }

    var output = formatSelection(input, "A");
    assert.deepEqual(output, {group: "A", answers: ['Daan', 'a', 'b', 'c']})
})

QUnit.test("Calculate Score", function(assert){


    var output = calculateScore(questions, answers);
    assert.equal(output, 0.5)
});

QUnit.test("Get feedback", function(assert){

    var output = getFeedback(questions, answers);
    assert.equal(output, "Je hebt beter gekozen dan kans")
})