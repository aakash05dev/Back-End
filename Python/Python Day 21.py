s="aaaabbcccddddffffff"

result={}

for i in s:
    if i in result:
        result[i] += 1

    else:
        result[i]=1

print(result)

big=0
for k, v in result.items():
    if v > big:
        big = v
        key = k

print("Highest key:", key)
print("Highest count:", big)

    
