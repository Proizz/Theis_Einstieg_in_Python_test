import sys, urllib.request
try:
    u = urllib.request.urlopen \
        ("http://localhost/Python310/url_lesen.htm")
except:
    print("Fehler")
    sys.exit(0)

li = u.readlines()
u.close()
for element in li:
    print(element)
