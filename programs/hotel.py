room_no =[ 1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]
d = dict()
for room in room_no:
    d[room] = d.get(room,0)+1

for k,v in d.items():
    if v == 1:
        print("the room number is:",k)
