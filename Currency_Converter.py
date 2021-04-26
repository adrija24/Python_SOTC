# Day - 2 === Currency Converter from INR to other

USD = float(74.22)  # United States Dollar
EUR = float(90.43)  # Euro
JPY = float(0.69)   # Japanese Yen
GBP = float(104.0)  # Great Britain Pound
CAD = float(59.97)  # Canadian Dollars

result = None

amount = float(input("Enter the Amount: "))
currency = input("Enter currency (USD, EUR, JPY, GBP, CAD): ")
convert = input(
    f"Do you want to convert from INR to {currency} or {currency} to INR (Press 1 & 2 for respective options): ")

if convert == "1": # INR to other
    if currency == "USD" or currency == "usd":
        result = amount / USD
    elif currency == "EUR" or currency == "eur":
        result = amount / EUR
    elif currency == "JPY" or currency == "jpy":
        result = amount / JPY
    elif currency == "GBP" or currency == "gbp":
        result = amount / GBP
    elif currency == "CAD" or currency == "gbp":
        result = amount / CAD

    if result is None:
        print("Invalid Currency")
    else:
        print(f"{amount} INR = {result} {currency}")

elif convert=="2": # INR from other
    if currency == "USD" or currency == "usd":
        result = amount * USD
    elif currency == "EUR" or currency == "eur":
        result = amount * EUR
    elif currency == "JPY" or currency == "jpy":
        result = amount * JPY
    elif currency == "GBP" or currency == "gbp":
        result = amount * GBP
    elif currency == "CAD" or currency == "gbp":
        result = amount * CAD

    if result is None:
        print("Invalid Currency")
    else:
        print(f"{amount} {currency} = {result} INR")

else:
    print("Convertion criterion did not match")