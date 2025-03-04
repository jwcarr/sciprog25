Unit 1
======

Question 1
----------

What is the result of `5 * 8 + 40 / 2`?

- [x] 60.0
- [ ] 40.0
- [ ] 120


Question 2
----------

What is the result of `10 / 5`?

- [ ] 0.5
- [ ] 2
- [ ] DivisionError
- [x] 2.0


Question 3
----------

What is the result of `f"Ciao, {name * 3}!"` given that `name = "Pedro"`?

- [ ] 'Ciao, Pedro!Ciao, Pedro!Ciao, Pedro!'
- [x] 'Ciao, PedroPedroPedro!'
- [ ] 'Ciao, Pedro!Pedro!Pedro!'
- [ ] FormattingError


Question 4
----------

What is the result of `(1 == 2) == False`?

- [x] True
- [ ] False
- [ ] SyntaxError


Question 5
----------

Given the list of colors defined above, what is the result of `colors[2][1]`?

- [ ] 'red'
- [ ] 'green'
- [x] 'r'
- [ ] True


Question 6
----------

What's the difference between lists and dictionaries?

- [ ] Only dictionaries have indexes.
- [ ] Dictionaries can hold strings, while lists can only hold numbers.
- [ ] Lists and dictionaries are essentially the same.
- [x] Dictionary items are accessed by key and list items are accessed by index.


Question 7
----------

Which of these statements is wrong?

- [x] Each if-statement needs to be completed with an else clause.
- [ ] If-statements restrict a block of code to running only under certain conditions.
- [ ] If-statements modify the sequential flow of the program.
- [ ] Every if-statement contains an expression that is evaluated.


Question 8
----------

Given the for-loop `for number in range(10, 20):`, how many times would its associated code block be executed?

- [ ] 9
- [ ] 20
- [x] 10
- [ ] 2
- [ ] Unknown/unpredictable


Question 9
----------

In the first line, why is there a set of empty brackets?

- [ ] The brackets indicate that `numbers_divisible_by_3_and_7` is comprised of ints.
- [ ] The brackets are a requirement of while-loops.
- [x] The brackets create an empty list.


Question 10
-----------

How many times does the while-loop run?

- [ ] 100
- [x] 2100
- [ ] 99
- [ ] 2099
- [ ] Unknown/unpredictable


Question 11
-----------

Why is `current_number += 1` not inside the if-statement? (warning: putting this line inside the if-statement will result in an infinite loop! Why?)

- [ ] The `+=` operator is syntactically part of the while-loop, so it cannot appear within the if-statement.
- [x] We want to increment `number_to_check` on every iteration of the while-loop, regardless of whether the if-statement's condition is met.
- [ ] Placing `current_number += 1` inside the if-statement is optional and a matter of personal preference.


Question 12
-----------

What happens if you change `and` to `or` in the if-statement? How does this change the resulting numbers?

- [x] The `or` condition is less restrictive than `and`, so we find 100 numbers more quickly.
- [ ] While-loops cannot be used with an `or`-based condition.
- [ ] Using `or` results in an infinite loop because it's possible for both conditions to be true at the same time.


Question 13
-----------

How would you modify the code to find numbers that are also divisible by five?

- [ ] `if number_to_check % 3 == 0 and % 7 == 0 and % 5 == 0:`
- [ ] `if number_to_check % 3 == 0 or number_to_check % 7 == 0 or number_to_check % 5 == 0:`
- [ ] `if number_to_check % 3 == 0 and number_to_check % 7 == 0 or number_to_check % 5 == 0:`
- [x] `if number_to_check % 3 == 0 and number_to_check % 7 == 0 and number_to_check % 5 == 0:`


Unit 2
======

Question 1
----------

Given that `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, what would the result of the following expression be: `max(numbers[0:5]) + min(numbers[5:10])`?

- [ ] 9
- [ ] 10
- [x] 11
- [ ] 12


Question 2
----------

What is the result of `sorted(['blue', 'red', 'green', 'yellow', 'black'])[-1]`?

- [ ] ['blue', 'black', 'green', 'red', 'yellow']
- [ ] ['black', 'blue', 'green', 'red', 'yellow']
- [ ] ['yellow', 'red', 'green', 'blue', 'black']
- [x] 'yellow'
- [ ] 'black'


Question 3
----------

What is the result of the following: `colors = ['blue', 'red', 'green', 'yellow', 'black']; shuffle(colors); print(colors[0])`?

- [ ] 'blue'
- [ ] 'red'
- [ ] 'green'
- [ ] 'yellow'
- [ ] 'black'
- [x] Unknown/unpredictable


Question 4
----------

Which of the following statements is incorrect?

- [ ] It is possible to write Python code without any functions.
- [x] Using a function makes your code run faster.
- [ ] Functions help organize code into discrete chunks.
- [ ] All functions have a return value.


Question 5
----------

Given the above function definition, would is the result of `raise_x_to_y(2, 2 * 8)`?

- [ ] 16
- [ ] 32
- [x] 65536


Question 6
----------

True or false? A function must take at least one argument.

- [ ] True
- [x] False 


Question 7
----------

True or false? A function will always return the same output if it is given the same input.

- [ ] True
- [x] False


Question 8
----------

What is the result of `colors = ['blue', 'red', 'green', 'yellow', 'black']; sorted_colors = colors.sort(); print(sorted_colors)`?

- [ ] ['black', 'blue', 'green', 'red', 'yellow']
- [ ] ['blue', 'red', 'green', 'yellow', 'black']
- [ ] TypeError
- [x] None


Question 9
----------

What is the result of `'hello world'.split(' ')[0]`?

- [x] 'hello'
- [ ] 'h'
- [ ] ['hello', 'world']
- [ ] ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']


Question 10
-----------

Which of these statements is incorrect?

- [ ] A collection of related functions can be organized together in a class.
- [ ] Functions must be declared before they can be used.
- [x] The `sum()` function has to be imported from the `math` module before it can be used.
- [ ] A given function is allowed to call itself.
