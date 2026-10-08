# Payroll Pros Program
# Payroll Output


def display_employee_data(payroll_results):

    print("\n")
    print("=" * 70)
    print("                 PAYROLL PROS")
    print("                 PAYROLL RESULTS")
    print("=" * 70)

    for employee in payroll_results:

        print("\nEmployee:", employee["first_name"], employee["last_name"])
        print("Employee ID:", employee["employee_id"])
        print("Dependents:", employee["dependents"])
        print("Hours Worked:", format(employee["hours_worked"], ".2f"))
        print("Hourly Rate: $", format(employee["hourly_rate"], ".2f"))
        print("Gross Pay: $", format(employee["gross_pay"], ".2f"))
        print("State Tax: $", format(employee["state_tax"], ".2f"))
        print("Federal Tax: $", format(employee["federal_tax"], ".2f"))
        print("Pre-Tax Amount: $", format(employee["pre_tax_amount"], ".2f"))
        print("Post-Tax Amount: $", format(employee["post_tax_amount"], ".2f"))

        print("-" * 70)


def save_payroll_results(payroll_results):

    with open("payroll_results.txt", "w") as file:

        file.write("PAYROLL PROS - PAYROLL RESULTS\n")
        file.write("=" * 70 + "\n")

        for employee in payroll_results:

            file.write(
                f"\nEmployee: {employee['first_name']} "
                f"{employee['last_name']}\n"
            )

            file.write(
                f"Employee ID: {employee['employee_id']}\n"
            )

            file.write(
                f"Dependents: {employee['dependents']}\n"
            )

            file.write(
                f"Hours Worked: {employee['hours_worked']:.2f}\n"
            )

            file.write(
                f"Hourly Rate: ${employee['hourly_rate']:.2f}\n"
            )

            file.write(
                f"Gross Pay: ${employee['gross_pay']:.2f}\n"
            )

            file.write(
                f"State Tax: ${employee['state_tax']:.2f}\n"
            )

            file.write(
                f"Federal Tax: ${employee['federal_tax']:.2f}\n"
            )

            file.write(
                f"Pre-Tax Amount: ${employee['pre_tax_amount']:.2f}\n"
            )

            file.write(
                f"Post-Tax Amount: ${employee['post_tax_amount']:.2f}\n"
            )

            file.write("-" * 70 + "\n")

    print("\nPayroll results saved to payroll_results.txt")