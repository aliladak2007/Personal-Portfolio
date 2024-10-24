# Scientific Calculator Application

## Overview
The **Scientific Calculator Application** is a JavaFX-based calculator that supports both basic arithmetic operations and advanced scientific functions such as trigonometric, hyperbolic, logarithmic, and exponential functions. The application is designed with a user-friendly GUI and maintains a history of calculations.

## Features
- **Basic Arithmetic Operations**: Addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Scientific Functions**:
  - Trigonometric functions: `sin`, `cos`, `tan` (input in degrees).
  - Inverse trigonometric functions: `asin`, `acos`, `atan` (output in degrees).
  - Hyperbolic functions: `sinh`, `cosh`, `tanh`.
  - Logarithmic functions: `log` (base 10) and `ln` (natural logarithm).
  - Square root (`√`), exponential (`exp`), and power (`^`).
- **Utility Functions**:
  - **Toggle Sign**: Switches between positive and negative for the current value.
  - **Decimal**: Adds a decimal point to the current input.
  - **Clear**: Clears the current input and resets the calculator.
- **Calculation History**: A list view showing the history of past calculations.

## Installation
To run the application, you need to have **Java JDK 11** or later and **JavaFX** installed on your system. Make sure your environment is set up correctly for JavaFX.

### Steps
1. Clone this repository or download the project files.
2. Open the project in your favorite Java IDE (e.g., IntelliJ IDEA or Eclipse).
3. Make sure to configure the JavaFX library path if necessary:
   - Add the JavaFX library files to your project's module path.
   - Update VM options with:
     ```
     --module-path <path_to_javafx_lib> --add-modules javafx.controls,javafx.fxml
     ```
4. Run the `CalculatorApp` class to start the application.

## Usage
- **Entering Numbers**: Click on the number buttons to enter digits. Click on the decimal button (`.`) to add a decimal point.
- **Basic Operations**: Click on any of the arithmetic operation buttons (`+`, `-`, `*`, `/`) to perform an operation. Press the equals button (`=`) to get the result.
- **Scientific Functions**: Use the function buttons (`sin`, `cos`, `log`, etc.) for scientific calculations.
- **Clearing the Input**: Press `C` to clear the display.
- **Viewing History**: The calculation history is displayed on the right side of the application.

## How It Works
- **Input Handling**: The application accepts number inputs and arithmetic operations. When an operator is pressed, the current number is stored, and the calculator waits for the next number input before performing the operation.
- **Scientific Calculations**: Scientific functions like `sin` and `log` are applied to the current input when their respective buttons are pressed.
- **History**: Each calculation is recorded and displayed in the history list. Clicking on an item in the history does not affect the current calculation.

## Code Structure
- **Main Class**: `CalculatorApp` — This is the main entry point for the application.
- **Methods**:
  - `appendNumber(int number)`: Appends a number to the display.
  - `setOperator(String op)`: Sets the operator for the calculation.
  - `applyFunction(String func)`: Applies a scientific function to the current input.
  - `calculate()`: Performs the calculation based on the stored operator and operands.
  - `clear()`: Clears the display and resets the calculator state.
  - `toggleSign()`: Toggles the sign of the current input.
  - `addHistory(String entry)`: Adds the calculation entry to the history list.

## Requirements
- **Java**: JDK 11 or later.
- **JavaFX**: Make sure JavaFX SDK is correctly set up in your project.

## Known Issues
- The calculator currently does not support parentheses or complex expressions involving multiple operators. Future updates may include such features.

## Future Improvements
- **Support for Parentheses**: Allowing users to input expressions with parentheses.
- **Graphing Functions**: Adding a feature to graph functions entered by the user.
- **Advanced Error Handling**: More detailed error messages and feedback to the user.

## Author
- **Name**: [Your Name]
- **Contact**: [Your Email]

Feel free to contribute to the project by submitting pull requests or opening issues for any bugs or feature requests!
