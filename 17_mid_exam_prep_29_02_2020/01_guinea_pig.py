food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000
end_of_month = False
count = 0
for day in range(1, 31):
    count += 1
    food -= 300
    if day % 2 == 0:
        hay -= 0.05 * food
    if day % 3 == 0:
        cover -= weight / 3
    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        end_of_month = True
        break
if not end_of_month:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")

