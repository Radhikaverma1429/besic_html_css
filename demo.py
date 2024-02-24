# input=int(input("Table number!.."))
# for i in range(1,11):
#     print(input*i)

# 1132

# n = int(input("Enter a number: "))
# digit_sum = 0
# while n > 0:
#     digit_sum += n % 10
#     n //= 10
# print("Sum of digits:", digit_sum)


# You are given an integer array. You are also given a number. Print the number of times the number appears in the array.
# Sample Input:
# 4 7 9 10 7 14 12 4 7 27
# 7
# Sample Output:
# 3

# arry=[4,7,9,10,7,14,12,4,7,27,2,2,2,2]
# count=0
# i=0
# value=int(input("enter a any number!..."))
# while i<len(arry):
#     if value == arry[i]:
#         count+=1
#     i+=1
# print(count)

 
# array2 = [6, 8, 9, -1, 14, 8, -3, 6];

# i=0
# while i<len(array2):
#     if(array2[i]<0):
#         print("yes")
#     else:
#         print("no")
#     i+=1


a=int(input())
b=[]
for i in range(a):
    c=int(input())
    b.append(c)
d=b
count=0
for i in d:
    if i<0:
        count+=1
print()
print(count)