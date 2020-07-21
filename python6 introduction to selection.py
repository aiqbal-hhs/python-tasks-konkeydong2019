i = 1
g = int(input("guess the number 'i'\n"))
while g != i:
    if g > i:
        print("lower\n")
    elif g < i:
        print("higher\n")
    g = int(input("guess the number 'i'\n"))

if g == i:
    print("correct\n")
