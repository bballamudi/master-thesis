import numpy as np
import pandas as pd


def movingaverage(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')

game = 'pong'
data = pd.read_csv('%s.csv' % game)
x = data[data.phase == 'test'].average_reward.as_matrix()
x_avg = movingaverage(x, 50)

plt.figure(figsize=(1920/200., 1080/200.), dpi=200)
plt.plot(x, label='Average reward')
plt.plot(x_avg, label='Moving average reward (50 samples)')

plt.xlabel('250k training steps')
plt.ylabel('Reward')
plt.legend()

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.savefig('/home/phait/Desktop/master-thesis/pictures/experiments/baseline_%s.png' % game)

