"""
Wrote by Kaeden Snyder and Hamim Shafin

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


def function1(a):
    return a*8*260

def function2(a,b,c):
    return a*8*(260-b-c)

DASH_LENGTH = 40
print('=' * DASH_LENGTH)
print(f"{'Unadjusted Salary':.<{COLUMN_LENGTH}}: $", round(function1(salary_per_hour),2))
print(f"{'Adjusted Salary':.<{COLUMN_LENGTH}}: $", round(function2(salary_per_hour,holidays_per_year,vacation_days_per_year), 2))

DASH_LENGTH = 40
print('=' * DASH_LENGTH)

print("Goodbye!")
