mix_list=["應收帳款",3000000,3.14159,"應付帳款",173,8.8787878787878,"AR","AP"]

#創建空列表
int_list=[]
string_list=[]
float_list=[]
for i in mix_list:
    if isinstance(i,int):
        int_list.append(i)
    elif isinstance(i,str):
        string_list.append(i)
    elif isinstance(i,float):
        float_list.append(i)
print("整數列表: ",int_list)
print("字串列表: ",string_list)
print("浮點數列表: ",float_list)
    