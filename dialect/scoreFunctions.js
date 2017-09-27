function createFeedback(answers, givenAnswers, group, settings) {
    console.log(answers)
    console.log(givenAnswers)
    console.log(group)
    console.log(settings)
    $(document).ready(function () {

        for (question in givenAnswers[group]) {
            givenAnswers[group][question] = parseLonLatString(givenAnswers[group][question])

        }
        score = Math.round(calculateScoreFromGroups(answers, givenAnswers, group, settings) * 10) / 10
        $(".question-title-container").append(`<p class="ans-feedback"> Je eindcijfer is een ${score} (op een schaal van 0-10) <p>`)

    })
}

function calculateScore(answers, givenAnswers, settings) {
    total = 0;
    count = 0;
    for (ans in answers) {
        count += 1;
        total += calculateScoreOneAns(answers[ans], givenAnswers[ans], settings);
        console.log(total)
    }
    if (count === 0) {
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


function calculateScoreFromGroups(answers, givenAnswers, group, settings) {

    return calculateScore(answers[group], givenAnswers[group], settings)
}

function parseLonLatString(str) {
    /**
     * Parses a string containing lon lat information to a json object
     */

    ar = str.split(",");

    ar = ar.map(a => a.replace(/^\D+/g, ''));
    return {
        lat: parseFloat(ar[0]),
        lng: parseFloat(ar[1])
    }


}