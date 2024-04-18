# print("x y z w")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f=(x<=y) and (y<=z) and (z <=w)
#                 if f==1:
#                     print(x,y,z,w)


#5


# for N in range(1,1000):
#     strr=""
#     N1=N
#     while N1>0:
#         strr+=str((N1%5))
#         N1//=5
          
#     if N%25==0:
#         strr=strr[-3:]+strr
#     N1=N%25
#     if N%25!=0:
#         strr1=""
#         while N1>0:
#             strr1+=str((N1)%5)
#             N1//=5
#         strr+=strr1
#     n=int(strr[::-1],5)        
#     if n>10000:
#        print(N)
#        break
       
#8
# from itertools import *

# c=1
# for i in product("АЕКПТЧ",repeat=7):
#     s="".join(i)
#     if s=="ПЕЧАТКА":##заменить "АПТЕЧКА" и вычесть из печатка аптечка и -1
#         print(c)
#         break
#     c+=1        
        
#11|       
# print(10*2**10/1000)

#12
# for n in range(3,10001):
#     s="5"+"2"*n
#     while "52" in s or "2222" in s or "1112" in s:
#         if "52" in s:
#             s=s.replace("52","11",1)
#             s=s.replace("2222","5",1)
#         else:
#             s=s.replace("1112","2",1)
#     summ=0
#     for i in s:
#         summ+=int(i)
#     if summ==1685:
#         print(n)
#13
# print(bin(110)[2:])
# print(bin(42)[2:])      

#15
# def f(A,x,y):
#     return (3*x+y>A) and (y<x) and (x<30)
# for A in range(0,1000):
#     if all(f(A,x,y)==False for x in range(1,1000) for y in range(1,1000)):
#         print(A)
#         break

#16
# from sys import *
# setrecursionlimit(1000)
# def f(n):
#     if n>10000:
#         return 42
#     if n<=10000 and n%2==0:
#         return 2*n+f(n+3)+f(n+4)+f(n+6)
#     if n<=10000 and n%2!=0:
#         return -(n+f(n+1)+f(n+3))
# print(f(9996)-f(9994))    

#17
# f=open("17.txt")
# lst=[int(x) for x in f]
# ans=[]
# summ=[]
# for i in range(1,len(lst)-4):
#     if abs(lst[i]+lst[i+1]<lst[i+2]+lst[i+3]) and abs(lst[i+2]+lst[i+3]> lst[i+4]+lst[i+5]):
#         ans.append(lst[i+2]+lst[i+3])
#         summ.append(lst[i+2]*lst[i+3])
# print(len(ans),min(summ))        

#19 20 21
# def f(a,s,n):
#     if a+s>=231: return n%2==0
#     if n==0: return 0
#     h=[f(a+4,s,n-1),f(a,s+4,n-1),f(a*3,s,n-1),f(a,s*3,n-1)]
#     return any(h) if (n-1)%2==0 else all(h)
# print([s for s in range(1,217) if f(10,s,2)])
# print([s for s in range(1,217) if not f(10,s,1) and f(10,s,3)])
# print([s for s in range(1,217) if not f(10,s,2) and f(10,s,4)])


#23

# def f(s, fin):   
#     if s == fin: return 1
#     if s > fin or s == 81: return 0    
#     return f(s + int(str(s)[:1]), fin) + f(s + 3, fin) + f(s * 2 - 1, fin)
# print(f(42,73) * f(73,89))


           #KOMPEGE


#2234
# base=7
# lst=[]
# s=51*7**12-7**3-22
# while s>0:
#     lst.append(s%base)
#     s//=base
# print(sum(lst))    


#2235
# base=15
# s=11*15**65+18*15**38-14*15**17+19*15**11+18338
# lst=[]
# while s>0:
#     lst.append(s%base)
#     s//=base
# print(len(set(lst)))    

#2033
# base=12
# s=6*144**26+11*12**75-48
# lst=[]
# while s>0:
#     lst.append(s%base)
#     s//=base
   
# print(lst.count(11))    

#1222
# s=5*216**1156-4*36**1147+6**1153-875
# base=6
# lst=[]
# while s>0:
#     lst.append(s%base)
#     s//=base
# a=lst.count(5) 
# b=lst.count(0)
# print(a-b)    

# for x in range(1,18):
#     a=int(f"9759{x}",17)+int(f"3{x}108",17)
#     if a%11==0:
#         print(a//11)


# for x in range (1,12):
#     a=int(f"3364{x}",11)+int(f"{x}7946",12) ==int(f'55{x}87',14)
#     if a:
#         print(x,int(f'55{x}87',14))

# for x in range(1,19):
#     a=1*18**4+x*18**3+2*18**2+5*18**1+3+3*18**3+2*18**2+x*18**1+8
#     if a%7==0:
#         print(x,a//7)

#15
# def f(a,x):
#     return ((x&26!=0) or (x&13!=0)) <=((x&29==0)<=(x&a!=0))

# for a in range(1,100):
#     if all(f(a,x)==1 for x in range (1,100)):
#         print(a)

# def f(a,x):
#     return (x&107==0)<=((x&55!=0)<=(x&a!=0))
# for a in range(1,100):
#     if all(f(a,x)==1 for x in range(1,100)):
#         print(a)

# def f(a,x,y):
#     return (x*y>a) and (x>y) and (x<8)
# for a in range(1,100):
#     if all(f(a,x,y)==0 for x in range (1,100) for y in range(1,100)):
#         print(a)

# def f(a,x,y):
#     return (2*x+y!=70) or (x<y) or (a<x)
# for a in range(1,300):
#     if all(f(a,x,y)==1 for x in range(1,300) for y in range(1,300)):
#         print(a)

# from itertools import *
# def f(x):
#     p=69<=x<=91
#     q=77<=x<=114
#     a=a1<=x<=a2
#     return q<=((p==q) or ((not p) <=a))
# ox=[ i/4 for i in range(69*4,115 *4)]
# m=[]
# for a1,a2 in combinations(ox,2):
#     if all(f(x)==1 for x in ox):
#         m.append(a2-a1)
# print(min(m)) 
 
# from itertools import *
# c=1
# k=sorted("АВГУСТ")
# r=6
# for i in permutations(k,r):
#     s="".join(i)
#     print(c,s)
#     c+=1

# from itertools import *
# c=1
# lst=[]
# lst1=[]
# k=sorted("МАРИНА")
# for i in product(k,repeat=8):
#     s="".join(i)
#     lst.append(s)
# lst1=sorted(set([x for x in lst]))
  
# print(lst1.index("МАРИАННА"))

# from itertools import *

# lst=[]
# for i in permutations("ВОДОПАД",r=7):
#     s="".join(i)
#     if not 'ОО' in s and not "АА" in s and not "АО" in s and not "ОА" in s:
#         lst.append(s)
# print(len(set(lst)))


# from itertools import *
# c=0
# lst=[]
# k=sorted("ВАСИЛИСА")
# for i in product(k,repeat=6):
#     s="".join(i)
#     if int(s.count("ИА"))== int(s.count("ВСЛ")):
#         lst.append(i)
# print(len(set(lst)))        
        
        
# from itertools import *
# c=0
# lst=[]
# k=sorted("АМФИБРАХИЙ",)
# for i in permutations(k):
#     s="".join(i)
#     if s[4] == "Б" in s and s[5]=="Р":
#         lst.append(s)
# print(len(set(lst)))


