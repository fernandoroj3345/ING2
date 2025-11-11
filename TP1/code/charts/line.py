from cProfile import label
from matplotlib import pyplot as plt 

years = [2016,2017,2018,2019,2020,2021]
allstaff = [45, 46, 47, 48, 50, 51]
femstaff= [9,15,23,30,35,26]

plt.plot(years,allstaff, marker='o', linestyle='--', color='g', label='All Staff')
plt.plot(years,femstaff, marker='o', linestyle='-',color='r', label='Female Staff')
plt.title('Growth in the number of female staff')
plt.xlabel('Years')
plt.ylabel('Staff')
plt.legend()
plt.show()