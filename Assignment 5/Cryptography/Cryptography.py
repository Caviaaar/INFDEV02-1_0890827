import sys
n = input("give a number for shifting give a number between -25 and 25: ")
line = raw_input("give a couple of letters that will be shifted by amount given just before: ")
if n in range(-25 , 25):
    for i in range(len(line)):
        intalpha = ord(line[i])
        if intalpha in range (0, 64):
            sys.stdout.write(chr(intalpha))        
        elif intalpha in range(65 , 91):
            newintalpha  = intalpha + n
            if ((newintalpha > 65) and (newintalpha < 91)):
                sys.stdout.write(chr(newintalpha))
            elif (newintalpha < 65):
                verynewintalpha = (newintalpha - 65) + 91  
                sys.stdout.write (chr(verynewintalpha))
            elif(newintalpha > 90):
                verynewintalpha = (newintalpha -91) + 65
                sys.stdout.write (chr(verynewintalpha))
        elif intalpha in range (92, 96):
            sys.stdout.write (chr(intalpha))
        elif intalpha in range(97 , 123):
            newintalpha  = intalpha + n
            if ((newintalpha > 97) and (newintalpha < 123)):
                sys.stdout.write(chr(newintalpha))
            elif (newintalpha < 97):
                verynewintalpha = (newintalpha - 97) + 123  
                sys.stdout.write (chr(verynewintalpha))
            elif(newintalpha > 122):
                verynewintalpha = (newintalpha -123) + 97
                sys.stdout.write (chr(verynewintalpha))           
        elif intalpha in range (124, 256):
            sys.stdout.write (chr(intalpha))
    print ("")