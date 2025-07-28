import json

# Open and load the JSON file
# ⚠️ Chack Json file path
with open('bdt_to_currency.json', 'r') as file:
    bdt_to_currency = json.load(file)



def currency_converter(amount: float | int = 1,  to_currency: str = "USD") -> str: # set default 1tk to US dollar.
    rate = bdt_to_currency[to_currency.upper()]
    return f"{format(amount * bdt_to_currency[to_currency.upper()], ".5g")} {to_currency.upper()}"


print(currency_converter(110, "usd"))



