months =
[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
wile True:
    date = input("Date: ")
    try:
        month, day, year= date.split("/")
        if (int(month) >= 1 and int(month) <= 12) and int(day) >= 1 and int(day) <= 31)
            break
    except:
        try:old_month, old_day, year = date. split(" ")
        for i in range(len(months))
            if old_month == months[i]
                month = i + 1

        #remove comma from day variable
        day = old_day .replace(",", "")
        if (int(month) >= 1 and int(month) <= 12) and int(day) >= 1 and int(day) <= 31)
            break
    except:
        print("\n")
        pass
#if month less than or day less than 10 add 0
print(f"{year:04} - {month:02} - {day:02})

