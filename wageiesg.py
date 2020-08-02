i = 0

while i == 0:
       days = int(input("how many days do you work per week?\n"))

       if days <= 0:
              print("get a job")
              break
       elif days > 7:
              print("there are 7 days in a week\n")
       else:
              i =1

while i == 1:
       hours = float(input("how many hours do you work everyday?\n"))

       if hours >= 24:
              print("no, you didn't")
       elif hours <= 0:
              print("You will recieve your pay when you do some work.")
       else:
              i = 2

while i == 2:
       wage = float(input("what is your hourly rate? (in dollars)\n"))

       if wage > 0:
              tha = wage * hours * days
              i = 3

if i == 3:
       print("Your weekly income is ${}" .format(tha))
       print("and after ${} tax" .format(round(tha * 0.8, 2) ))
       
