import time

tic=time.perf_counter()
i=999999

for j in range(i):
    print(j)

toc=time.perf_counter()
print(toc-tic)
