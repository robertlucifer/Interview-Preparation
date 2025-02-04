nums=[1,3,2,6]
traget = 4
index= {}

for i , num in  enumerate(nums):
    print(i,num)#enumerate function created the index and value in two varibles
    difference = traget - num
    if difference in index:
        print ([index[difference], i])
    index[num]=i

# if you using in from dictionary it will vheck whether that key is present in that particular dictionary.
# so here we find the difference between the traget and current value and trying to find the difference value present the dictionay, we are adding the number as key and index as value because in function key for the key in hash map.

final_value=[]
for x in range(len(nums)):
    for j in range(x+1,len(nums)):
        if nums[x]+nums[j]==target:
            final_value.append(x)
            final_value.append(j)
print(final_value)