import math
biscuits_per_day_per_worker = int(input())
worker_count = int(input())
competitor_biscuits = int(input())
total_number_biscuits = 0

for work_day in range(1, 31):
    total_biscuits_per_day = biscuits_per_day_per_worker * worker_count
    if work_day % 3 == 0:
        total_biscuits_per_day *= 0.75
    total_number_biscuits += math.floor(total_biscuits_per_day)

print(f"You have produced {int(total_number_biscuits)} biscuits for the past month.")

if total_number_biscuits > competitor_biscuits:
    percent = ((total_number_biscuits - competitor_biscuits) / competitor_biscuits) * 100
    print(f"You produce {percent:.2f} percent more biscuits.")
else:
    percent = ((competitor_biscuits - total_number_biscuits) / competitor_biscuits) * 100
    print(f"You produce {percent:.2f} percent less biscuits.")
