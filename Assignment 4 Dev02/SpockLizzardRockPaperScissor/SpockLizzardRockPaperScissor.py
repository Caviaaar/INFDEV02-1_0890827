playerone = raw_input("Rock, paper , Scissor, Spock  or  Lizard: ").lower()
playertwo = raw_input("Rock, paper , Scissor, Spock  or  Lizard: ").lower()
if playerone and playertwo in ("rock", "paper", "scissor", "spock", "lizard"):
  if (playerone == playertwo ):
    print "it's a tie" 
  elif ((playerone== "rock" and playertwo == "lizard") or (playerone== "lizard" and playertwo == "rock") ):
      if (playerone== "rock"):
          print ("player one wins")
      else:
          print ("player two wins")
      print ("rock spashed lizard")
  elif ((playerone== "rock" and playertwo == "scissor") or (playerone== "scissor" and playertwo == "rock") ):
      if (playerone== "rock"):
          print ("player one wins")
      else:
          print ("player two wins")
      print ("rock smashes scissor")
  elif ((playerone== "paper" and playertwo == "spock") or (playerone== "spock" and playertwo == "paper") ):
      if (playerone== "paper"):
          print ("player one wins")
      else:
          print ("player two wins")
      print ("paper cuts spock")
  elif ((playerone== "paper" and playertwo == "rock") or (playerone== "rock" and playertwo == "paper") ):
      if (playerone== "paper"):
          print ("player one wins")
      else:
          print ("player two wins")
      print ("paper covers rock")
  elif ((playerone== "scissor" and playertwo == "lizard") or (playerone== "lizard" and playertwo == "scissor") ):
      if (playerone== "scissor"):
          print ("player one wins")
      else:
          print ("player two wins")
      print ("scissor decapitetes lizard")
  elif ((playerone== "scissor" and playertwo == "paper") or (playerone== "paper" and playertwo == "scissor") ):
      if (playerone== "scissor"):
          print ("player one wins")
      else:
          print ("player two wins")
      print ("scissor cuts paper")
  elif ((playerone== "lizard" and playertwo == "spock") or (playerone== "spock" and playertwo == "lizard") ):
      if (playerone== "lizard"):
          print ("player one wins")
      else:
          print ("player two wins")
      print ("lizard poisons spock")
  elif ((playerone== "lizard" and playertwo == "paper") or (playerone== "paper" and playertwo == "lizard") ):
      if (playerone== "lizard"):
          print ("player one wins")
      else:
          print ("player two wins")
      print ("lizard eats paper")
  elif ((playerone== "spock" and playertwo == "rock") or (playerone== "rock" and playertwo == "spock") ):
      if (playerone== "spock"):
          print ("player one wins")
      else:
          print ("player two wins")
      print ("spock vaporizes rock")
  elif ((playerone== "spock" and playertwo == "scissor") or (playerone== "scissor" and playertwo == "spock") ):
      if (playerone== "spock"):
          print ("player one wins")
      else:
          print ("player two wins")
      print ("spock smashes scissor")
