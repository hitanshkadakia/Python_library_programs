from forex_python.converter import CurrencyRates
c=CurrencyRates()
x=1
r=c.convert("USD","INR", x)
print(x," rupee = ",r," dollar")