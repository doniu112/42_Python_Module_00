def ft_water_reminder():
    num_of_days = int(input("Days since last watering: "))
    if num_of_days >= 2:
        print("Water the plants!")
    else:
        print("Plants are fine")