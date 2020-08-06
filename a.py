q = int(input("length: "))
i = int(input("frequency: "))
w = 1
while True:
       
       print("a" * w)
       w += i
       if w >= q:
              while w != 1:
                     print("a" * w)
                     w -= i
