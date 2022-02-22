import matplotlib.pyplot as plt
input_file = ('plt.csv','r')
temp_x1 = []
temp_y1 = []
temp_x2 = []
temp_y2 = []
for i in input_file:
  temp = i.split(',')
temp_x1.append(temp[0])
temp_y1.append(temp[1])
temp_x2.append(temp[2])
temp_y2.append(temp[3][:len(temp[3])-1)
x1_co = tuple(temp_x1[1:])
y1_co = tuple(temp_y1[1:])
x2_co = tuple(temp_x2[1:])
y2_co = tuple(temp_y2[1:])
plt.plot(x1_co,y1_co,lable='line1',color='red')
plt.plot(x2_co,y2_co,lable='line2')
plt.xlable('pid&position')
plt.ylable('__')
plt.legend()
plt.show()
