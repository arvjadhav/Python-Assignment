def  check(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def main():
    number=int(input("Enter the number :"))
    Ret=check(number)
    if Ret==True:
        print("Thhe number is prime")
    else:
        print("The number is not prime")


if __name__=="__main__":
    main()