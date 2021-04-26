# Day - 2 === Currency Converter from INR to other

INR = float(0.013)  # United States Dollar
EUR = float(1.21)  # Euro
JPY = float(0.0093)   # Japanese Yen
GBP = float(1.39)  # Great Britain Pound
CAD = float(0.81)  # Canadian Dollars

result = None

amount = float(input("Enter the Amount: "))
currency = input("Enter currency (INR, EUR, JPY, GBP, CAD): ")
convert = input(
    f"Do you want to convert from USD to {currency.upper()} or {currency.upper()} to USD (Press 1 & 2 for respective options): ")

if convert == "1": # INR to other
    if currency == "INR" or currency == "inr":
        result = amount / INR
    elif currency == "EUR" or currency == "eur":
        result = amount / EUR
    elif currency == "JPY" or currency == "jpy":
        result = amount / JPY
    elif currency == "GBP" or currency == "gbp":
        result = amount / GBP
    elif currency == "CAD" or currency == "cad":
        result = amount / CAD

    if result is None:
        print("Invalid Currency")
    else:
        print(f"{amount} USD = {result} {currency.upper()}")

elif convert=="2": # INR from other
    if currency == "INR" or currency == "inr":
        result = amount * INR
    elif currency == "EUR" or currency == "eur":
        result = amount * EUR
    elif currency == "JPY" or currency == "jpy":
        result = amount * JPY
    elif currency == "GBP" or currency == "gbp":
        result = amount * GBP
    elif currency == "CAD" or currency == "cad":
        result = amount * CAD

    if result is None:
        print("Invalid Currency")
    else:
        print(f"{amount} {currency.upper()} = {result} USD")

else:
    print("Convertion criterion did not match")