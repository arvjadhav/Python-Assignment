import module

def main():
    a1=int(input("enter the first number"))
    v1=int(input("enter second number"))

    ret=module.add(a1,v1)
    ret1=module.sub(a1,v1)
    ret2=module.mul(a1,v1)
    ret3=module.dev(a1,v1)


    print("addition is:",ret)
    print("substraction is:",ret1)
    print("multiplication is:",ret2)
    print("division is:",ret3)

if __name__=="__main__":
    main()