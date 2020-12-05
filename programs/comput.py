#defining the function computepay
def computepay(hrs,rate) :
    h = float(hrs)
    r = float(rate)
    price = 0.0
    if h <= 40 :
        price = h*r
    else :
        price = ((h-40)*r*1.5) + (40*r)
    return price

hrs = input("Enter Number of hours : ")
rate = input("Enter rate per hour : ")
pay = computepay(hrs,rate)
print("Pay",pay)
