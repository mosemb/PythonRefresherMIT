
#balance = balance
annualInterestRate = (0.2/0.12/100)
#monthlyPaymentRate = 0.04*balance

for i in range(1,13):

        balance = round(balance,2)
        monthlyPaymentRate= round(balance*0.04,2)
        InterestRate = (0.2 / 0.12 / 100)
        unpaid = round(balance-monthlyPaymentRate,2)
        interest = round(unpaid*annualInterestRate,2)
        newbalance = round(unpaid+interest,2)
        balance = round(newbalance,2)

print('Remaining balance: '+ str(balance))



