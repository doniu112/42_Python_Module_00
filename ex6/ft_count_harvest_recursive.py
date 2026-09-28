def ft_count_harvest(day: int, days: int) -> None:
    if day > days:
        print("Harvest time!")
        return

    print("Day ", day)
    ft_count_harvest(day+1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    ft_count_harvest(1, days)
