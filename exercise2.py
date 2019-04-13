house_price = 1000000
has_good_credit = False

if has_good_credit:
    house_price -= house_price * (10/100)
    print('Buyer has good credit')
    print('Putting down the price by 10%')
else:
    house_price -= house_price * (20/100)
    print('Buyer has bad credit')
    print('Putting down the price by 20%')

print(f"Downpayment: ${round(house_price)}")