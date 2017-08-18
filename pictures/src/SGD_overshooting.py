x = np.linspace(-5, 5, 1000)
y = x ** 2

x2 = np.linspace(-4, -2, 10)
y2 = x2 ** 2

j = np.array([-1, 1, -1, 1, -1, 1, -1, 1, -1, 1])
x3 = x2 * j
y3 = x3 ** 2


plt.subplot(1,2,1)
plt.plot(x, y)
plt.quiver(x2[:-1], y2[:-1], x2[1:]-x2[:-1], y2[1:]-y2[:-1], angles='xy', width=0.004, color='red')
plt.xlabel('w')
plt.ylabel('f(w)')

plt.subplot(1,2,2)
plt.plot(x, y)
plt.quiver(x3[:-1], y3[:-1], x3[1:]-x3[:-1], y3[1:]-y3[:-1], scale=11.25, angles='xy', width=0.003, color='red')
plt.xlabel('w')
plt.ylabel('f(w)')
