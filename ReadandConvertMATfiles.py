import numpy as np
import shutil
from PIL import Image
import os
import mat73
a = mat73.loadmat('/home/soheib/Soheib-PHD/RLVC-master/13*13-Jpegpleno-datasets/rolex_learning_center_4d_lf_mat/Buildings/Rolex_Learning_Center.mat')

adr1 = '/home/soheib/Soheib-PHD/RLVC-master/13*13-Jpegpleno-datasets/rolex_learning_center_4d_lf_mat/Buildings/PNG-Files/'
adr2 = '/home/soheib/Downloads/Jpeg_Pleno_Dataset/red_and_white_building_4d_lf_mat/Buildings/PNG-Files-X/PNG-Files-X-1/'
adr3 = '/home/soheib/Downloads/Jpeg_Pleno_Dataset/red_and_white_building_4d_lf_mat/Buildings/PNG-Files-X/PNG-Files-X-2/'
adr4 = '/home/soheib/Downloads/Jpeg_Pleno_Dataset/red_and_white_building_4d_lf_mat/Buildings/PNG-Files-X/PNG-Files-X-Finall/'
adr5 = '/home/soheib/Downloads/Jpeg_Pleno_Dataset/red_and_white_building_4d_lf_mat/Buildings/PNG-Files-X/PNG-Files-X-Finall-Renamed/'

a = a['LF']

a = a.transpose(4,3,2,1,0)

#converting all row
"""
for i in range(13):
    for j in range(13):
        b = a[i+1,j+1,:,:,0:3]
        b = (b / 65535)*255
        b = b.astype('int8')
        img = Image.fromarray(b, 'RGB')
        img.save(adr1 + str(i+1).zfill(3) + '_' + str(j+1).zfill(3) + '.png')
"""

# converting 1,3,5,7,9,11,13 row
"""
for i in range(7):
    for j in range(13):
        b = a[2*(i+1)-1,j+1,:,:,0:3]
        b = (b / 65535)*255
        b = b.astype('int8')
        img = Image.fromarray(b, 'RGB')
        img.save(adr2 + str(2*(i+1)-1).zfill(3) + '_' + str(j+1).zfill(3) + '.png')


# converting 2,4,6,8,10,12 row

for i in range(6):
    for j in range(13):
        b = a[2*(i+1),j+1,:,:,0:3]
        b = (b / 65535)*255
        b = b.astype('int8')
        img = Image.fromarray(b, 'RGB')
        img.save(adr3 + str(2*(i+1)).zfill(3) + '_' + str(14-(j+1)).zfill(3) + '.png')


#transfering all row to one folder

src_path1 = '/home/soheib/Downloads/Jpeg_Pleno_Dataset/red_and_white_building_4d_lf_mat/Buildings/PNG-Files-X/PNG-Files-X-1/'
src_path2 = '/home/soheib/Downloads/Jpeg_Pleno_Dataset/red_and_white_building_4d_lf_mat/Buildings/PNG-Files-X/PNG-Files-X-2/'
dst_path = '/home/soheib/Downloads/Jpeg_Pleno_Dataset/red_and_white_building_4d_lf_mat/Buildings/PNG-Files-X/PNG-Files-X-Finall/'

arr1 = os.listdir(src_path1)
arr1.sort()
arr2 = os.listdir(src_path2)
arr2.sort()

print(arr1)
print(arr2)

for i in range(len(arr1)):
    shutil.move(src_path1 + arr1[i], dst_path)

for j in range(len(arr2)):
    shutil.move(src_path2 + arr2[j], dst_path)

"""
"""
#rename the png files

adr10 = '/home/soheib/Soheib-PHD/RLVC-master/13*13-Jpegpleno-datasets/rolex_learning_center_4d_lf_mat/Buildings/PNG-Files_Resized/'

arr = os.listdir(adr10)
arr.sort()
print(arr)


for i in range(len(arr)):
    os.rename(adr10+arr[i], adr10+'f'+str(i+1).zfill(3)+'.png')

"""
#Resize the PNG files
"""
adr6 = '/home/soheib/Soheib-PHD/RLVC-master/13*13-Jpegpleno-datasets/rolex_learning_center_4d_lf_mat/Buildings/PNG-Files/'
adr7 = '/home/soheib/Soheib-PHD/RLVC-master/13*13-Jpegpleno-datasets/rolex_learning_center_4d_lf_mat/Buildings/PNG-Files_Resized/'

adr8 = '/home/soheib/Soheib-PHD/RLVC-master/13*13-Jpegpleno-datasets/rolex_learning_center_4d_lf_mat/Buildings/PNG-Files-X/PNG-Files-X-Finall-Renamed/'
adr9 = '/home/soheib/Soheib-PHD/RLVC-master/13*13-Jpegpleno-datasets/rolex_learning_center_4d_lf_mat/Buildings/PNG-Files-X-Resized/'

arr = os.listdir(adr8)
arr.sort()
print(arr)

for i in range(len(arr)):
    a = Image.open(adr8+arr[i])
    a = a.resize((624,432))
    a.save(adr9+arr[i])
"""

#First Test

"""
b = a[3,3,:,:,0:3]

b = (b / 65535)*255

b = b.astype('int8')

img = Image.fromarray(b, 'RGB')

img.show()

img.save('/home/soheib/Soheib-PHD/1.png')

"""
