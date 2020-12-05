l1=[1 ,2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1,5 ,6, 2 ]
set1, set2 = set(), set()
for room in l1:
    if room not in set1:
        set1.add(room)
    else:
        set2.add(room)
set1.difference_update(set2)
print(set1.pop())
