# Payroll Pros Program
# Main Program
# David, Mike,Vivek and Chris
# Connects Input, Calculations, and Output modules.


from input import get_employee_information

from calculations import (
    calculate_gross_pay,
    calculate_taxes,
    calculate_net_pay
)

from output import (
    display_employee_data,
    save_payroll_results
)


def main():

    print("=" * 70)
    print("                  PAYROLL PROS")
    print("              Employee Payroll System")
    print("=" * 70)

    print("\nPlease enter information for 10 employees.")

    # Gets all employee information from input.py.

    (
        first_names,
        last_names,
        employee_ids,
        dependents,
        hours_worked,
        hourly_rates
    ) = get_employee_information()


    # Stores completed payroll information.

    payroll_results = []


    # Processess all 10 employees.

    for i in range(10):

        # Calculates gross pay using Mike's function.

        gross_pay = calculate_gross_pay(
            hours_worked[i],
            hourly_rates[i]
        )


        # Since the optional 401(k) idea is not part of
        # the required project, gross pay is the pre-tax amount.

        pre_tax_amount = gross_pay


        # Calculate state and federal taxes.

        state_tax, federal_tax, total_tax = calculate_taxes(
            pre_tax_amount
        )


        # Calculate post-tax amount.

        post_tax_amount = calculate_net_pay(
            pre_tax_amount
        )


        # Store all information for this employee.

        employee_result = {
            "first_name": first_names[i],
            "last_name": last_names[i],
            "employee_id": employee_ids[i],
            "dependents": dependents[i],
            "hours_worked": hours_worked[i],
            "hourly_rate": hourly_rates[i],
            "gross_pay": gross_pay,
            "state_tax": state_tax,
            "federal_tax": federal_tax,
            "pre_tax_amount": pre_tax_amount,
            "post_tax_amount": post_tax_amount
        }


        payroll_results.append(employee_result)


    # Send completed results to output.py.

    display_employee_data(payroll_results)

    save_payroll_results(payroll_results)


if __name__ == "__main__":
    main()