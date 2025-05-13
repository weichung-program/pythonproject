with open("C:/Users/維中/Desktop/news.txt",'r',encoding="utf-8") as f:
    while True:
        c=f.read (1)
        if c.islower():
            print(c.capitalize(),end="")
        elif c=="":
            break
        else:
            print(c,end="")


