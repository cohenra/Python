def odds_minus_even(list_of_number):
    odds_numbers = 0
    even_numbers = 0
    sum_misson = 0
    for i in  (list_of_number):
        if i % 2 == 0:
            even_numbers += i
        else:
            odds_numbers += i
    sum_misson = odds_numbers - even_numbers
    return sum_misson

sum_mission = odds_minus_even([1,2,3,4,5,6,7,8,9,10])
print(sum_mission)