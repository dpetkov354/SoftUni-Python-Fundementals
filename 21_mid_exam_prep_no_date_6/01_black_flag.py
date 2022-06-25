duration = int(input())
plunder_per_day = int(input())
expected_plunder = int(input())
bonus_plunder = 0


for day in range(1, duration + 1):
    bonus_plunder += plunder_per_day
    if day % 3 == 0:
        bonus_plunder += plunder_per_day * 0.5
    if day % 5 == 0:
        bonus_plunder *= 0.7

if bonus_plunder >= expected_plunder:
    print(f"Ahoy! {bonus_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(bonus_plunder / expected_plunder) * 100:.2f}% of the plunder.")
