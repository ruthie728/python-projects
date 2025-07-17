ques = input("Enter your question ")

x, y, z = ques.split()
x = float(x)
z = float(z)

if y == "+":
    print(round(x + z,1))

elif y == "-":
    print(round(x - z,1))

elif y == "/":
    print(round(x / z,1))

else:
    print(round(x * z,1))





