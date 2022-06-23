population_list = list(map(int, input().split(", ")))
minimum_wealth = int(input())
below_minimum_wealth = [i for i in population_list if i < minimum_wealth]
above_minimum_wealth = [j for j in population_list if j > minimum_wealth]
above_average_wealth = sum(list(map(lambda k: k - minimum_wealth, above_minimum_wealth)))
below_average_deficit = sum(list(map(lambda l: minimum_wealth - l, below_minimum_wealth)))

if below_average_deficit > above_average_wealth:
    print("No equal distribution possible")
else:
    move_count = 1
    loop_count = 0
    for f in population_list:
        if f >= minimum_wealth:
            loop_count += 1
            continue
        else:
            restart = True
            while restart:
                current_deficit = minimum_wealth - f
                if f < minimum_wealth and (population_list[-move_count] - minimum_wealth) >= current_deficit:
                    population_list[-move_count] -= current_deficit
                    population_list[loop_count] += current_deficit
                    loop_count += 1
                    restart = False
                else:
                    move_count += 1

    print(population_list)
