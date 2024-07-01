#ACCEPT NUMBER AND PERFORM MENUS: 1)SQUARE 2)CUBE 3)EVEN-ODD
n=int(input("enter number:"))
print("1-square \n 2-cube \n 3-even-odd")
ch=int(input("enter choice:"))
if ch==1:
 print("square",n*n)
elif ch==2:
    print("cube",n*n*n)
elif ch==3:
    if n%2==0:
        print("number is even")
    else:
        print("number is odd")
else:
    print("wrong choice")
           
               
