qwer = list(map(int, input().split()))

def max1(list1):
    return list1[0] if list1[0] > list1[1] and list1[0] > list1[2] else (list1[1] if list1[1] > list1[2] else list1[2])
print(max1(qwer))
