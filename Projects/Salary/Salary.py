try:

    hours = float (input("Enter Hours You Worked :"))
    rate = float (input ("Enter Your Rate :"))

    if 0<=hours<=168 and rate>=0 :
        if hours <= 40 :
            pay = hours * rate

        else :
            pay = 40 * rate + (hours-40) * rate * 1.5
        print(f"Pay : {pay: .2f}" )

    else :
        print("-1")
except :
    print("-1")
    
