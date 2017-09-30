import numpy as np
import pandas as pd


def movingaverage(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')

game = 'pong'
data = pd.read_csv('%s.csv' % game)
x = data[data.phase == 'test'].average_reward.as_matrix()
p = np.polyfit(range(len(x)), x, 5)
z = np.poly1d(p)
x_avg = z(range(len(x)))

ours = [-9] * len(x)

plt.figure(figsize=(1920/200., 1080/200.), dpi=200)
plt.plot(x, label='Average reward')
plt.plot(x_avg, label='Polynomial trendline')
plt.plot(ours, label='Ours')

plt.xlabel('250k training steps')
plt.ylabel('Reward')
plt.legend()

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.savefig('/home/phait/Documents/master-thesis/presentation/images/results_%s.png' % game)

