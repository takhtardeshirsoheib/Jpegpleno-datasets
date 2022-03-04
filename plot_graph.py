import matplotlib.pyplot as plt

# line 1 points
#x1 = [0.083,0.129,0.202,0.359]
#y1 = [31.04,32.85,34.29,35.31]

x1 = [0.087,0.148,0.203,0.351]
y1 = [0.963,0.978,0.981,0.987]
# plotting the line 1 points
plt.plot(x1, y1,  color='green', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=8, label = "Bike_Jpeg Pleno")

# line 2 points
#x2 = [0.097,0.162,0.262,0.469]
#y2 = [29.57,31.51,33.10,34.18]

x2 = [0.101,0.177,0.253,0.435]
y2 = [0.936,0.954,0.971,0.981]
# plotting the line 2 points
plt.plot(x2, y2, color='red', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=8, label = "Danger_Jpeg pleno")

# line 3 points
#x3 = [0.085,0.135,0.216,0.377]
#y3 = [30.16,32.05,33.43,34.39]

x3 = [0.081,0.140,0.203,0.353]
y3 = [0.960,0.969,0.977,0.984]
# plotting the line 2 points
plt.plot(x3, y3, color='yellow', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=8, label = "Fountain_Jpeg Pleno")

# line 4 points
#x4 = [0.065,0.105,0.177,0.332]
#y4 = [31.57,33.44,34.93,36.11]

x4 = [0.075,0.141,0.205,0.362]
y4 = [0.951,0.962,0.973,0.983]
# plotting the line 2 points
plt.plot(x4, y4, color='black', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=8, label = "Stone_Jpeg Pleno")

# naming the x axis
plt.xlabel('bpp')
# naming the y axis
plt.ylabel('PSNR')
# giving a title to my graph
#plt.title('PSNR for Jpeg_pleno 15*15 Light Field Datasets')
plt.title('MS-SSIM for Jpeg_pleno 15*15 Light Field Datasets')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
