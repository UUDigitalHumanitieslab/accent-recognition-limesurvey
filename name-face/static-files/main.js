var ROOT =  "https://dhstatic.hum.uu.nl/name-face/";
//
var imgDimensions = [300, 450];

//Questions structure: {Question_id : {A: [name1, name2, name3], B: [name1, name2, name3], realName: name}, Question_id2: ....}

/**
 *
 * @param questions, json containing questions, a question has the following structure:
 * {Question_id : {A: [name1, name2, name3], B: [name1, name2, name3], realName: name}
 * @Output json containing a selection for each question. selection has the following structure:
 * {Question_id: {group: selectedGroup, answers: [realName, namex, namey, namex]}
 */
function makeSelection(questions){
    var results = {};
    var groupA = "A";
    var groupB = "B";
    var nrOfQuestions = Object.keys(questions).length;
    var selection = [];
    for(var i = 0; i < Math.ceil(nrOfQuestions/2.0); i++){
        selection.push(groupA);
        selection.push(groupB);
    }
    shuffle(selection);
    var j = 0;
    for (var question in questions){
        results[question] = formatSelection(questions[question], selection[j]);
        j++;
    }
    return results;
}



/**
 *
 * @param question, json describing a question. see make selection for structure
 *
 */
function formatSelection(question, selectedGroup){
    return {
        group: selectedGroup,
        answers: [question.realName].concat(question[selectedGroup])
    }
}


function showScore(questions, givenAnswers){
    var feedback = getFeedback(questions, givenAnswers);
    var questionContainer = $('.question-title-container');
    var answerContainer = $('.answer-container');
    answerContainer.find(':first-child').hide();
    questionContainer.append(`<div class="feedback">${feedback}</div>`);
}

/**
 * Gives feedback on how well the user did
 * @param questions the questions
 * @param givenAnswsers the answers that the user gave
 */
function getFeedback(questions, givenAnswers){
    var msg = "";
    score = calculateScore(questions, givenAnswers)
    if(score >= 6){
        msg = "Je hebt beter gekozen dan kans."
    } else {
        msg = "Je hebt niet boven kans gekozen."
    }
    return msg;
}

/**
 *  Calculates the score of the user
 *
 */
function calculateScore(questions, givenAnswers){
    totalCorrect = 0
    for(i in givenAnswers){
        if(givenAnswers[i] == questions[i]["realName"]){
            totalCorrect++;
        }

    }
    return totalCorrect

}


function shuffle (array) {
    var i = 0
        , j = 0
        , temp = null

    for (i = array.length - 1; i > 0; i -= 1) {
        j = Math.floor(Math.random() * (i + 1))
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
    }


}

/**
 * Add spaces after the '{' symbol
 * @param str
 * @returns {string}
 */
function addSpaces(str){
    result = "";
    for(n in str){
        s = str[n];
        result += s == "{" ? "{ " : s
    }
    return result
}

function generateRadioInput(str){
    return  ` <div class="ans-style"><input type="radio" class="ans-option" name="ans" value="${str}">${str}</div><br> `
}

function arrayToStr(ar){
    var str = '';
    for (var el in ar){
        str += ar[el]
    }

    return str
}



function generateQuestion(questionId, selection){
    console.log(selection);
    var answerContainer = $('.answer-container');
    answerContainer.find(':first-child').hide();
    answerContainer.append(`
<div class="col-sm-4 col-sm-offset-2"><img src='${ROOT}img/${questionId}.jpg' width=${imgDimensions[0]} height=${imgDimensions[1]}></div>
`)
    //Put the answers in the question
    var answers = selection['answers']
    shuffle(answers)
    radioButtons = answers.map(generateRadioInput);
    answerContainer.append(`
        <form action="">
        <div>
          ${arrayToStr(radioButtons)}
         </div>
        </form>
    `)

    $(".ans-option").click(function(el){
        $('.textarea').val(el.currentTarget.value)
    })
}

