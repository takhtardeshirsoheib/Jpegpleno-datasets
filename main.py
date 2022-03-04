
import os
from PIL import Image

adr = '/home/soheib/Soheib-PHD/RLVC-master/Dataset_Jpeg/Stone_Pillars_Outside/Stone_Pillars_Outside/'
adr1 = '/home/soheib/Soheib-PHD/RLVC-master/Dataset_Jpeg/Output/'
adr2 = '/home/soheib/Soheib-PHD/RLVC-master/Dataset_Jpeg/Output1/'
adr3 = '/home/soheib/Soheib-PHD/RLVC-master/Dataset_Jpeg/Output2/'

#"""
arr = os.listdir(adr)
arr.sort()
print(arr)
#"""
#convert ppm file to png
#"""
arr1 = []
for i in range(len(arr)):
    arr1.append(arr[i].replace(".ppm",""))

print(arr)
print(arr1)

for i in range(len(arr)):
    os.system('ffmpeg '+' -i ' + str(adr)+arr[i] + ' '+ str(adr1)+arr1[i]+ '.png')
#"""

#rename the png files
#"""
arr = os.listdir(adr1)
arr.sort()
print(arr)

for i in range(len(arr)):
    os.rename(adr1+arr[i], adr2+'f'+str(i+1).zfill(3)+'.png')

#"""
#resize the png files
#"""
arr = os.listdir(adr2)
arr.sort()
print(arr)

for i in range(len(arr)):
    a = Image.open(adr2+arr[i])
    a = a.resize((624,432))
    a.save(adr3+arr[i])
#"""