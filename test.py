# scores = {'math':98,'english':99,'chinese':90}
#
# print(scores['math'])
# scores["PE"]=90
# print(scores)
# print(scores.get('english'))
#
# dict1 = {('daijun',18),("wangyuanyuan",20)}
# dict1 = dict(dict1)
# print(dict1.get('daijun'))
#
# ims = scores.items()
# for x,y in scores.items():
#     print(x,y)
'''import random
n = int(input("请输入一个整数:"))
list2 = []
for i in range(n):
    list2.append(random.choice('QWERTYUIOPASDFGHJKLZXCVBNM'))
print(list2)'''

src_list = [x for x in range(1,100)]
a_list = []
b_list = []
c_list = []
while len(src_list)>0:
    ele = src_list.pop()
    if ele % 3 ==0:
        a_list.append(ele)
    elif ele % 3 ==1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print(a_list)
print(b_list)
print(c_list)
