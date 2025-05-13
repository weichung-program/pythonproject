#巢狀迴圈
#直角三角形
rows=4
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print()


#等腰三角形
rows = 20
for i in range(rows):
    # 列印空格，空格的數量等於總行數減去目前行數再減1
    for j in range(rows - i - 1): #外層 for 迴圈控制行數，i 會依次取值 0, 1, 2。
        print(" ", end="")
    # 列印星號，星號的數量等於目前行數乘以2再加1
    for k in range(2 * i + 1):#內層 for 迴圈列印空格在每一行星號列印之前，先列印空格。
                    #列印的空格數量等於(總行數-當前行數-1)。這樣可以讓星號圖案居中。
        print("*", end="")
    # 每列印完一行後換行
    print()


