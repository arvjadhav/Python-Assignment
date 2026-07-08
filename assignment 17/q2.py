def patern(num):
    for i in range(num):
        for j in range(num):
            print("*", end=" ")
        print()

def main():
    number=int(input("enter the number"))

    ret=patern(number)

if __name__=="__main__":
    main()