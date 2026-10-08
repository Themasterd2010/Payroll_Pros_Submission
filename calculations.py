# Payroll Pros Program
# Gross Pay, State Tax, Federal Tax, and Net Pay Calculations


STATE_TAX_RATE = 0.056
FEDERAL_TAX_RATE = 0.079


# Calculate gross pay.
# Overtime begins after 40 hours at 1.5 times the hourly rate.

def calculate_gross_pay(hours_worked, hourly_rate):

    if hours_worked <= 40:
        gross_pay = hours_worked * hourly_rate

    else:
        regular_pay = 40 * hourly_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5

        gross_pay = regular_pay + overtime_pay

    return gross_pay


# Calculate state tax at 5.6%.

def calculate_state_tax(pre_tax_amount):

    state_tax = pre_tax_amount * STATE_TAX_RATE

    return state_tax


# Calculate federal tax at 7.9%.

def calculate_federal_tax(pre_tax_amount):

    federal_tax = pre_tax_amount * FEDERAL_TAX_RATE

    return federal_tax


# Calculate both taxes.

def calculate_taxes(pre_tax_amount):

    state_tax = calculate_state_tax(pre_tax_amount)
    federal_tax = calculate_federal_tax(pre_tax_amount)

    total_tax = state_tax + federal_tax

    return state_tax, federal_tax, total_tax


# Calculate post-tax income.

def calculate_net_pay(pre_tax_amount):

    state_tax = calculate_state_tax(pre_tax_amount)
    federal_tax = calculate_federal_tax(pre_tax_amount)

    post_tax_amount = pre_tax_amount - state_tax - federal_tax

    return post_tax_amount