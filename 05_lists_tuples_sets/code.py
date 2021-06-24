l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

print(l)
print(l[0])
print(t[0])

l[0] = "Smith"
print(l)

l.append("Smith")
print(l)

l.remove("Smith")
print(l)

s.add("Smith")
print(s)
s.add("Smith")
print(s)