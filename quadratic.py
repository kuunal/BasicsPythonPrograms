import cmath

def main():
    
    try:
        print("Enter three values")
        a = int(input())
        b = int(input())
        c = int(input())
    except ValueError:
        print("Please provide valid input!")
        main()
    else:
        delta = b*b-(4*a*c)
        print(delta)
        x1 = -b+cmath.sqrt(delta)/(2*a)
        x2 = -b-cmath.sqrt(delta)/(2*a)
        print(x1,x2)

main()