
tuple_1 = (2, 3, 4, "hello python", False)
print("1. Tuple:", tuple_1)
print("Jumlah element:", len(tuple_1))


tuple_1 = (2, 3, 4, 5)
print("\n2. Akses index:")
print("elem 0:", tuple_1[0])
print("elem 1:", tuple_1[1])


tuple_2 = ('ultra instinc shaggy', 'nightwing', 'noob saibot')
print("\n3. Perulangan:")
for t in tuple_2:
    print(t)


print("\n4. Perulangan dengan index:")
for i in range(0, len(tuple_2)):
    print("index:", i, "elem:", tuple_2[i])


print("\n5. Enumerate:")
for i, v in enumerate(tuple_2):
    print("index:", i, "elem:", v)


tuple_1 = (10, 70, 20)
n = 70
print("\n6. Cek element:")
if n in tuple_1:
    print(n, "is exists")
else:
    print(n, "is NOT exists")


tuple_nested = ((0, 2), (0, 3), (2, 2), (2, 4))
print("\n7. Nested tuple:")
for row in tuple_nested:
    for cell in row:
        print(cell, end=" ")
    print()


data = [
    ("ultra instinc shaggy", 1, True, ['detective', 'saiyan']),
    ("nightwing", 3, True, ['teen titans', 'bat family']),
]

data.append(("noob saibot", 6, False, ['brotherhood of shadow']))
data.append(("tifa lockhart", 2, True, ['avalanche']))

print("\n8. List berisi tuple:")
print("name | rank | win | affiliation")
print("------------------------------")
for row in data:
    for cell in row:
        print(cell, end=" | ")
    print()


alphabets = tuple('abcdefgh')
print("\n9. String ke tuple:")
print(alphabets)


numbers = tuple([2, 3, 4, 5])
print("\n10. List ke tuple:")
print(numbers)


r = range(0, 3)
rtuple = tuple(r)
print("\n11. Range ke tuple:")
print(rtuple)


first_name = "aerith gainsborough"
rank = 11
win = False
row_data = (first_name, rank, win)
print("\n12. Tuple packing:")
print(row_data)


row_data = ('aerith gainsborough', 11, False)
first_name, rank, win = row_data
print("\n13. Tuple unpacking:")
print(first_name, rank, win)


empty_tuple = ()
print("\n14. Tuple kosong:")
print(empty_tuple)


data = [
    ("ultra instinc shaggy", 1, True, ('detective', 'saiyan')),
    ("nightwing", 3, True, ('teen titans', 'bat family')),
    ("kucing meong", 7, False, ()),
]

print("\n15. Data tuple lengkap:")
for row in data:
    print(row)
