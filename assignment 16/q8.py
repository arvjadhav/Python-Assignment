def fun(num):
    for i in range(num):
        print("*",end="   ")

def main():
    a=int(input("enter the number"))
    fun(a)

if __name__=="__main__":
    main()