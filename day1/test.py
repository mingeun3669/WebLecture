a1 = int(input())
for i in range(0x18) :
    print((i ^ (a1 + i)) + 2 * i )