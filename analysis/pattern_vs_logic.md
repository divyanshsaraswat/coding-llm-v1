# Pattern Matching vs. Logical Reasoning

## The Hypothesis
LLMs are excellent at **Pattern Matching** (repeating boilerplate, standard algorithms) but struggle with **Logical Reasoning** (tracking state changes across many lines).

## Evidence

### Pattern Matching Success
*   Writing a standard configured dictionary.
*   Implementing a common meaningful variable name.
*   Closing parenthesis correctly.

### Logical Reasoning Failure
*   Modifying a variable inside a loop and using it correct afterwards if the loop logic is complex.
*   Understanding the side effects of a function call that isn't defined in the immediate context.
