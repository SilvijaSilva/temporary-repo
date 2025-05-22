year_input = input("Enter the year of birth: ")
month_input = input("Enter the month of birth: ")
day_input = input("Enter the date of birth: ")

year = int(year_input)
month = int(month_input)
day = int(day_input)

from datetime import datetime

current_date = datetime.now()

date_of_birth = datetime(year, month, day)

age = current_date - date_of_birth

print(f"Age: {age.days // 365} years")
