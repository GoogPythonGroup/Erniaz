x =int(raw_input("Enter a number from  1 to 9:"))
if x>=1 and x<=3:
    s =str(raw_input("Enter the string"))
    n =int(raw_input("Enter the number of repetitions of the line:"))
    i =0
    while i<n:
        print (s)
        i =i+1
elif x>=4 and x<=6:
    m =int(raw_input("Enter the degree in which you must enter the number:"))
    print (x**m)
elif x>=7 and x<=9:
    i =0
    while i<10:
        x=x+1
        i=i+1
        print (x)
else:
    print("Input error")



