n_centuries = int(input())

years = n_centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{n_centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
