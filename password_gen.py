import random
i = 0;
array = ''
while (i<50):
    array += chr(random.randrange(33, 126, 1))
    i+=1
print array    
