# 6. Given an unsorted array of size N that contains only non-negative integers, find a contiguous subarray which adds to a given number S. In case of multiple subarrays,
# return the subarray which comes first on moving from left to right. Eg, let us say the array is - 3, 6, 7, 5, 10. And the value of S = 12. The output should be - 7, 5
N=int(input())
N1=[0]*N
for i in range(N):
  N1[i]=input()
print(N1)
count=0
Num=int(input())
for i in range(N):
  for j in range(N):
    if int(N1[i])+int(N1[j])==Num:
      a=N1[i]
      b=N1[j]
      count+=1
  if count>0:
    print(a,b)
    break