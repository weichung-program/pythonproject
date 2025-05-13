en_dictionary={                  #建立字典
    "personnel":"員工",
    "manner":"態度",
    "assume":"承擔",
    "demonstrate":"示範",
    "charge":"責任"
}
new_words = {                   #新的字
    "feature": {"特徵", "特色", "功能"},
    "goal": {"目標", "球門", "得分"},
    "oyster": {"牡蠣", "生蠔"},
    "win": {"贏得", "勝利"},
    "yield": {"產生", "屈服", "收益"}
}
en_dictionary.update(new_words) #更新字典裡的字詞
print("這本字典收納了",len(en_dictionary),"個英文字。")

print("按英文字母排序",end=" ") 
for word in sorted(en_dictionary.keys()): #按英文字母排序,並使用迴圈
    print(word,end=',')

   