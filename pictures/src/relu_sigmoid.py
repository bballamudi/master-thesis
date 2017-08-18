def sigmoid(x):
    return 1. / (1. + np.exp(-x))

x = np.linspace(-5, 5, 1000)
y = np.maximum(x, 0, x)

x = np.linspace(-5, 5, 1000)
z = sigmoid(x)

plt.figure()

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title('ReLU')

plt.subplot(1, 2, 2)
plt.plot(x, z)
plt.title('Sigmoid')

