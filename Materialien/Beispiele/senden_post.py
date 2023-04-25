import urllib.request, urllib.parse

pnn = input("Bitte den Nachnamen eingeben: ")
pvn = input("Bitte den Vornamen eingeben: ")
dc = {b"nn":pnn, b"vn":pvn}
data = bytes(urllib.parse.urlencode(dc), "UTF-8")

u = urllib.request.urlopen \
   ("http://localhost/Python310/senden_post.php", data)
li = u.readlines()
u.close()
for element in li:
    print(element)
