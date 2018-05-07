x = 0.5
e = 2.71828
i = -1
print()
print("F(x) = 2^x - x^2 - 0.5")
print("F'(x) = ((2^x)*ln(2)-2*x")
print()
while(1):
    i += 1
    print()
    print("ITER ",i)
    print()
    F1 = ((2**x)*0.69315)-2*x
    F = 2**x - x**2 - 0.5

    #F = ((1-x**2)**0.5)-e**x+0.1
    #F1 = (-x/((1 - x**2)**0.5))-e**x
    #F2 = (-x ** 2 / (1 - x ** 2) ** 1.5) - (1 - x ** 2) ** 0.5 - e ** x
    #print(F * F2)

    x1 = x - F/F1
    print("X = ",x)
    print("F(x) = ", F)
    print("F'(x) = ", F1)
    print("F(x)/F'(x) = ", F/F1)
    print("epsilong = ", round(abs(x1 - x), 5))
    print("X1 = ",x1)

    if(abs(x1 - x)<=0.001):
        print()
        print()
        print("end = ",x1)
        print("epsilong = ",round(abs(x1 - x),4))
        break
    else:
        x = x1