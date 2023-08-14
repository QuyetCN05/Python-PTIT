import math
def check(s):
    cnt=0
    for i in s:
        if(i== '4' or i=='7'):
            cnt+=1
    return cnt
    
if __name__=='__main__':
  s=input()
  if(check(s)==4 or check(s)==7):
      print('YES')
  else:
      print('NO')

    
       
   
    


