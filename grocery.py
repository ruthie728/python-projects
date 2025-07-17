def main ():
    grocery = {}
    while True:
        try:
            item = input(). strip() . upper()
            if item in grocery:
                grocery[item]+=1
            else:
                grocery[item]=1
        except EOFError:
            print("\n")  #print a new line after ctrl + D
            break

        #sorted output
    for item in sorted(grocery):
        print(f"{grocery[item]} {item}")

if __name__ == "__main__":
    main()
