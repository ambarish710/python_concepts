
# Shallow Copy
a = [1, 2, 3]
print("a: {}".format(a))
b = a
print("b: {}".format(b))

print("Changing b[0] to 55")
b[0] = 55
print("b: {}".format(b))
print("a: {}".format(a))


print("\n\n\n")


# Deep Copy
a = [1, 2, 3]
print("a: {}".format(a))
b = a[:]
print("b: {}".format(b))

print("Changing b[0] to 55")
b[0] = 55
print("b: {}".format(b))
print("a: {}".format(a))
