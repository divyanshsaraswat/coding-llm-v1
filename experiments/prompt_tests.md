# Prompt Engineering Tests

## Objective
Test how the model responds to various types of coding prompts.

## Zero-Shot Tests

| Prompt | Expected Output | Actual Output | Observations |
| :--- | :--- | :--- | :--- |
| `def factorial(n):` | Standard recursive or iterative solution | | |
| `import matplotlib.pyplot as` | `plt` | | |
| `class User:` | `def __init__(self, ...):` | | |

## Few-Shot Tests

| Context (Few-Shot) | Prompt | Actual Output | Did it help? |
| :--- | :--- | :--- | :--- |
| (Provide 2 examples of adding numbers) | `def add(a, b):` | | |


## Automated Run Results


## Automated Run Results
| type          | prompt                      | expected                      | actual_output                                                                                           |
|:--------------|:----------------------------|:------------------------------|:--------------------------------------------------------------------------------------------------------|
| Zero-Shot     | def factorial(n):           | Recursive function            | def factorial(n):): exp while fa>>):,ductctalind):ase power):nge,):): s1:sort result count):):>fi[1:... |
| Zero-Shot     | import matplotlib.pyplot as | plt                           | import matplotlib.pyplot asrs//"in ex[](0,):ma nmanac]((nums c[. return range( find[bo 0 0talj[....     |
| Zero-Shot     | class User:                 | __init__ method               | class  ⁇ ser: result =(0, total result if ( result[er += result[list[irj]1))): n power rem"tur numsr... |
| Zero-Shot     | def is_palindrome(s):       | Check string reversal         | def is_palindrome(s): exp): if): i):ntnt rem): if c s[[1:]) lef fibonj ex(n tarsort count count +=(r... |
| Failure-Check | while True:                 | Infinite loop or break        | while True: +=spacesroddown n count_nums + total n return result = totalli): n in(0, count n result ... |
| Failure-Check | from sklearn.metrics import | Valid metric or Hallucination | from s ⁇ learn.metrics import result[posum result fib if n * sy *= *= = right n n return[0 nums for ... |