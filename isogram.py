# isogram
i=input()
k=[]
for x in i:
    if x not in k:
        k.append(x)
if len(i)==len(k):
    print('yes')
else:
    print('no')
