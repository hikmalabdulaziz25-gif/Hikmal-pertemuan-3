
seq = [i * 2 for i in range(5)]
print("1.", seq)


seq = [i for i in range(10) if i % 2 == 1]
print("2.", seq)


seq = [(i * (2 if i % 2 == 0 else 3)) for i in range(1, 10)]
print("3.", seq)


list_x = ['a', 'b', 'c']
list_y = ['1', '2', '3']
seq = [x + y for x in list_x for y in list_y]
print("4.", seq)


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = [[row[i] for row in matrix] for i in range(4)]
print("5.", transposed)
