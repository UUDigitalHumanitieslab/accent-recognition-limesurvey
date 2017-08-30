function createFeedback(answers, givenAnswers, settings) {
    $(document).ready(function(){
        score = Math.round(calculateScore(answers, givenAnswers, settings) * 10) / 10
        $(".question-title-container").append(`Your score is a ${score} out of 10`)

    })
}

function calculateScore(answers, givenAnswers, settings) {
    total = 0;
    count = 0;
    for (ans in answers) {
        count += 1;
        total += calculateScoreOneAns(answers[ans], givenAnswers[ans], settings);
    }
    if (count == 0) {
        return 0;
    }
    return total / count
}


function calculateScoreOneAns(answer, givenAnswer, settings) {
    distance = distanceBetweenAns(answer, givenAnswer);
    min = settings["goodAnsRange"];
    max = settings["totallyWrong"];
    if (distance < min) {
        return 10
    } else if (distance > max) {
        return 0
    } else {
        return 10 - (distance - min) / (max - min) * 10
    }
}