import math

cent = int(input())
year = cent * 100
day = year * 365.2422
day_round = math.floor(day)
hours = day_round * 24
minutes = hours * 60

print(f"{cent} centuries = {year} years = {day_round} days = {hours} hours = {minutes} minutes")
