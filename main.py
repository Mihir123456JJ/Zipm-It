name=["Mihir","Atharv","Vansh","Dev"]
roll_number=[12,23,76,43]
res=zip(name,roll_number)
print(list(res))
x1=[1,2,3,4,5,6,7]
x2=[2,5,3,8,6,9,11]
for i,j in zip(x1,x2[::-1]):
    print(i,j)
course=["Math 1","English 5","Science 1"]
code=[22123,55,858]
dic1={course:code for course,code in zip(course,code)}
print(dic1)
