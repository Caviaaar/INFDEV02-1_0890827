playerone = raw_input("Rock, paper , Scissor, Spock  or  Lizard: ").lower()
playertwo = raw_input("Rock, paper , Scissor, Spock  or  Lizard: ").lower()
if playerone and playertwo in ("rock", "paper", "scissor", "spock", "lizard"):
  if (playerone == playertwo ):
    print "it's a tie" 
 