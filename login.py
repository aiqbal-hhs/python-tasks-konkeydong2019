password = "drasifmw"
lock = 1 

for i in range(3):
       while lock == 1:
              bug = input("enter the password (the password is: {})\n" .format(password))
              if bug == password:
                     print("login successful. \n\nwear the mask. \ndrink the tap water. \nlive in the pod. \neat the bug.\ndon't have kids.")
                     lock = 2
              else:
                     print("incorrect password.\n.\n.")
                     break

if lock == 1:
       print("too many failed attempts.")
