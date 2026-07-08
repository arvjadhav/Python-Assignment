def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
        

def main():
    a=int(input("enter the number"))
    ret=factorial(a)
    print("factorial:",ret)


if __name__=="__main__":
    main()