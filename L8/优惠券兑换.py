from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code:
        return False
    try:
        current = datetime.strptime(current_date, '%B %d, %Y')
        expiration = datetime.strptime(expiration_date, '%B %d, %Y')
    except ValueError:
        return False
    return current <= expiration

print(check_coupon('123', '123', 'September 5, 2014', 'October 1, 2014'))
print(check_coupon('123a', '123', 'September 5, 2014', 'October 1, 2014'))
print(check_coupon('123', '123', 'July 9, 2015', 'July 2, 2015'))
