
doubles = [x * 2 for x in range(1, 11)]
fruits = ['apple', 'banana', 'cherry']
fruits = [fruit.upper() for fruit in fruits]
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]

print(fruits)
print(positive_nums)

def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

print(day_of_week(1))
