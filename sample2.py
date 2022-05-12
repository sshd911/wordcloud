t=1,"aaa",2,["ccc","ddd"]
print(t[1])

# Sequence Unpacking
i,s,j,l=t
print(i,s,j,l)

# タプルでイテレーションをする
for i in t:
    print('loop',i)
    