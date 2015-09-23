noawnser = True
while (noawnser == True):
  userCelsius = input("input celsius please: ")
  Kelvin = userCelsius + 273.15
  if userCelsius < -273.15:
      print "not a valid degree"
  else:
     print Kelvin , " K"
     noawnser = False