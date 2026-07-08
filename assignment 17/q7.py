def patern(num):
    for i in range(1,num):
        for j in range(1,num+1):
            print(j, end=" ")
        print()

def main():
    number=int(input("enter the number"))

    ret=patern(number)

if __name__=="__main__":
    main()