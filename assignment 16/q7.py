#if div by 5 return true, if not false

def check():
    num=int(input("enter the number"))
    if num % 5==0:
        print("True")
    else:
        print("False")
    
def main():
    check()

if __name__=="__main__":
    main()