def list1(a):
    sum=0
    for i in a:
        sum=sum+i
    return sum





def main():
    data=[]
    number=int(input("enter the number of elements"))

    for i in range(number):
        no=int(input("enter number"))
        data.append(no)
    res=list1(data)
    print("addition is:",res)


if __name__ =="__main__":
    main()