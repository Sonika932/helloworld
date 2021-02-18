#odd numbers list and sum of the list
n= int(input('enter the numbers:'))
list =[]
for i in range (1,2*n,2):
    list.append(i)
print(list)
# sum of the above series
sum=0
for i in range (0,n):
    sum= sum+ list[i]

print ('sum of the series of odd numbers', sum)

# finding odd numbers from a series
n= int(input('enter the numbers of series:'))
list1= []
for i in range(0,n):
    element= int(input())
    list1.append(element)
print('input list is: ', list1)
odd_list=[]
for i in range(0,n):
    if (list1[i]+1)%2 == 0:
        odd_list.append(list1[i])
print(odd_list)
#sum of odd numbers in the list
sum1= 0

for i in odd_list:
    sum1= sum1 + i
print(sum1)


