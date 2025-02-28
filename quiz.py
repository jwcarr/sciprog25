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

    _js_submission_script + """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>Given that <code>numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</code>, what would the result of the following expression be: <code>max(numbers[0:5]) + min(numbers[5:10])</code>?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> 9</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> 10</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> 11</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> 12</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>What is the result of <code>sorted(['blue', 'red', 'green', 'yellow', 'black'])[-1]</code>?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> ['blue', 'black', 'green', 'red', 'yellow']</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> ['black', 'blue', 'green', 'red', 'yellow']</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> ['yellow', 'red', 'green', 'blue', 'black']</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> 'yellow'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="e"> 'black'</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>What is the result of the following: <code>colors = ['blue', 'red', 'green', 'yellow', 'black']; shuffle(colors); print(colors[0])</code>?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> 'blue'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> 'red'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> 'green'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> 'yellow'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="e"> 'black'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="f"> Unknown/unpredictable</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>Which of the following statements is incorrect?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> It is possible to write Python code without any functions.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> Using a function makes your code run faster.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> Functions help organize code into discrete chunks.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> All functions have a return value.</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>Given the above function definition, would is the result of <code>raise_x_to_y(2, 2 * 8)</code>?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> 16</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> 32</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> 65536</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>True or false? A function must take at least one argument.</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> True</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> False </label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>True or false? A functions will always return the same output if it is given the same input.</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> True</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> False</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>What is the result of <code>colors = ['blue', 'red', 'green', 'yellow', 'black']; sorted_colors = colors.sort(); print(sorted_colors)</code>?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> ['black', 'blue', 'green', 'red', 'yellow']</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> ['blue', 'red', 'green', 'yellow', 'black']</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> TypeError</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> None</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>What is the result of <code>'hello world'.split(' ')[0]</code>?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> 'hello'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> 'h'</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> ['hello', 'world']</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

    """
    <div id="question-UNIT_NUMBER-QUESTION_NUMBER">
        <p>Which of these statements is incorrect?</p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="a"> A collection of related functions can be organized together in a class.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="b"> Functions must be declared before they can be used.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="c"> The <code>sum()</code> function has to be imported from the <code>math</code> module before it can be used.</label></p>
        <p><label><input type="radio" name="answer-UNIT_NUMBER-QUESTION_NUMBER" value="d"> A given function is allowed to call itself.</label></p>
        <p><button id="button-UNIT_NUMBER-QUESTION_NUMBER" onclick="submitAnswer(questionId='UNIT_NUMBER-QUESTION_NUMBER')">Submit</button></p>
        <p id="response-message-UNIT_NUMBER-QUESTION_NUMBER"></p>
        <hr />
    </div>
    """,

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
