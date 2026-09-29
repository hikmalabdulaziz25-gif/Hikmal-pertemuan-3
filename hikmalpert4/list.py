
list_1 = [10, 70, 20]
print("1. Akses index:")
print(list_1[0], list_1[1], list_1[2])


n = 70
print("\n2. Cek element:")
if n in list_1:
    print(n, "is exists")
else:
    print(n, "is NOT exists")


list_2 = ['ab', 'cd', 'hi', 'ca']
print("\n3. Slicing:")
print("list_2:", list_2)
slice_1 = list_2[1:3]
print("slice_1:", slice_1)


list_2[1] = 'zk'
list_2[2] = 'sa'
print("\n4. Mengubah element:")
print(list_2)

list_1 = [10, 70, 20]
list_1.append(88)
list_1.append(87)
print("\n5. Append:")
print(list_1)


list_1 = [10, 70, 20]
list_2 = [88, 77]
list_1.extend(list_2)
print("\n6. Extend:")
print(list_1)


list_1 = [10, 70, 20]
list_2 = [88, 77]
list_3 = list_1 + list_2
print("Gabungan dengan +:", list_3)


list_3 = [10, 70, 20, 70]
list_3.insert(0, 15)
list_3.insert(2, 25)
print("\n7. Insert:")
print(list_3)


list_3 = [10, 70, 20, 70]
list_3.remove(70)
print("\n8. Remove:")
print(list_3)


list_3 = [10, 70, 20, 70]
x = list_3.pop(2)
print("\n9. Pop:")
print("list_3:", list_3)
print("removed element:", x)


list_3 = [10, 70, 20, 70]
del list_3[1]
print("\n10. Del index:")
print(list_3)


list_3 = [10, 70, 20, 70]
del list_3[1:3]
print("\n11. Del range:")
print(list_3)


list_3 = [10, 70, 20, 70]
print("\n12. Len:")
print("jumlah element:", len(list_3))


print("\n13. Count:")
print("jumlah angka 70:", list_3.count(70))


list_2 = ['ab', 'cd', 'hi', 'ca']
print("\n14. Index:")
print("index cd:", list_2.index('cd'))


list_1 = [10, 70, 20]
list_1.clear()
print("\n15. Clear:")
print(list_1)


list_1 = [10, 70, 20]
list_1.reverse()
print("\n16. Reverse:")
print(list_1)


list_1 = [10, 70, 20]
list_2 = list_1.copy()
print("\n17. Copy:")
print("list_1:", list_1)
print("list_2:", list_2)


list_1 = [10, 70, 20]
list_1.sort()
print("\n18. Sort:")
print(list_1)
