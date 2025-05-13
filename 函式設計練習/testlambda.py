#lambda練習

#搭配map
a=[1,2,3,7]
newa=list(map(lambda x : x*x,a))
print(newa)
#搭配filter
b=[2,4,6,9,85,22]
even=list(filter(lambda x :x%2==0,b))
print(even)
#搭配sorted
students=[("a",95),("b",90),("c",88)]
sort_stud=sorted(students,key=lambda x:x[1],reverse=True)
print(sort_stud)
#過濾數值
a=["hh",5,("5"),5.5,True]
newa=list(filter(lambda x:isinstance(x,(int,float)) and not isinstance(x , bool),a))
print(newa)

alist=[5,4,1,1,1]
mean=sum(alist)/len(alist)
var=sum((x-mean**2) for x in alist)/len(alist)
std=var**0.5
stan=list(map(lambda x: str((x-mean)/std) ,alist))
print((stan))