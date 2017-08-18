plt.figure()

plt.subplot(1, 3, 1)
plt.title('Linear')
data1 = np.random.multivariate_normal([2, 0], [[0.4,0],[0,0.4]], 50)
data2 = np.random.multivariate_normal([0, 2], [[0.4,0],[0,0.4]], 50)
x = data1[:, 0]
y = data1[:, 1]
plt.scatter(x, y)
x = data2[:, 0]
y = data2[:, 1]
plt.scatter(x, y)

plt.subplot(1, 3, 2)
plt.title('Non-linear')
data1 = np.random.multivariate_normal([0, 0], [[0.2,0],[0,0.2]], 50)
data2 = np.random.multivariate_normal([0, 0], [[0.8,0],[0, 0.8]], 30000)
mask = np.abs(data2[:, 0]) > np.abs(data1[:, 0]).max() + 0.5
mask = mask + np.abs(data2[:, 1]) > np.abs(data1[:, 1]).max() + 0.5
data2 = data2[mask]
data2 = data2[np.random.choice(data2.shape[0], 50, replace=False), :]
x = data1[:, 0]
y = data1[:, 1]
plt.scatter(x, y)
x = data2[:, 0]
y = data2[:, 1]
plt.scatter(x, y)

plt.subplot(1, 3, 3)
plt.title('Inseparable')
data1 = np.random.multivariate_normal([0, 0], [[0.4,0],[0,0.4]], 50)
data2 = np.random.multivariate_normal([0, 0], [[0.4,0],[0,0.4]], 50)
x = data1[:, 0]
y = data1[:, 1]
plt.scatter(x, y)
x = data2[:, 0]
y = data2[:, 1]
plt.scatter(x, y)
