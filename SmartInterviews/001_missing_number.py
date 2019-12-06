enter_input = int(input())
while enter_input:
    n = int(input())
    list1 = [int(x) for x in range(1, n+2)]
    list2 = [int(x) for x in input().split()]
    print(sum(list1) - sum(list2))
    enter_input -= 1
    