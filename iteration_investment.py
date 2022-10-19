initial_investment = 100
years = 0
while initial_investment <= 1000:
    initial_investment = initial_investment + (initial_investment * 0.1)
    years = years + 1
print(years)