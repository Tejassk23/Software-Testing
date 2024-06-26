def inr_to_usd(amount_inr):
    conversion_rate_usd = 0.013
    amount_usd = amount_inr * conversion_rate_usd
    return amount_usd

def inr_to_euro(amount_inr):
    conversion_rate_euro = 0.011
    amount_euro = amount_inr * conversion_rate_euro
    return amount_euro
def inr_to_gbp(amount_inr):
    conversion_rate_gbp = 0.0095
    amount_gbp = amount_inr * conversion_rate_gbp
    return amount_gbp

amount_inr = float(input("Enter the amount in Indian Rupees (INR): "))
amount_usd = inr_to_usd(amount_inr)
amount_euro = inr_to_euro(amount_inr)
amount_gbp = inr_to_gbp(amount_inr)

print(f"{amount_inr} INR is equal to {amount_usd} US Dollars.")
print(f"{amount_inr} INR is equal to {amount_euro} Euros.")
print(f"{amount_inr} INR is equal to {amount_gbp} British Pounds.")