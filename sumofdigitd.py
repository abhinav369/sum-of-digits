val = int(input())
lis = []
i = 1
while i <= val :
    x = input()
    
    for a in lis :
        y = x % 10
        x = x / 10
        lis.append(y)
    for ele in range(0, len(lis)):
        total = total + lis[ele]
        print(total)
    i = i + 1
