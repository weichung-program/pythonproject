
grade_list=[88,86,94,72,83] #新增成績list
grade_list[3]=75#把第三個元素改成75
print("由小到大排序 : ",sorted(grade_list))#排序(由小到大)
grade_list.extend([91,60,54,72,81])#增加心新的元素
print("由小到大排序 : ",sorted(grade_list))#新增後排序(小到大)
print ("最高分是 : ", max(grade_list))
print("最低分是 : ", min(grade_list))
print("全距是 : ", max(grade_list)-min(grade_list))
print("平均是: ",sum(grade_list)/len(grade_list))


