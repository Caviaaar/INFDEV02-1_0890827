size = int(raw_input("how rows do you want a triagle to be? "))
for i in range(size):
    space = (size -i - 1 ) *" "
    traingle = (2*i+1)  * "*"
    print space + traingle
print "done"
    
