# Propositional Logic Truth Table Generator

## Overview

This Java program generates truth tables for logical expressions using propositional logic. It supports logical operations such as `AND`, `OR`, `NOT`, `→` (implication), and `↔` (biconditional). The program converts infix expressions (expressions with parentheses and operators in their natural order) into postfix notation using the **Shunting Yard Algorithm**, making it easier to evaluate and generate the truth table correctly.

## Features

- **Logical Operations**: Supports conjunction (`AND`), disjunction (`OR`), negation (`NOT`), implication (`→`), and biconditional (`↔`).
- **Parentheses and Precedence Handling**: Properly handles nested parentheses and respects operator precedence to evaluate complex expressions correctly.
- **Dynamic Variable Handling**: Supports up to 26 variables (`A` through `Z`), allowing for flexibility in expression length.
- **Console Output**: Displays a neatly formatted truth table directly in the console.

## How It Works

1. **Expression Input**: The user inputs a logical expression using variables (`A`, `B`, `C`, etc.) and logical operators (`AND`, `OR`, `NOT`, `→`, `↔`). The expression should be written in infix notation (e.g., `( A AND B ) OR C`).
2. **Variable Count**: The user specifies the number of variables used in the expression. This allows the program to dynamically generate all possible combinations of truth values for the given variables.
3. **Conversion to Postfix**: The program uses the **Shunting Yard Algorithm** to convert the infix expression into postfix notation, respecting parentheses and operator precedence.
4. **Truth Table Generation**: The program evaluates the expression for every combination of truth values and displays the results in a properly formatted truth table.

## Getting Started

### Prerequisites

- Java Development Kit (JDK) installed on your system.
- A Java IDE (e.g., IntelliJ IDEA, Eclipse) or any text editor for editing and running the code.

### Running the Program

1. **Clone or Download** the repository containing this Java file.
2. **Compile the Java file** using a terminal or an IDE:
   ```bash
   javac PropositionalLogic.java
   ```
3. **Run the program**:
   ```bash
   java PropositionalLogic
   ```
4. **Follow the prompts**:
   - Enter a logical expression using variables (`A`, `B`, etc.) and operators (`AND`, `OR`, `NOT`, `->`, `<->`).
   - Enter the number of variables used in your expression (e.g., `2` for `A` and `B`).

### Example Usage

#### Input:
```
Enter a logical expression (e.g., '( A AND B ) OR C' or 'A -> ( B AND C )'):
( A AND B ) OR ( C -> A )
Enter the number of variables in your expression (e.g., 2 for A, B):
3
```

#### Output:
```
A	B	C	Result
----------------------
T	T	T	T
T	T	F	T
T	F	T	T
T	F	F	T
F	T	T	F
F	T	F	T
F	F	T	F
F	F	F	T
```

## Supported Logical Operators

- **Conjunction (`AND`)**: True when both operands are true.
- **Disjunction (`OR`)**: True when at least one of the operands is true.
- **Negation (`NOT`)**: True when the operand is false.
- **Implication (`->`)**: True unless the first operand is true and the second operand is false.
- **Biconditional (`<->`)**: True when both operands are the same (either both true or both false).

### Important Notes

- The program expects logical operators in all caps (`AND`, `OR`, `NOT`, `->`, `<->`).
- Ensure variables are capital letters (`A`, `B`, `C`, etc.) and are within the number of variables you specify.

## Extending the Program

You can extend this program by:
- Adding more logical operators if needed (e.g., `NAND`, `NOR`).
- Enhancing the parser to handle user errors gracefully.
- Adding a GUI for better user interaction using JavaFX.

## Troubleshooting

- **Incorrect Variable Count**: Make sure you enter the number of variables correctly. For example, if you use variables `A`, `B`, and `C` in your expression, enter `3` as the variable count.
- **Invalid Expression**: Ensure that your expression follows the format expected by the program and uses the supported logical operators and variables.

## Author

- Ali Ladak