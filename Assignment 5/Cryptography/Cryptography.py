import sys
n = input("give a number for shifting give a number between -26 and 26: ")
line = raw_input("give a couple of letters that will be shifted by amount given just before: ")
if n in range(-27 , 27):
    for i in range(len(line)):
        intalpha = ord(line[i])
        if intalpha in range (0, 64):
            sys.stdout.write(chr(intalpha))        
        elif intalpha in range(65 , 91):
            intalpha  = intalpha + n
            if ((intalpha > 65) and (intalpha < 91)):
                sys.stdout.write(chr(intalpha))
            elif (intalpha < 65):
                intalpha = (intalpha - 65) + 91  
                sys.stdout.write (chr(intalpha))
            elif(intalpha > 90):
                intalpha = (intalpha -91) + 65
                sys.stdout.write (chr(intalpha))
        elif intalpha in range (92, 96):
            sys.stdout.write (chr(intalpha))
        elif intalpha in range(97 , 123):
            intalpha  = intalpha + n
            if ((intalpha > 97) and (intalpha < 123)):
                sys.stdout.write(chr(intalpha))
            elif (intalpha < 97):
                intalpha = (intalpha - 97) + 123  
                sys.stdout.write (chr(intalpha))
            elif(intalpha > 122):
                intalpha = (intalpha -123) + 97
                sys.stdout.write (chr(intalpha))           
        elif intalpha in range (124, 256):
            sys.stdout.write (chr(intalpha))
    print ("")