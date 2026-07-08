def check():

    a=int(input("enter the number"))

    if a>0:
        print("positive")
    elif a<0:
        print("negative")
    else :
        print("zero")


def main():
    check()

if __name__=="__main__":
    main()