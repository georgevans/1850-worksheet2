weekdays = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
}

day = input('Enter day of the week: ').lower()

if day in weekdays:
    for n in weekdays.keys():
        if day == n:
            print(f"{day.capitalize()} is day {weekdays[n]}")
else:
    print('Please enter a valid day')
