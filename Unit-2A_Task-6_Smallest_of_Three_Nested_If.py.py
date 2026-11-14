x=int(input("enter the number"))
y=int(input("enter the number"))
z=int(input("enter the number"))
if x<=y:
    if x<=z:
        smallest=x
    else:
        smallest=z
else:
    if y<=z:
        smallest=y
    else:
        smallest=z
        print(f"samllest={smallest}(among{x},{y},{z})")