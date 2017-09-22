algs = ('Random', 'Ours', 'DQN')
y_pos = np.arange(len(algs))
colors = ['#1f77b4', '#203651', '#65829b']

# Max score
score = [1, 17, 319]
plt.subplot(2, 3, 1)
plt.bar(y_pos, score, align='center', color=colors)
plt.xticks(y_pos, algs)
plt.title('Max score (Breakout)')
plt.ylabel('Score')

score = np.array([-20, -9, 19]) + 21
plt.subplot(2, 3, 2)
plt.bar(y_pos, score, align='center', color=colors)
plt.xticks(y_pos, algs)
plt.title('Max score (Pong)')
plt.ylabel('Score')

score = [174, 469, 1125]
plt.subplot(2, 3, 3)
plt.bar(y_pos, score, align='center', color=colors)
plt.xticks(y_pos, algs)
plt.title('Max score (Space Invaders)')
plt.ylabel('Score')

# Limited score
score = [1, 17, 2]
plt.subplot(2, 3, 4)
plt.bar(y_pos, score, align='center', color=colors)
plt.xticks(y_pos, algs)
plt.title('Score @ 100k samples (Breakout)')
plt.ylabel('Score')

score = np.array([-20, -9, -20]) + 21
plt.subplot(2, 3, 5)
plt.bar(y_pos, score, align='center', color=colors)
plt.xticks(y_pos, algs)
plt.title('Score @ 100k samples (Pong)')
plt.ylabel('Score')

score = [174, 469, 145]
plt.subplot(2, 3, 6)
plt.bar(y_pos, score, align='center', color=colors)
plt.xticks(y_pos, algs)
plt.title('Score @ 100k samples (Space Invaders)')
plt.ylabel('Score')

################################################################################
plt.figure()
algs = ('Ours', 'DQN')
y_pos = np.arange(len(algs))
colors = ['#203651', '#65829b']

# Log samples
score = np.array([100000, 19250000])
plt.subplot(2, 3, 1)
plt.bar(y_pos, score, align='center', color=colors, log=True)
plt.xticks(y_pos, algs)
plt.title('Samples (Breakout)')
plt.ylabel('Number of samples')

score = np.array([100000, 35250000])
plt.subplot(2, 3, 2)
plt.bar(y_pos, score, align='center', color=colors, log=True)
plt.xticks(y_pos, algs)
plt.title('Samples (Pong)')
plt.ylabel('Number of samples')

score = np.array([100000, 31500000])
plt.subplot(2, 3, 3)
plt.bar(y_pos, score, align='center', color=colors, log=True)
plt.xticks(y_pos, algs)
plt.title('Samples (Space Invaders)')
plt.ylabel('Number of samples')

# Efficiency
np.set_printoptions(suppress=True)
score = np.array([17/100000., 319/19250000.])
print score
plt.subplot(2, 3, 4)
plt.bar(y_pos, score, align='center', color=colors, log=True)
plt.xticks(y_pos, algs)
plt.title('Efficiency (Breakout)')
plt.ylabel('Reward per sample')

score = np.array([12/100000., 40/35250000.])
print score
plt.subplot(2, 3, 5)
plt.bar(y_pos, score, align='center', color=colors, log=True)
plt.xticks(y_pos, algs)
plt.title('Efficiency (Pong)')
plt.ylabel('Reward per sample')

score = np.array([460/100000., 1125/31500000.])
print score
plt.subplot(2, 3, 6)
plt.bar(y_pos, score, align='center', color=colors, log=True)
plt.xticks(y_pos, algs)
plt.title('Efficiency (Space Invaders)')
plt.ylabel('Reward per sample')

################################################################################
