playerone = raw_input("Rock, paper , Scissor, Spock  or  Lizard: ").lower()
playertwo = raw_input("Rock, paper , Scissor, Spock  or  Lizard: ").lower()
if playerone and playertwo in ("rock", "paper", "scissor", "spock", "lizard"):
        if (playerone == playertwo ):
            print "it's a tie" 
        elif (playerone == "rock" and (playertwo =="scissor" or "lizard")):
            if (playertwo == "scissor"):
                print "rock crushes scissor"
            else:
                print "rock crushes lizard"  
            print "player one wins"
        elif (playerone =="paper" and (playertwo == "spock" or "rock")):
            if (playertwo == "spock"):
                print "paper disproves Spock"
            else:
                print "paper covers rock"
            print "player one wins"
        elif (playerone == "scissor" and (playertwo == "lizard" or "paper") ):
            if (playertwo == "lizard"):
                print "scissor decepitates lizard"
            else:
                print "scissor cuts paper"
            print "player one wins" 
        elif (playerone == "lizard" and (playertwo == "paper" or "spock")):
            if (playertwo == "spock"):
                print "lizard poisons spock"
            else:
                print "lizard eats paper"
            print "player one wins"
        elif (playerone == "spock" and (playertwo == "rock" or "scissor")):
            if (playertwo == "rock"):
                print "spock vaporizes rock"
            else:
                print "spock smashes scissor" 
            print "player one wins"
        else:
            print "player two wins"
    