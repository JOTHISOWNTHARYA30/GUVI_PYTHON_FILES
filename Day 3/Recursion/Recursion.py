'''def get_data(data):
    print(data)

get_data(2,3,1,4,5)'''

'''def profile(name,age=18):
    print("My Name is",name,"age is",age)
profile("Sowntharya")'''


'''def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))'''

'''def number(n):
    if n%2==0:
      return"even"
    else:
        return"odd"
print(number(6))'''

'''def area(n):
    pi=3.1415
    area=pi*n*n
    return area
print(area(3))'''

'''exp=lambda x,y,z : x+y+z
print(exp(5,5,5))'''

'''lst=[1,2,3,4,5]
mul_by_5= list(map(lambda x:x*5,lst)
print(mul_by_5)

odd=list(filter(lambda x:x%2==1,lst))
print(odds)'''


L=[2,3,4,5]
odds=list(filter(lambda x:x<3,L))
print(odds)

L=[1,2,3,4,5,6]
even=list(filter(lambda x:x%2==0,L))
print(even)
mul_by_2=list(map(lambda even:even*2,even))
print(mul_by_2)








