# Payroll Pros Program
# Employee Input


def get_first_name():
    while True:
        first_name = input("Enter first name: ").strip()

        if first_name:
            return first_name
        else:
            print("First name cannot be empty. Please try again.")


def get_last_name():
    while True:
        last_name = input("Enter last name: ").strip()

        if last_name:
            return last_name
        else:
            print("Last name cannot be empty. Please try again.")


def get_employee_id():
    while True:
        employee_id = input("Enter employee ID: ").strip()

        if employee_id.isdigit():
            return employee_id
        else:
            print("Employee ID must contain numbers only. Please try again.")


def get_dependents():
    while True:
        try:
            dependents = int(input("Enter number of dependents: "))

            if dependents < 0:
                print("Number of dependents cannot be negative.")
            else:
                return dependents

        except ValueError:
            print("Please enter a whole number.")


def get_hours_worked():
    while True:
        try:
            hours_worked = float(input("Enter hours worked: "))

            if hours_worked < 0:
                print("Hours worked cannot be negative.")
            else:
                return hours_worked

        except ValueError:
            print("Please enter a valid number.")


def get_hourly_rate():
    while True:
        try:
            hourly_rate = float(input("Enter hourly pay rate: $"))

            if hourly_rate < 0:
                print("Hourly pay rate cannot be negative.")
            else:
                return hourly_rate

        except ValueError:
            print("Please enter a valid number.")


def get_employee_information():
    first_name = []
    last_name = []
    employee_id = []
    dependents = []
    hours_worked = []
    hourly_rate = []

    for i in range(10):
        print("\n------------------------------")
        print("Employee", i + 1)
        print("------------------------------")

        first_name.append(get_first_name())
        last_name.append(get_last_name())
        employee_id.append(get_employee_id())
        dependents.append(get_dependents())
        hours_worked.append(get_hours_worked())
        hourly_rate.append(get_hourly_rate())

    return (
        first_name,
        last_name,
        employee_id,
        dependents,
        hours_worked,
        hourly_rate
    )