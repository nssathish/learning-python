has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print('Eligibile for loan')

if has_good_credit or has_high_income:
    print('Eligible')

if has_high_income and not has_good_credit:
    print('Not eligible for loan')

