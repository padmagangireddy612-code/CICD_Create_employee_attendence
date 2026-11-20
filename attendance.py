
def calculate_attendance(attended_days, total_days):

    if total_days <= 0:
        raise ValueError("Total days must be greater than zero")

    if attended_days < 0 or attended_days > total_days:
        raise ValueError("Attended days must be between 0 and total days")

    percentage = (attended_days / total_days) * 100

    return round(percentage, 2)


def check_eligibility(percentage):

    if percentage >= 75:
        return "Eligible"
    else:
        return "Shortage"


def calculate_absent_days(total_days, attended_days):

    absent_days = total_days - attended_days

    return absent_days


# Main program

attended = 85
total = 100

percentage = calculate_attendance(attended, total)

status = check_eligibility(percentage)

absent_days = calculate_absent_days(total, attended)

print("Employee Attendance Management")
print("--------------------------------")
print("Total Working Days:", total)
print("Days Attended:", attended)
print("Days Absent:", absent_days)
print("Attendance Percentage:", percentage, "%")
print("Attendance Status:", status)
