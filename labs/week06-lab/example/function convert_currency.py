เขียน function แปลงหน่วยสกุล เงิน

def THB_to_USD(bath):
    dollar = bath / 32
    return dollar


def USD_to_THB(dollar):
    bath = dollar * 32
    return bath


def convert_currency(amount, scale):
    if scale.upper() == "THB":
        converted = THB_to_USD(amount)
        return f"{amount}THB = {converted:.1f}USD"
    elif scale.upper() == "USD":
        converted = USD_to_THB(amount)
        return f"{amount}USD = {converted:.1f}THB"
    else:
        return "Invalid scale. Use 'THB' or 'USD'"


print("CurrencyConverter:")
print(convert_currency(100, "THB"))
print()
