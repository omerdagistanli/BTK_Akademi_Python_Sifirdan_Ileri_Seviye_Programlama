import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y, color="red", linewidth="3")
plt.axis([0,6,0,20])

plt.title("Grafik Başlığı")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")

plt.show()