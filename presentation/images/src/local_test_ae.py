from deep_ifs.extraction.Autoencoder import Autoencoder
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
from time import sleep
import imageio
import os
from glob import glob
from tqdm import tqdm

# plt.ion()
sars = np.load('../../data/BreakoutDeterministic-v3_57-eps05-500k/sars_0.npy')
ae = Autoencoder((4, 108, 84),
                 n_features=640,
                 batch_size=32,
                 nb_epochs=1,
                 binarize=True,
                 binarization_threshold=0.1)
ae.load('autoencoder_ckpt.h5')



frames = range(0, 100)
anim_1 = []  # Feature maps

for f in tqdm(frames):
    img = sars[f][0]  #1259
    
    pred = ae.predict(np.expand_dims(img, 0)) * 255
    feat = ae.all_features(np.expand_dims(img, 0)).reshape(16, 8, 5)

    fig = plt.figure(figsize=(12, 6), dpi=100)
    '''
    fig.add_subplot(1, 4, 1)
    plt.imshow(img[0], cmap='gray')
    plt.xticks([])
    plt.yticks([])
    
    '''
    fig.add_subplot(1, 4, 2)
    plt.imshow(feat[2], cmap='hot')
    plt.xticks([])
    plt.yticks([])
    
    fig.add_subplot(1, 4, 3)
    plt.imshow(feat[5], cmap='hot')
    plt.xticks([])
    plt.yticks([])
    
    fig.add_subplot(1, 4, 4)
    plt.imshow(feat[11], cmap='hot')
    plt.xticks([])
    plt.yticks([])   
    
    
    filename = 'frame_%s.png' % f
    
    plt.tight_layout()
    
    fig.savefig(filename, bbox_inches='tight')
    plt.close()
    anim_1.append(imageio.imread(filename))

imageio.mimsave('features.gif', anim_1, duration=0.1)
for f in glob('frame_*.png'):
    os.remove(f)
    

