//coded by harish rane
ll=int(input("enter the lower limit"))
up=int(input("enter the upper limit"))

if ll>0:
    if up>0:
        if up<ll:
            for x in range(ll,up+1):
                print(x)
    else:
        print("given boundries are not valid")


if ll<0:
    if up<0:
        if up<ll:
            for x in range(ll,up-1,-1):
                print(x)
    else:
        print("given boundries are not valid")


if ll>0:
    if up<0:
        if up<ll:
            for x in range(ll,up-1,-1):
                print(x)
    else:
        print("given boundries are not valid")

