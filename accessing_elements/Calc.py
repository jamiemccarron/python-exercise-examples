from myfile import Math
while True:
    options = {
        "adding":1,
        "subtracting":2,
        "divding":3,
        "multiplication":4,
        "square root":5,
        "cubbed root":6,
        "end code":0}
    for item in options:
        print(item)
        print(options[item])
    chouse=int(input("what formula do you want to use entre the number that matches the fromula: "))

       
    a = Math()
    #adding
    if chouse==1:
        x=int(input("enter frist number"))
        y=int(input("entre secound number"))
        print (a.add(x,y))

    #subtracting
    elif chouse==2:
        x=int(input("enter frist number"))
        y=int(input("entre secound number"))
        print (a.sub(x,y))

    #divding
    elif chouse==3:
        x=int(input("enter frist number"))
        y=int(input("entre secound number"))
        print (a.div(x,y))
           
    #Multiplication
    elif chouse==4:
        x=int(input("enter frist number"))
        y=int(input("entre secound number"))
        print(a.mult(x,y))

    #square root
    elif chouse==5:
        x=int(input("enter a number to be squared"))
        print(a.square(x))

    #cubbed root
    elif chouse==6:
        x=int(input("entre number to be cubbed"))
        print(a.cubbed(x))

    elif chouse==0:
        break
    else:
        print("you ented an invaild number")

        
