# a little challenge to create a tip calculator

bill = float(input("how much was your restaurant bill?"))

percent_1 = 0.05
percent_2 = 0.15
percent_3 = 0.30

amount_1 = (bill * percent_1) + bill
amount_2 = (bill * percent_2) + bill
amount_3 = (bill * percent_3) + bill

print(f"total amount with\
    \n{percent_1*100:.0f}% is ${amount_1:.2f}\
    \n{percent_2*100:.0f}% is ${amount_2:.2f}\
    \n{percent_3*100:.0f}% is ${amount_3:.2f}")
