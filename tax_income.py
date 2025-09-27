# not pure me
income_tax = 45_000
tax_payable = 0
print(f"Given Incode {income_tax}")

if income_tax <= 10_000:
    tax_payable = 0
elif income_tax <= 20_000:
    x = income_tax - 10000
    tax_payable = x * 10/100
else:
    tax_payable = 0

    tax_payable = 10_000 * 10/100

    tax_payable += (income_tax - 20_000) * 20/100

print(f"Total tax to pay: {tax_payable}")