# a=int(input("Enter the count: "))
# num1=0
# num2=1
# i=1
# while i<=a:
#     num=num1+num2
#     print(num,end="\n")
#     i=i+1
#     num1,num2=num2,num

def fibonacci(n):
    if n<0:
        print("input error")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(int(input("Enter the count:"))))

