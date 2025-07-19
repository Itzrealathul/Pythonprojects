def total_bill(bill_amount,tip_percentage):
    total=bill_amount*(1+0.01*tip_percentage)
    total=round (total,2)
    print("The total bill amount is",total)
bill_amount=int(input("Enter the bill amount"))
tip=int(input("Enter the tip percentage"))
total_bill(bill_amount,tip)
