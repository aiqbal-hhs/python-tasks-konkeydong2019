import time

one = int(1)
for i in range (1, 11):
    print(i * one)
    time.sleep(1)

sf_seed = int(input("how many sunflower seeds will you take?\n"))
print("That will be ${}" .format(0.99 * sf_seed))
