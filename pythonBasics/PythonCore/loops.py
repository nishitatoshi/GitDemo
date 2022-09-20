#if else
greeting = "Good Morning"

if greeting == "Morning":
    print("Condition matched")
else:
    print("Condition not matched")

#for loop
obj = [2, 3, 7, 9]
for i in obj:
    print(i)

#Sum of first 5 natural numbers 1+2+3+4+5=15
#range(i,j) -> i to j-1
summation = 0
for j in range(1,6):
    summation=summation+j
print(summation)

print("*******************************************")
#range(i,j,k) -> prints values from i to j-1 with a gap of k between them
for k in range(1,10,2):
    print(k)

print("*********************SKIPPING FIRST INDEX**********************")
for m in range(10):
    print(m)