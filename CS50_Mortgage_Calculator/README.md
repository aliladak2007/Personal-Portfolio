# Mortgage Calculator with Deposit Functionality
#### Video Demo:  <URL HERE>
## Overview

This project is a Mortgage Calculator built using Python's `tkinter` library, which provides a graphical user interface (GUI) for users to easily compute their monthly mortgage payments based on various inputs such as the principal loan amount, annual interest rate, loan term, and an optional deposit. The calculator also generates an amortization schedule that breaks down the monthly payments into interest and principal components, showing the remaining balance after each payment. This tool is particularly useful for individuals looking to understand their mortgage payments and the impact of making a deposit on the total cost of the loan.

### Features

- **Principal Amount Input:** Users can input the total loan amount they plan to borrow.
- **Deposit Amount Input:** Users can specify a deposit amount, which reduces the principal before the monthly payment is calculated.
- **Annual Interest Rate Input:** The interest rate is input using a slider that allows precise adjustments.
- **Loan Term Input:** The loan term (in years) is also selected using a slider, making it easy to adjust.
- **Monthly Payment Calculation:** The tool calculates the monthly payment based on the adjusted principal, annual interest rate, and loan term.
- **Amortization Schedule:** Displays a detailed schedule showing how each payment is split between interest and principal, and how the loan balance decreases over time.
- **Save Calculation:** Users can save the calculation results to a text file for future reference.
- **Reset Functionality:** All input fields and results can be reset to their default values with the click of a button.
- **Tooltips:** Tooltips provide helpful guidance to users on how to use the various inputs and features.

## Installation

To use this Mortgage Calculator, ensure you have Python installed on your machine. The project requires Python 3.x and uses the built-in `tkinter` library, which is included with Python. No additional dependencies are required.

### Steps:

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/your-username/mortgage-calculator.git
   cd mortgage-calculator
   ```

2. **Run the Script**: 
   ```bash
   python mortgage_calculator.py
   ```

This will launch the GUI application, and you can start using the mortgage calculator.

## Usage

Once the application is running, you will see a window with the following inputs and features:

### 1. **Principal Amount Input**
   - Enter the total loan amount you wish to borrow in the "Principal Amount ($)" field. This is the base amount before any deposit is considered.

### 2. **Deposit Amount Input**
   - Enter the deposit amount in the "Deposit Amount ($)" field. The deposit will be subtracted from the principal to determine the actual amount to be financed.

### 3. **Annual Interest Rate Input**
   - Use the slider under "Annual Interest Rate (%)" to select the interest rate for your loan. The slider allows for fine-tuning of the rate, supporting increments as small as 0.1%.

### 4. **Loan Term Input**
   - Use the slider under "Loan Term (Years)" to select the duration of the loan. This slider ranges from 1 to 30 years, accommodating most common mortgage terms.

### 5. **Calculate Button**
   - Once all inputs are filled out, click the "Calculate" button. The tool will compute the monthly payment and update the "Monthly Payment" label with the result. Additionally, it will generate an amortization schedule showing how the loan balance decreases over time.

### 6. **Save Calculation**
   - If you wish to save the details of your calculation, click the "Save Calculation" button. The results will be saved in a text file named `mortgage_calculation.txt` in the same directory as the script. This file will include the principal, deposit, adjusted principal, interest rate, loan term, and the calculated monthly payment.

### 7. **Reset Button**
   - To clear all fields and reset the calculator, click the "Reset" button. This will remove all input values, clear the amortization schedule, and reset the monthly payment display.

### 8. **Amortization Schedule**
   - The amortization schedule is displayed in a text box at the bottom of the window. This schedule shows a month-by-month breakdown of each payment, indicating how much goes towards interest and how much goes towards reducing the principal. It also shows the remaining balance after each payment.

### 9. **Tooltips**
   - Hover over any input field or slider to see a tooltip with instructions or explanations. This feature helps users understand what data is required and how it affects the calculation.

## Project Structure

The project consists of a single Python file:

- **mortgage_calculator.py**: The main script containing the GUI setup, input validation, mortgage calculation logic, amortization schedule generation, and file-saving functionality.

## Example

Here’s a simple example of how you might use this tool:

1. Enter a principal amount of $200,000.
2. Enter a deposit of $20,000.
3. Set the annual interest rate to 4.5%.
4. Set the loan term to 30 years.
5. Click "Calculate" to see your monthly payment.
6. The "Monthly Payment" label will update to show the calculated payment (e.g., $911.84).
7. The amortization schedule will display below, showing how each payment contributes to interest and principal and the remaining loan balance over time.

## Enhancements

Future enhancements could include:

- **Currency Selection**: Allow users to select different currencies (e.g., USD, GBP, EUR) and adjust calculations accordingly.
- **Graphical Visualization**: Add charts to visually represent the amortization schedule or compare different loan scenarios.
- **More Detailed Reports**: Enhance the save functionality to include more detailed reports or export options such as CSV or PDF.

## Conclusion

This Mortgage Calculator is a powerful and user-friendly tool for anyone looking to calculate their mortgage payments and understand the impact of various factors like interest rates, loan terms, and deposits. Its straightforward interface, combined with advanced features like amortization scheduling and save functionality, makes it a valuable resource for potential homeowners, financial planners, and real estate professionals.

Whether you're planning to buy a home, refinance an existing mortgage, or simply exploring different loan scenarios, this calculator provides the insights needed to make informed decisions.