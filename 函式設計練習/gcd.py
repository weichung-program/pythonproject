#最大公因數
def gcd(a,b):
    while b != 0:
        a,b= b,a%b
    return a
#最小公倍數
def lcm(a,b):
    return a * b // gcd(a, b)
a, b = map(int, input("輸入兩個正整數: ").split())
# 計算
g = gcd(a, b)
l = lcm(a, b)
# 輸出結果
print(f"\n最大公因數為: {g}")
print(f"\n最小公倍數為: {l}")



#recursive function 
# def multiply_list(nums):
#     if  not  nums:
#         return 1
#     else:
#         return nums[0]*multiply_list(nums[1:])
# print(multiply_list([2,3,59,66]))


