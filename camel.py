def main():
    txt = input("Enter camel case: ")
    print("Snake_case:",end="")

    #loop through every character
    for chr in txt:
        if chr.isupper():

         print( "_" + chr.lower()  ,end="")
        else:
            print(chr , end="")
    print()

if __name__ == "__main__":
    main()

















