# 세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다.
# 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

# 옮기는 과정을 찾는 함수 Hanoi() 선언하고, Hanoi(n) = Hanoi(n-1)에서 2<->3, 1->3 삽입, Hanoi(n-1)에서 1<->2 
# n=1일 때 Hanoi(n)은 1->3
# 리스트의 리스트 result 선언.   



# def convert(arr, a, b):
#     # print(arr)
#     res = []
#     for i in arr:
#         temp = copy.deepcopy(i)
#         for j in range(len(temp)):
#             if(temp[j] == a):
#                 temp[j] = b
#                 # print(temp)
#             elif(temp[j] == b):
#                 temp[j] = a
#                 # print(temp)
#         res.append(temp)
#         # print("append  ", temp)
#     return res
                

result=[]
def hanoi(n, a, b, c):
    if(n == 1):
        result.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        result.append([a,c])
        hanoi(n-1, b, a, c)

#convert test
# print(convert([[1,2],[2,3],[2,1]], 1, 3))

hanoi(int(input()), 1, 2, 3)
print(len(result))
for i in result:
    print(i[0], i[1])

# import copy
# def convert(arr, a, b):
#     res = []
#     for i in arr:
#         temp = copy.deepcopy(i)
#         for j in range(len(temp)):
#             if(temp[j] == a):
#                 temp[j] = b
#             elif(temp[j] == b):
#                 temp[j] = a
#         res.append(temp)
#     return res                
# def hanoi(n):
#     if(n == 1):
#         return [[1,3]]
#     else:
#         return convert(hanoi(n-1), 2, 3) + [[1,3]] + convert(hanoi(n-1), 1, 2)
# res = hanoi(int(input()))
# print(len(res))
# for i in res:
#     print(i[0], i[1])