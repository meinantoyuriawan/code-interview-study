# interview from grab
# Given an string of num in binary, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

# example :
# input : '011100'
# output : 7
# explanation : 011100 = 28
# 28/2 = 14
# 14/2 = 7
# 7-1 = 6
# 6/2 = 3
# 3-1 = 2
# 2/2 = 1
# 1-1 = 0

# sums of step = 7

n = '011100'
n = '111'
temp_step = 0
lz = False
step = 0
# iterate backwards in every character, if the character is 0 then 1 step (even). If the character is 1 then 2 step (odd, substract and divide)
for i in range(len(n)-1, -1, -1):
    if int(n[i]) & 1:
        step += 2
        # store the temporary step, it is for leading zero (0 before the assignment)
        temp_step = step
        lz = False
    else:
        step += 1
        # automatically set the leading zero to true, changed if there is 1. If it is zero till the end, then use a temporary step
        lz = True
    
# print(step)
if lz:
    step = temp_step
# result = step - lz*2
result = step-1
print(result)