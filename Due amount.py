def calculate_due_amount(total_bill, amount_paid):
    return amount_paid - total_bill

total = float(input())
paid = float(input())

due = calculate_due_amount(total, paid)
print(due)