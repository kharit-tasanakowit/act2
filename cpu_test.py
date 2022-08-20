import time
timeList = []
x = time.time()
for i in range(50000):
    timeList.append(time.time()-x)
filename = "test.txt"
f = open(filename, "w")
for i in range(50000):
    f.write(str(i)+", "+str(timeList[i])+"\n")
f.close()
