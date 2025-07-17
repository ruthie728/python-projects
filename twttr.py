txt = input("Input:").strip()

vowels =["a", "e", "i", "o", "u","A", "E", "I", "O", "U",]

print("Output:", end="")

for char in txt:
    if char not in vowels:
        print(char, end="")

print()
