num = [2,3,2,1,2,3,2,3,2,2,1,2,1,2,3,2]
num.sort()
num.append(0)

max_c = 0
new_c = 0
result = 0
i = 0

while i < len(num)-1:

    if num[i] == num[i+1]:
        new_c += 1

    if new_c >= max_c and num[i] != num[i+1]:
        max_c = new_c
        result = num[i]
        new_c = 0

    if num[i] != num[i+1]:
        new_c = 1

    i += 1
print(result)