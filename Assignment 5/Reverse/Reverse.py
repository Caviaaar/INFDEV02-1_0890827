import sys
line = raw_input("Please enter something: ")
print (line)
size = len(line)
for i in range (size):
  reversed = line[size-i-1]
  sys.stdout.write (reversed)
print("")
  
