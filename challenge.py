import os

primeList = []

for num in range(2,250):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           primeList.append(num)

f = open("results.txt", 'w')
f.write(str(primeList))
f.close()
