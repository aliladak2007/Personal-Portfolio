import tkinter as tk
from tkinter import messagebox, ttk
import datetime

def calculate_monthly_payment(principal, annual_interest_rate, years):
    """Calculate the monthly mortgage payment based on the principal, interest rate, and term."""
    monthly_interest_rate = annual_interest_rate / 100 / 12  # Convert annual interest rate to a monthly rate
    number_of_payments = years * 12  # Total number of payments over the loan term
    # Calculate the monthly payment using the amortization formula
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    return monthly_payment

def validate_inputs(principal, deposit, annual_interest_rate, years):
    """Validate user inputs ensuring all inputs are positive numbers."""
    try:
        principal = float(principal)  # Convert principal to a float
        deposit = float(deposit)  # Convert deposit to a float
        annual_interest_rate = float(annual_interest_rate)  # Convert interest rate to a float
        years = int(years)  # Convert loan term to an integer
        # Ensure all values are positive and that the deposit is less than the principal
        if principal <= 0 or deposit < 0 or annual_interest_rate <= 0 or years <= 0:
            raise ValueError("Principal, interest rate, and years must be greater than zero. Deposit must be non-negative.")
        if deposit >= principal:
            raise ValueError("Deposit must be less than the principal amount.")
        return principal, deposit, annual_interest_rate, years
    except ValueError as e:
        # Raise a ValueError with a descriptive error message if validation fails
        raise ValueError(f"Invalid input: {e}")

def display_result(principal, deposit, annual_interest_rate, years, label_result, text_amortization):
    """Display the monthly payment result or show an error message if inputs are invalid."""
    try:
        # Validate inputs and calculate the adjusted principal (principal - deposit)
        principal, deposit, annual_interest_rate, years = validate_inputs(principal, deposit, annual_interest_rate, years)
        adjusted_principal = principal - deposit
        # Calculate the monthly payment based on the adjusted principal
        monthly_payment = calculate_monthly_payment(adjusted_principal, annual_interest_rate, years)
        # Update the result label with the calculated monthly payment
        label_result.config(text=f"Monthly Payment: ${monthly_payment:.2f}", fg="#4CAF50")
        # Generate and display the amortization schedule
        generate_amortization_schedule(adjusted_principal, annual_interest_rate, years, monthly_payment, text_amortization)
    except ValueError as e:
        # Show an error message if input validation fails
        label_result.config(text=str(e), fg="red")
        messagebox.showerror("Input Error", str(e))

def generate_amortization_schedule(principal, annual_interest_rate, years, monthly_payment, text_amortization):
    """Generate and display the amortization schedule."""
    text_amortization.config(state=tk.NORMAL)  # Enable editing of the text widget
    text_amortization.delete(1.0, tk.END)  # Clear any existing text in the widget
    # Insert table headers into the amortization schedule
    text_amortization.insert(tk.END, f"{'Month':<10}{'Interest':<15}{'Principal':<15}{'Balance':<15}\n")
    text_amortization.insert(tk.END, "-" * 55 + "\n")

    monthly_interest_rate = annual_interest_rate / 100 / 12  # Monthly interest rate
    balance = principal  # Initial balance is the principal amount

    # Generate the schedule month by month
    for month in range(1, years * 12 + 1):
        interest_payment = balance * monthly_interest_rate  # Calculate interest for the month
        principal_payment = monthly_payment - interest_payment  # Calculate principal payment for the month
        balance -= principal_payment  # Subtract the principal payment from the balance

        # Insert the calculated values into the amortization schedule
        text_amortization.insert(tk.END, f"{month:<10}{interest_payment:<15.2f}{principal_payment:<15.2f}{balance:<15.2f}\n")

        if balance <= 0:
            break  # Exit the loop if the balance is paid off

    text_amortization.config(state=tk.DISABLED)  # Disable editing of the text widget after populating it

def save_calculation(principal, deposit, annual_interest_rate, years, monthly_payment):
    """Save the current calculation results to a text file."""
    try:
        # Validate inputs and calculate the adjusted principal (principal - deposit)
        principal, deposit, annual_interest_rate, years = validate_inputs(principal, deposit, annual_interest_rate, years)
        adjusted_principal = principal - deposit
        monthly_payment = calculate_monthly_payment(adjusted_principal, annual_interest_rate, years)
        # Save the calculation details to a text file
        with open("mortgage_calculation.txt", "a") as file:
            file.write(f"Date: {datetime.datetime.now()}\n")
            file.write(f"Principal: ${principal:.2f}\n")
            file.write(f"Deposit: ${deposit:.2f}\n")
            file.write(f"Adjusted Principal: ${adjusted_principal:.2f}\n")
            file.write(f"Annual Interest Rate: {annual_interest_rate:.2f}%\n")
            file.write(f"Loan Term: {years} years\n")
            file.write(f"Monthly Payment: ${monthly_payment:.2f}\n")
            file.write("-" * 30 + "\n")
        messagebox.showinfo("Save Successful", "Calculation saved to mortgage_calculation.txt")
    except ValueError as e:
        # Show an error message if input validation fails during the save operation
        messagebox.showerror("Save Error", str(e))

def reset_fields(entry_principal, entry_deposit, scale_interest_rate, scale_years, label_result, text_amortization):
    """Reset all input fields and results."""
    entry_principal.delete(0, tk.END)  # Clear the principal input field
    entry_deposit.delete(0, tk.END)  # Clear the deposit input field
    scale_interest_rate.set(3.0)  # Reset the interest rate slider to the default value
    scale_years.set(15)  # Reset the loan term slider to the default value
    label_result.config(text="Monthly Payment: $0.00", fg="black")  # Reset the result label
    text_amortization.config(state=tk.NORMAL)  # Enable editing of the text widget
    text_amortization.delete(1.0, tk.END)  # Clear the amortization schedule
    text_amortization.config(state=tk.DISABLED)  # Disable editing of the text widget

def main():
    """Main function to set up and run the Tkinter application."""
    root = tk.Tk()  # Create the main window
    root.title("Mortgage Calculator")  # Set the window title
    root.geometry("600x550")  # Set the window size
    root.configure(bg="#f8f8f8")  # Set the background color

    # Main frame for padding and organization
    main_frame = tk.Frame(root, bg="#f8f8f8", padx=20, pady=20)
    main_frame.pack(expand=True, fill=tk.BOTH)

    # Principal amount input
    label_principal = tk.Label(main_frame, text="Principal Amount ($):", bg="#f8f8f8", font=("Helvetica", 10, "bold"))
    label_principal.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

    entry_principal = tk.Entry(main_frame, font=("Helvetica", 10))
    entry_principal.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)

    # Deposit amount input
    label_deposit = tk.Label(main_frame, text="Deposit Amount ($):", bg="#f8f8f8", font=("Helvetica", 10, "bold"))
    label_deposit.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

    entry_deposit = tk.Entry(main_frame, font=("Helvetica", 10))
    entry_deposit.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)

    # Interest rate slider
    label_interest_rate = tk.Label(main_frame, text="Annual Interest Rate (%):", bg="#f8f8f8", font=("Helvetica", 10, "bold"))
    label_interest_rate.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

    scale_interest_rate = tk.Scale(main_frame, from_=0.0, to=20.0, orient=tk.HORIZONTAL, resolution=0.1, bg="#d3d3d3", font=("Helvetica", 10))
    scale_interest_rate.set(3.0)
    scale_interest_rate.grid(row=2, column=1, padx=10, pady=5, sticky=tk.EW)

    # Loan term slider
    label_years = tk.Label(main_frame, text="Loan Term (Years):", bg="#f8f8f8", font=("Helvetica", 10, "bold"))
    label_years.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

    scale_years = tk.Scale(main_frame, from_=1, to=30, orient=tk.HORIZONTAL, bg="#d3d3d3", font=("Helvetica", 10))
    scale_years.set(15)
    scale_years.grid(row=3, column=1, padx=10, pady=5, sticky=tk.EW)

    # Calculate button
    button_calculate = tk.Button(main_frame, text="Calculate", font=("Helvetica", 10, "bold"), bg="#4CAF50", fg="white",
                                 command=lambda: display_result(entry_principal.get(),
                                                                entry_deposit.get(),
                                                                scale_interest_rate.get(),
                                                                scale_years.get(),
                                                                label_result,
                                                                text_amortization))
    button_calculate.grid(row=4, columnspan=2, pady=10)

    # Save button
    button_save = tk.Button(main_frame, text="Save Calculation", font=("Helvetica", 10, "bold"), bg="#2196F3", fg="white",
                            command=lambda: save_calculation(entry_principal.get(),
                                                             entry_deposit.get(),
                                                             scale_interest_rate.get(),
                                                             scale_years.get(),
                                                             calculate_monthly_payment(float(entry_principal.get()) - float(entry_deposit.get()),
                                                                                       scale_interest_rate.get(),
                                                                                       scale_years.get())))
    button_save.grid(row=5, columnspan=2, pady=5)

    # Reset button
    button_reset = tk.Button(main_frame, text="Reset", font=("Helvetica", 10, "bold"), bg="#f44336", fg="white",
                             command=lambda: reset_fields(entry_principal, entry_deposit, scale_interest_rate, scale_years, label_result, text_amortization))
    button_reset.grid(row=6, columnspan=2, pady=5)

    # Result label
    label_result = tk.Label(main_frame, text="Monthly Payment: $0.00", bg="#f8f8f8", font=("Helvetica", 12, "bold"))
    label_result.grid(row=7, columnspan=2, padx=10, pady=5)

    # Amortization schedule
    label_amortization = tk.Label(main_frame, text="Amortization Schedule:", bg="#f8f8f8", font=("Helvetica", 10, "bold"))
    label_amortization.grid(row=8, columnspan=2, padx=10, pady=5)

    text_amortization = tk.Text(main_frame, height=10, state=tk.DISABLED, bg="#e8e8e8", font=("Courier", 10))
    text_amortization.grid(row=9, columnspan=2, padx=10, pady=5, sticky=tk.EW)

    # Tooltips for better UX
    create_tooltip(entry_principal, "Enter the total loan amount.")
    create_tooltip(entry_deposit, "Enter the deposit amount (must be less than principal).")
    create_tooltip(scale_interest_rate, "Slide to select the annual interest rate.")
    create_tooltip(scale_years, "Slide to select the loan term in years.")

    root.mainloop()

def create_tooltip(widget, text):
    """Create a tooltip for the given widget."""
    tooltip = tk.Label(widget, text=text, bg="yellow", fg="black", bd=1, relief="solid", font=("Helvetica", 8), wraplength=150)
    def show_tooltip(event):
        tooltip.place(x=event.x + 20, y=event.y)  # Show tooltip near the cursor
    def hide_tooltip(event):
        tooltip.place_forget()  # Hide the tooltip
    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)

if __name__ == "__main__":
    main()
