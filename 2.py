yn = input("will you churn the cream into butter? Y/N\n")
t = 0
while t == 0: 
    if yn == "y" or yn == "Y":
        print("thank you")
        t = 1
    elif yn == "n" or yn == "N":
        print("there will be no supper for you")
        t = 1
    else:
        print("\n please answer with 'Y' or 'N' \n")
        yn = input("will you churn the cream into butter? Y/N\n")
