hours = float(input("how many hours have you worked today?\n"))
if hours >= 24:
       print("no, you didn't")
       
elif hours <= 0:
       print("You will recieve your pay when you do some work.")
else:
       print("That is ${} for today." .format(hours * 15))
