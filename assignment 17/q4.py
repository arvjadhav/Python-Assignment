def factorial(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    return sum
            
        

def main():
    a=int(input("enter the number"))
    ret=factorial(a)
    print("factorial:",ret)


if __name__=="__main__":
    main()