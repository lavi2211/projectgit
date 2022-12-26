n=int(input("enter the number for mul table:"))

if(n<=0):
    print("{} is a invalid input:".format(n))
else:
    print("mul table for{}".format(n))
    print("="*50)
    for i in range(1,11):
        print("\t{}*{}={}".format(n,i,n*i))
    else:
        print("="*60)








