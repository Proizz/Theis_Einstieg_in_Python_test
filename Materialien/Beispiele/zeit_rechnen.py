import time

z_start = 2022, 2, 15, 23, 55, 0, 0, 0, 0
print("Start:", time.strftime("%d.%m.%Y %H:%M:%S", z_start))
mk_start = time.mktime(z_start)

z_ende = 2022, 2, 16, 0, 5, 15, 0, 0, 0
print("Ende: ", time.strftime("%d.%m.%Y %H:%M:%S", z_ende))
mk_ende = time.mktime(z_ende)
print()

print("Differenz:")
diff_sek = mk_ende - mk_start
diff_min = diff_sek/60
diff_std = diff_min/60
diff_tag = diff_std/24

print(diff_sek, "Sekunden")
print(diff_min, "Minuten")
print(diff_std, "Stunden")
print(diff_tag, "Tage")
