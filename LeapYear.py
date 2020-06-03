def validate(inputYear):
    if len(str(inputYear)) != 4:
        raise Exception("Invalid year! Please enter year of 4 digits.");


def check_leap_year(inputYear):
    return inputYear % 4 == 0 and (inputYear % 100 != 0 or inputYear % 400 == 0)   

try:
    inputYear = int(input("Enter year to find out leap or not"))
except ValueError:
    print("Please enter year in numbers!")
else:
    validate(inputYear)
    isLeapYear = check_leap_year(inputYear)
    print(inputYear, " is leap year!" if isLeapYear else "is not a leap year!")
