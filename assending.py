list = []
n= int(input('enter the number of elements:'))
for i in range (0,n):
    ele= int(input())
    list.append(ele)
print('the list is:', list)

for i in range(0,n):
    for j in range(i+1,n):
       if list[i]> list[i+1]:
            small= list[i]
            list[i]= list[i+1]
            list[i+1]= small
print('the assending order of series is:', list)