import collections
d = collections.deque([8, 18, 28])
print("Erstellt:", d)

d.appendleft(5)
print("Element angefügt:", d)
d.append(25)
print("Element angefügt:", d)
d.insert(2, 11)
print("Element eingefügt:", d)
d.extendleft([7,9])
print("Elemente angefügt:", d)
d.extend([17,19])
print("Elemente angefügt:", d)

x = 5
if x in d:
    print(f"Position von {x}: {d.index(5)}")

for i in range(5):
    li = d.popleft()
    print("Entferntes Element, links:", li)
re = d.pop()
print("Entferntes Element, rechts:", re)
print("Danach:", d)

d.rotate()
print("Nach Rotation um +1:", d)
d.rotate(-1)
print("Nach Rotation um -1:", d)
