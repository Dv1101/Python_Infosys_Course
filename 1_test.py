import time

print('Enter Number')
num=input()
num=int(num)

prime=True

#time.clock() is removed in python 3.8
tic=time.perf_counter()
for i in range(2,num):
    if num%i == 0:
        prime=False
        break

if prime:
    print('Number is prime')
else:
    print('Number is not prime')

toc=time.perf_counter()

print('Time Taken is',toc-tic,"seconds.")
