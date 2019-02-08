#4
print bin(1)

for i in range(2,6):
  print bin(i)
  
#8
print bin(0b1110 or 0b101)

#11
def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired >0 :
    return "on"
  else:
    return "off"
    
    
    
