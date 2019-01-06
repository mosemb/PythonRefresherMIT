
def creditcard(balance,annualInterestRate,monthlyPaymentRate):
    """ takes in the balance in ints or floats , takes in the annual interest rate in decimals
    for example 18% = 0.18 and monthlyPaymentRate as decimal still in the form 0.4 as 0.04 then gives back
    remaining balance in 12 months"""
    balance = balance
    monthly_mothly_interest = (annualInterestRate/0.12/100)
    for i in range(1,13):

        balance = round(balance,2)
        minpay = round(balance*monthlyPaymentRate,2)
        unpaid = round(balance-minpay,2)
        interest = round(unpaid*monthly_mothly_interest,2)
        newbalance = round(unpaid+interest,2)
        balance = round(newbalance,2)
    return print('Remaining balance: '+ str(balance))


balance = 3329
annualInterestRate = 0.2
monthly_interest_rate = annualInterestRate/0.12
total_plus_interest = balance*annualInterestRate
total = balance+total_plus_interest
monthly = total/12
print(round(monthly))



















