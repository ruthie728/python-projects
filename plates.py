def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
   #length must be btwn 2 and 6
    if len(s) < 2 or  len(s) > 6:
        return False

   #first 2 characters should be letters
    if not s[0:2].isalpha():
        return False

   #only alphanumeric characters allowed
    if not s.isalnum():
        return False

    digit_found= False
    for i, char in enumerate(s):
        if char.isdigit():

            #first digit can not be zero  check if this is the first digit
            if char == "0" and all(c .isalpha() for c in s[:i]):
                return False
            
            digit_found=True

        elif digit_found and char .isalpha():   #letter comees after a digit not allowed
                return False

    return True

main()






