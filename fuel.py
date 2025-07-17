while True:
    fuel = input("Fractions: ")
    try:
        x,y = fuel.split("/")
        new_x = int(x)
        new_y = int(y)

        #ensure both x and y are positive interges
        if new_x > new_y or new_x < 0 or new_y <= 0:
            continue

        frac = new_x / new_y
        break

    except (ValueError, ZeroDivisionError):
        pass
percentage = round(frac * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")

