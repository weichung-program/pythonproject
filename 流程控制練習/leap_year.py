error_count=0 #設定錯誤次數
true_count=0#設定正確次數
while True: #設定無限執行程式
    try:#試看看是否為整數
        user_inputyear=int(input("請輸入整數: "))
    except:#輸入直不是整數會跳到例外情況
        print("數值錯誤,請重新輸入!")

        error_count+=1
        if error_count==3:
          print("輸入錯誤次數過多,結束")
          break
    else:#正確的話執行以下程式碼,判斷是否為閏年規則
        if (user_inputyear % 4 == 0 and user_inputyear % 100 != 0) or (user_inputyear % 400 == 0):
            print(user_inputyear, "年是閏年")
        else:
            print(user_inputyear, "年不是閏年")

        #為成功輸入 3 次後結束    
        true_count+=1
        if true_count==3:
          print("成功輸入3次,結束")
          break
       