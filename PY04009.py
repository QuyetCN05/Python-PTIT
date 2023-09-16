class Sophuc:
    def __init__(self,thuc,ao) -> None:
        self.__thuc=thuc
        self.__ao=ao
    def __add__(self,other):
        res=self.__thuc+other.__thuc
        ans=self.__ao+other.__ao
        return Sophuc(res,ans)
    def __mul__(self,other):
        res=self.__thuc*other.__thuc-self.__ao*other.__ao
        ans=self.__ao*other.__thuc+self.__thuc*other.__ao
        return Sophuc(res,ans)
    def __str__(self) -> str:
        if self.__ao < 0:
            return f'{self.__thuc} - {self.__ao*(-1)}i'
        else:
            return f'{self.__thuc} + {self.__ao}i'

if __name__=='__main__':
    for i in range(int(input())):
        a,b,c,d=map(int,input().split())
        p=Sophuc(a,b)
        q=Sophuc(c,d)
        c=(p+q)*p
        d=(p+q)*(p+q)
        print(c,d,sep=', ')
        

        