print("\t---SIMPLE CALCULATOR---")
print('"key"   : "operation"')
print("1 : Addtion \n2 : Subraction \n3 : Multiplication \n4 : Division ")
n=int(input("Enter the key to do the operation:"))
a=int(input("Enter the value 1:"))
b=int(input("Enter the value 2:"))
if n==1:
 print("%d+%d=%d"%(a,b,a+b))
elif n==2:
 print("%d-%d=%d"%(a,b,a-b))
elif n==3:
 print("%d*%d=%d"%(a,b,a*b))
elif n==4:
 print("%d/%d=%d"%(a,b,a/b))
else:
 print("Enter the correct key to the operation:")
 
