import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 9, 20)
y = x ** 3
z = x ** 2
figure = plt.figure()

# axes = figure.add_axes([0.1,0.1,0.8,0.8])        # değerler 1 olursa ekranın tamamını kaplar
#                                                 # (soldan sağa, aşağıdan yukarı) -> konum ayarları, (sağdan sola, aşağıdan yukarıya) -> boyut ayarları
# axes.plot(x,y,"b")
# axes.set_xlabel("X Ekseni")
# axes.set_ylabel("Y Ekseni")
# axes.set_title("Küp")
#
# axes = figure.add_axes([0.15,0.6,0.25,0.25])        # değerler 1 olursa ekranın tamamını kaplar
#                                                 # soldan sağa, aşağıdan yukarı, sağdan sola, yukardan aşağıya kaydırma yapa
#
# axes.plot(x,z,"r")
# axes.set_xlabel("X Ekseni")
# axes.set_ylabel("Y Ekseni")
# axes.set_title("Kare")

# plt.legend()                                              # sol üstte grafiklerin özetini veriyor

axes = figure.add_axes([0,0,1,1])

axes.plot(x, z, label = "Kare")
axes.plot(x, y, label=" Küp")
axes.legend(loc=2)                                          # 1 sol üst, 2 sağ üst, 3 sol alt, 4 sağ alt

plt.show()