 run = True
 while run:   
    import time

    print("Hi!!!!!")
    time.sleep(1)
    #the name input
    name =input("what's your name??? ")
    time.sleep(1)
    print("Hello "+name)
    time.sleep(1)
    print("i will now calculate your old")
    time.sleep(1)
    #the age input
    age =  str(int(input("who old are you: ")))
    time.sleep(2)
    #not so important just for fun
    print("10%")
    time.sleep(1)
    print("20%")
    print("30%")
    time.sleep(1)
    print("50%")
    print("60%")
    time.sleep(1)
    print("80%")
    print("100%")
    time.sleep(1)
    print("well you are "+age+" old")
    print("hmmmmmm")
    time.sleep(1)
    #the calculate
    print("i think you are about "+str(int(age)*12*31)+" days")
    time.sleep(1)
    print(str(int(age)*12*31*24)+" hours")
    time.sleep(1)
    print(str(int(age)*12*31*24*60)+" mineuts")
    time.sleep(1)
    print(str(int(age)*12*31*24*60*60)+" seconds")
    time.sleep(1)
    restart = input('do you want to try again: ')
    if restart == "yes":
        run = True
    if restart == "no":
        run = False
