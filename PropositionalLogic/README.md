# Propositional Logic Truth Table Generator

A Java application that generates truth tables for propositional logic expressions. The program converts infix logical expressions to postfix notation and evaluates them for all possible truth value combinations.

## Features

- **Logical Operations**: Supports AND, OR, NOT, implication (→), and biconditional (↔)
- **Expression Parsing**: Converts infix expressions to postfix using the Shunting Yard algorithm
- **Truth Table Generation**: Automatically generates complete truth tables for any valid expression
- **Multiple Variables**: Supports expressions with multiple propositional variables (A, B, C, etc.)

## Supported Operators

| Operator | Symbol | Description | Precedence |
|----------|--------|-------------|------------|
| NOT | `NOT` | Logical negation | 3 (highest) |
| AND | `AND` | Logical conjunction | 2 |
| OR | `OR` | Logical disjunction | 1 |
| Implication | `->` | If-then conditional | 0 |
| Biconditional | `<->` | If and only if | 0 (lowest) |

## Usage

### Running the Program

```bash
javac PropositionalLogic.java
java PropositionalLogic
```

### Input Format

1. **Expression**: Enter your logical expression using the supported operators
2. **Variables**: Specify the number of variables in your expression

**Important Notes:**
- Variables must be single uppercase letters (A, B, C, etc.)
- Use spaces to separate all tokens in the expression
- Parentheses are supported for grouping operations

### Example Usage

```
Enter a logical expression (e.g., '( A AND B ) OR C' or 'A -> ( B AND C )'):
( A AND B ) OR C
Enter the number of variables in your expression (e.g., 2 for A, B):
3
```

**Output:**
```
A	B	C	Result
-----------------
T	T	T	T
T	T	F	T
T	F	T	T
T	F	F	F
F	T	T	T
F	T	F	F
F	F	T	T
F	F	F	F
```

## Sample Expressions

### Basic Operations
- `A AND B` (2 variables)
- `A OR B` (2 variables)
- `NOT A` (1 variable)

### Complex Expressions
- `( A AND B ) OR C` (3 variables)
- `A -> ( B AND C )` (3 variables)
- `( A OR B ) <-> ( C AND D )` (4 variables)
- `NOT ( A AND B ) OR C` (3 variables)

### Conditional Logic
- `A -> B` (If A then B)
- `A <-> B` (A if and only if B)
- `( A -> B ) AND ( B -> A )` (Equivalent to A <-> B)

## How It Works

1. **Expression Parsing**: The program uses the Shunting Yard algorithm to convert infix notation to postfix notation
2. **Truth Value Generation**: Creates all possible combinations of truth values for the specified number of variables
3. **Expression Evaluation**: Evaluates the postfix expression for each combination using a stack-based approach
4. **Table Display**: Formats and displays the results in a clear truth table format

## Technical Details

### Algorithm Components
- **Shunting Yard Algorithm**: Converts infix to postfix notation with proper operator precedence
- **Stack-based Evaluation**: Efficiently evaluates postfix expressions
- **Truth Table Generation**: Systematically generates all 2^n combinations for n variables

### Operator Precedence (Highest to Lowest)
1. NOT (unary negation)
2. AND (conjunction)
3. OR (disjunction)
4. -> and <-> (implication and biconditional)

## Limitations

- Variables must be single uppercase letters (A, B, C, etc.)
- Variables must be consecutive starting from A
- Limited error handling for malformed expressions
- No support for custom variable names

## Requirements

- Java 8 or higher
- No external dependencies required

## Example Applications

This tool is useful for:
- **Logic Course Assignments**: Verify truth tables for homework problems
- **Digital Circuit Design**: Analyze boolean expressions
- **Formal Logic Study**: Understand logical equivalences
- **Computer Science**: Study propositional logic fundamentals

## Future Enhancements

Potential improvements could include:
- Better error handling and input validation
- Support for custom variable names
- GUI interface
- Export functionality for truth tables
- Support for logical equivalence checking
- Tautology and contradiction detection

## License

This project is open source and available under standard educational use terms.

---

*For questions or suggestions, please refer to the source code comments or create an issue in the project repository.*