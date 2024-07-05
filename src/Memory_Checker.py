from tracemalloc import *

start()
j = []

for i in range (0, 100000):
    j.append(i)
    
print(get_traced_memory())
stop()