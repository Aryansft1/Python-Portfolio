age=input()
age=int(age)
Type=input()
show=input()
price=0
offer=0
TypeMain={"normal","3d"}
showMain={"morning","afternoon","evening"}
if 0<=age<=120 and Type in TypeMain and show in showMain :
    if age>12 and age<60 :
        if Type=="normal" :
            if show=="afternoon":
                price=50000
                print(f"price : {price}")
            elif show=="morning":
                price=50000-5000
                print(f"price : {price}")
            elif show=="evening":
                price=50000+10000
                print(f"price : {price}")
        elif Type=="3d" :
            if show=="afternoon":
                price=70000
                print(f"price : {price}")
            elif show=="morning":
                price=70000-5000
                print(f"price : {price}")
            elif show=="evening":
                price=70000+10000
                print(f"price : {price}")
    elif age<=12 :
        if Type=="normal" :
            if show=="afternoon":
                offer=50000*50/100
                print(f"price : {offer}")
            elif show=="morning":
                price=50000*50/100
                offer=price-5000
                print(f"price : {offer}")
            elif show=="evening":
                price=50000*50/100
                offer=price+10000
                print(f"price : {offer}")
        elif Type=="3d" :
            if show=="afternoon":
                offer=70000*50/100
                print(f"price : {offer}")
            elif show=="morning":
                price=70000*50/100
                offer=price-5000
                print(f"price : {offer}")
            elif show=="evening":
                price=70000*50/100
                offer=price+10000
                print(f"price : {offer}")
    elif age>=60 :
        if Type=="normal" :
            if show=="afternoon":
                offer=50000*30/100
                print(f"price : {offer}")
            elif show=="morning":
                price=50000*30/100
                offer=price-5000
                print(f"price : {offer}")
            elif show=="evening":
                price=50000*30/100
                offer=price+10000
                print(f"price : {offer}")
        elif Type=="3d" :
            if show=="afternoon":
                offer=70000*30/100
                print(f"price : {offer}")
            elif show=="morning":
                price=70000*30/100
                offer=price-5000
                print(f"price : {offer}")
            elif show=="evening":
                price=70000*30/100
                offer=price+10000
                print(f"price : {offer}")
else :
    print("Error!")
        
