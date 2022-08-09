import numpy as np
import json
import glob

for i in glob.glob('bns_generative_extras*'):

    with open(i,'r') as f:
        d = json.load(f)

    times = np.array(d['times'])
    mags = np.array(d['model_observations'])
    bands = np.array(d['all_bands'])

    out = i.split('extras_')[-1].split('.json')[0] + '.txt'


    d1 = list(zip(times[bands=='u'], mags[bands=='UVW2'], mags[bands=='UVM2'], mags[bands=='UVW1'], mags[bands=='u'], mags[bands=='B'], mags[bands=='g'], mags[bands=='V'], mags[bands=='c'], mags[bands=='r'], mags[bands=='w'], mags[bands=='o'], mags[bands=='i'], mags[bands=='z'], mags[bands=='y'], mags[bands=='J'], mags[bands=='H'], mags[bands=='K']))

    np.savetxt(out,d1,fmt='%.3f',header='day W2 M2 W1 u B g V c r w o i z y J H K')
