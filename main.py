"""
Wrote by Kaeden Snyder and Hamim Shafin
https://github.com/hamimshafin/PythonCalculator
"""

# this is the header
DASH_LENGTH = 40
print('=' * DASH_LENGTH)
print("The Salary Calculator program")
print('=' * DASH_LENGTH)
# end of header

COLUMN_LENGTH = 25
salary_per_hour = float(input(f"{'Salary per hour':.<{COLUMN_LENGTH}}: "))
hours_per_week = float(input(f"{'Hours per Week':.<{COLUMN_LENGTH}}: "))
days_per_week = float(input(f"{'Days per Week':.<{COLUMN_LENGTH}}: "))
holidays_per_year = float(input(f"{'Holidays per Year':.<{COLUMN_LENGTH}}: "))
vacation_days_per_year = float(input(f"{'Vacation Days per Year':.<{COLUMN_LENGTH}}: "))

hours_working_day = float(input(f"{f'Numbers of hour in a working day':.<{COLUMN_LENGTH}}:"))  # user input


def unadjusted_salary(salary_per_hour):
    return salary_per_hour * hours_working_day * days_per_week*52


def adjusted_salary(salary_per_hour, holidays_per_year, vacation_days_per_year):
    return salary_per_hour * hours_working_day * (days_per_week*52 - holidays_per_year - vacation_days_per_year)


DASH_LENGTH = 40
print('=' * DASH_LENGTH)
print(f"{'Unadjusted Salary':.<{COLUMN_LENGTH}}: $", round(unadjusted_salary(salary_per_hour), 2))
print(f"{'Adjusted Salary':.<{COLUMN_LENGTH}}: $",
      round(adjusted_salary(salary_per_hour, holidays_per_year, vacation_days_per_year), 2))

DASH_LENGTH = 40
print('=' * DASH_LENGTH)

print("Goodbye!")
