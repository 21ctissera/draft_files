A=float(input("How many shares were purchased? "))
B=float(input("How much were the shares purchased for? "))
C=float(input("What percentage does the stockbroker make on commision? "))
D=float(input("What was the amount each stock sold for? "))

paid_stock=A*B
commision_paid=C*paid_stock
sold_for=A*D
commision_sale=sold_for*C
totalpaid=paid_stock+commision_paid
recieved=sold_for-commision_sale
profit_loss=recieved-totalpaid

print("Amount paid for the stock: $", format(paid_stock, ",.2f"))
print("Commision paid on the purchase: $", format(commision_paid, ",.2f"))
print("Amount the stock sold for: $", format(sold_for, ",.2f"))
print("Commision paid on the sale: $", format(commision_sale, ",.2f"))
print("Profit (or loss if negative): $", format(profit_loss, ",.2f"))



