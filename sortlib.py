from heap import *

def selection_sort(u):
   if len(u)==0:
      return False

   for i in range(0,len(u)-1,1):
      minIdx = i
      for j in range(i+1,len(u),1):
         if u[j]<u[minIdx]:
            minIdx = j
#      print("minIdx is " + str(minIdx))
      if minIdx != i:
         temp = u[i]
         u[i] = u[minIdx]
         u[minIdx] = temp
#      print(list(u))

   return True

def heapify(u):

   sorted = False
   while(sorted == False):
      sorted = True
      for k in range(1,len(u),1):
         if k%2==0:
            p = int((k-2)/2)
         else:
            p = int((k-1)/2)
         if u[p]<u[k]:
            temp = u[p]
            u[p] = u[k]
            u[k] = temp
            sorted = False
#   print("heap is " + str(u))
   return True

def reheapify(u,end):
   sorted = False
   while (sorted == False):
      sorted = True
      for i in range(1,end,1):
         if (i%2==0):
            p = int((i-2)/2)
         else:
            p = int((i-1)/2)   
         if u[p]<u[i]:
            temp = u[p]
            u[p] = u[i]
            u[i] = temp
            sorted = False
   return True 	
#   print("u is now" + str(u))


   for i in range(1,len(u),1):
#      print("u is currently " + str(u))
      temp = u[len(u)-i]
      u[len(u)-i] = u[0]
      u[0] = temp
#      print("u before reheapify is " + str(u))
      reheapify(u,len(u)-i)   
   return True


def heap_sort(u):
   heapify(u)
   for i in range(1,len(u),1):  
      temp=u[len(u)-i]
      u[len(u)-i] = u[0]
      u[0] = temp
      reheapify(u,len(u)-i)

def merge_sort(u):
   mid = int(len(u)//2)
   lU = u[0:mid]
   rU = u[mid:len(u)]
#   print("lU is " + str(lU))
#   print("rU is " + str(rU))  

 
   if len(lU)>1:
      merge_sort(lU)
   if len(rU)>1:
      merge_sort(rU)
#   while(len(1U)!=0 and len(rU)!=0):
   for i in range(0,len(u),1): 
#      print(str(u))
      if len(lU)==0:
         u[i] = rU[0]
         rU = rU[1:len(rU)]
      elif len(rU)==0:
#         print("lU is " + str(lU))
#         print("rU is " + str(rU))
         u[i] = lU[0]
         lU = lU[1:len(lU)]
      elif lU[0]>rU[0]:
         u[i] = rU[0]
         rU = rU[1:len(rU)]
      else:
         u[i] = lU[0]
         lU = lU[1:len(lU)]
    
#      print("lU is " + str(lU))
#      print("rU is " + str(rU))
   return True
      

def test():
   v1 = [10,9,8,7,6,5,4,3,2,1,0]
   v2 = [100,1,1000,9,8,7,2,2000,10]
   v3 = [100,10,1000,9,8,7,2,6,5,2,3,1]

   for i in [v1,v2,v3]:
      x=list(i)
      selection_sort(x)
      print(x)

      x = list(i)
      heap_sort(x)
      print(x)
      
      x = list(i)
      merge_sort(x)
      print(x)

   return True

#test()
