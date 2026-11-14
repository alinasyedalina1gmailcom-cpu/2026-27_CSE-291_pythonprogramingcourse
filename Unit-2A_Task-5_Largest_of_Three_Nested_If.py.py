x=int(input("enter the number:"))
y=int(input("enter the number:"))
z=int(input("enter the number:"))
if x>=y:
   if x>=z:
        largest=x
   else:
        largest=z
else:   
    if y>=z:
        largest=y
    else:
        largest=z
        print(f"largest={largest}(among{x},{y},{z})")