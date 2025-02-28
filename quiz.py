from IPython.display import display, HTML

_js_submission_script = """
<script>
function submitAnswer(questionId) {
    var selectedAnswer = document.querySelector(`input[name="answer-${questionId}"]:checked`);
    if (!selectedAnswer) {
        document.getElementById(`response-message-${questionId}`).innerText = "Please select an answer.";
        return;
    }
    var data = {
        question: `${questionId}`,
        answer: selectedAnswer.value
    };
    fetch("https://joncarr.net/sciprog_submit.php", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`response-message-${questionId}`).innerText = "Answer submitted!";
        document.getElementById(`button-${questionId}`).setAttribute("disabled", "disabled");
    })
    .catch(error => {
        document.getElementById(`response-message-${questionId}`).innerText = "Error submitting answer.";
    });
}
</script>
"""

_unit1_questions = [

    _js_submission_script + """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>What is the result of <code>5 * 8 + 40 / 2</code>?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> 60.0</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> 40.0</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> 120</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>What is the result of <code>10 / 5</code>?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> 0.5</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> 2</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> DivisionError</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> 2.0</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>What is the result of <code>f"Ciao, {name * 3}!"</code> given that <code>name = "Pedro"</code>?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> 'Ciao, Pedro!Ciao, Pedro!Ciao, Pedro!'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> 'Ciao, PedroPedroPedro!'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> 'Ciao, Pedro!Pedro!Pedro!'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> FormattingError</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>What is the result of <code>(1 == 2) == False</code>?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> True</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> False</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> SyntaxError</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p><p>Given the list of colors defined above, what is the result of <code>colors[2][1]</code>?</p></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> 'red'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> 'green'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> 'r'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> True</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>What's the difference between lists and dictionaries?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> Only dictionaries have indexes.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> Dictionaries can hold strings, while lists can only hold numbers.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> Lists and dictionaries are essentially the same.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> Dictionary items are accessed by key and list items are accessed by index.</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>Which of these statements is wrong?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> Each if-statement needs to be completed with an else clause.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> If-statements restrict a block of code to running only under certain conditions.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> If-statements modify the sequential flow of the program.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> Every if-statement contains an expression that is evaluated.</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>Given the for-loop <code>for number in range(10, 20):</code>, how many times would its associated code block be executed?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> 9</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> 20</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> 10</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> 2</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="e"> Unknown/unpredictable</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>In the first line, why is there a set of empty brackets?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> The brackets indicate that <code>numbers_divisible_by_3_and_7</code> is comprised of ints.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> The brackets are a requirement of while-loops.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> The brackets create an empty list.</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>How many times does the while-loop run?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> 100</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> 2100</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> 99</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> 2099</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="e"> Unknown/unpredictable</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>Why is <code>current_number += 1</code> not inside the if-statement? (warning: putting this line inside the if-statement will result in an infinite loop! Why?)</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> The <code>+=</code> operator is syntactically part of the while-loop, so it cannot appear within the if-statement.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> We want to increment <code>number_to_check</code> on every iteration of the while-loop, regardless of whether the if-statement's condition is met.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> Placing <code>current_number += 1</code> inside the if-statement is optional and a matter of personal preference.</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>What happens if you change <code>and</code> to <code>or</code> in the if-statement? How does this change the resulting numbers?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> The <code>or</code> condition is less restrictive than <code>and</code>, so we find 100 numbers more quickly.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> While-loops cannot be used with an <code>or</code>-based condition.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> Using <code>or</code> results in an infinite loop because it's possible for both conditions to be true at the same time.</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>How would you modify the code to find numbers that are also divisible by five?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> <code>if number_to_check % 3 == 0 and % 7 == 0 and % 5 == 0:</code></label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> <code>if number_to_check % 3 == 0 or number_to_check % 7 == 0 or number_to_check % 5 == 0:</code></label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> <code>if number_to_check % 3 == 0 and number_to_check % 7 == 0 or number_to_check % 5 == 0:</code></label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> <code>if number_to_check % 3 == 0 and number_to_check % 7 == 0 and number_to_check % 5 == 0:</code></label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

]

_unit2_questions = [



]

_unit3_questions = [



]

_unit4_questions = [



]

_unit5_questions = [



]

_unit1_questions = [
    q.replace("QUESTION_NUMBER", str(i)).replace("UNIT_NUMBER", "1")
    for i, q in enumerate(_unit1_questions, 1)
]
_unit2_questions = [
    q.replace("QUESTION_NUMBER", str(i)).replace("UNIT_NUMBER", "2")
    for i, q in enumerate(_unit2_questions, 1)
]
_unit3_questions = [
    q.replace("QUESTION_NUMBER", str(i)).replace("UNIT_NUMBER", "3")
    for i, q in enumerate(_unit3_questions, 1)
]
_unit4_questions = [
    q.replace("QUESTION_NUMBER", str(i)).replace("UNIT_NUMBER", "4")
    for i, q in enumerate(_unit4_questions, 1)
]
_unit5_questions = [
    q.replace("QUESTION_NUMBER", str(i)).replace("UNIT_NUMBER", "5")
    for i, q in enumerate(_unit5_questions, 1)
]
