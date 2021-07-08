import random
ans=random.randint(1,20)
x=input('1~20猜一個數字')
x=int(x)
i=1
while i!=5:
    if x!=ans:
        print('猜錯了')
        x=input('1~20猜疑個數字')
        i=i+1
    else:
        print('猜對了答案是:',ans)
        break

