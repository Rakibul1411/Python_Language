value = float(input("Enter the USD amount to convert BDT: "))

def calc_bdt (amount):
  return 117*amount

result = calc_bdt(value)
print(value, "USD =", result, "BDT")
print(str(value) + " USD = " + str(result) + " BDT")
print(f"{value} USD = {result} BDT")
print()