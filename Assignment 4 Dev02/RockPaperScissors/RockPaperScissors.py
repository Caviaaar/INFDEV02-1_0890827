playerone = raw_input("Rock, Paper or Scissor player one: ").lower()
playertwo = raw_input("Rock, Paper or Scissor player two: ").lower()
    
if (playerone and playertwo in ("rock", "paper","scissor")):
    if (playerone == playertwo):
       print ("it's a tie")
    elif (playerone == "rock" and playertwo == "scissor"):
       print "rock crushes scissor"
       print "player one wins"
    elif (playerone== "scissor" and playertwo =="paper"):
        print " Scissor cuts Paper"
        print "player one wins"
    elif  (playerone== "paper" and playertwo == "rock"):
        print "paper covers rock"
        print "player one wins"
    else:
        if (playertwo == "rock"):
            print "rock crushes scissor"
        elif (playertwo == "scissor"):
            print " Scissor cuts Paper"
        else:
            print "paper covers rock"
        print "player two wins"
 

# rock crushes Scissors 
# Paper covers Rock
# Scissors cuts Paper
# same ties