password = raw_input("enter your password: ")
passwordpoints = 0
if (password.isalpha() or password.isdigit() or password.isspace()):
    print "password is unsafe and weak"
else:
    for i in range(len(password)):
        char = ord(password[i])
        if char in range(0, 48):
            #special chars
              passwordpoints = passwordpoints + 2
        elif char in range(48, 58):
            #number chars
              passwordpoints = passwordpoints + 1
        elif char in range (58, 65):
            #special chars
              passwordpoints = passwordpoints +2
        elif char in range (65, 91):
            #lowercase alpha
             passwordpoints = passwordpoints + 0.5
        elif char in range(91, 97):
            #special chars
             passwordpoints = passwordpoints +2
        elif char in range (97, 123):
            #uppercase aplha
             passwordpoints = passwordpoints + 0.5
        elif char in range (123 ,256):
            #special chars
             passwordpoints = passwordpoints + 2
    if (passwordpoints < 5 ):
        print ("password weak")
    elif(passwordpoints < 10 ):
        print ("password medium")
    elif (passwordpoints >10 ):
        print ("password strong")