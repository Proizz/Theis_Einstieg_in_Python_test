import time

z_start = time.time()
print("Start:", z_start)
for i in range(5):
    time.sleep(2)
    print(time.time())
z_ende = time.time()
print("Ende:", z_ende)

differenz = z_ende - z_start
print("Differenz:", differenz)
