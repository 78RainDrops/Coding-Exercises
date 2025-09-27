total_money = 1000
quantity = 3
price = 450

# I have 1000 dollars so I can buy 3 football for 450.00 dollars.
print(
    "I have {} dollars so I can but {} football for {:.2f} dollars".format(
        total_money, quantity, price
    )
)
txt = "I have {} dollars so I can but {} football for {:.2f} dollars"
print(txt.format(total_money, quantity, price))
