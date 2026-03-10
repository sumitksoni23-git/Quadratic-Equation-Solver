a=int(input("if a(X)2 + b(X) + c = 0 is the Quadratic, enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

if b**2>4*(a*c):
    print(f"First root is: {((-1)*(b)+(b**2-4*a*c)**(1/2))/2*a}")
    print(f"Second root is: {((-1)*(b)-(b**2-4*a*c)**(1/2))/2*a}")


elif(b**2==4*(a*c)):
    print(f"Both roots are: {((-1)*(b))/2*a}")

elif(b**2<4*(a*c)):

    p=(-1)*(b)
    q=((-1)*(b**2-4*a*c))
    r=2*a
    print(f"First root is: ",p,"+","_/-",q,"i","/",r)
    print(f"Second root is: ",p,"-","_/-",q,"i","/",r)


