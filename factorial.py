num=7
factorial=1
if num<0:
    print("sorry,factorial doesnot exist for negative numbers")
elif num==0:
    print("the factorial of 0 and 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of",num,"is",factorial)
