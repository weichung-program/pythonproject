prime_number=[]
for number in range(2,1001):
    for i in range(2,number):
        if (number%i) ==0 :
            break
    else:    
        prime_number.append(number)
else:
    print("數值錯誤") 
