def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    i = 1
    while days >= i:
        print("Day", i)
        i = i + 1
    print("Harvest time!")
