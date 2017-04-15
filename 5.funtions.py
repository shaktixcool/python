print (1)
def currency_converter(rate,euros):
    dollars = euros*rate
    return dollars
rate = float (input("Enter rate: "))
euros = float (input("Enter Euros: "))
print (rate)
print (euros)

print (currency_converter(rate,euros))
