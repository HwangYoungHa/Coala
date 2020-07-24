data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251", "조회수: 13,432", "조회수: 998"]
sum = 0

#level 1
for i in data:
    print(i)
print("\n")
#level 2
for views in data:
    print(views[5:])
print("\n")
#level 3
for views in data:
    temp = int(views[5:].replace(",", ""))
    sum = sum + temp
print("총 합: %d"%sum)