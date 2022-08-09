import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import json


plt.figure(1)
plt.clf()

if len(sys.argv)>1:
    i = sys.argv[1]

mass = i[1:5]

q = i[7:11]

disk = i[13:16]

if 'a' in i:
    a = i.split('a')[1][0:3]
else:
    a = 1.0

jsonfile = 'bns_generative_M'+mass+'_q'+q+'_d0.1_v60_C0.0.json'

if os.path.exists(jsonfile):
    jsonpath = jsonfile

elif os.path.exists(os.path.join('full_output',jsonfile)):
    jsonpath = os.path.join('full_output',jsonfile)
    
else:
    print('No matching json found in this directory or full_output subdirectory')
    jsonpath = ''
    
if len(jsonpath) > 0:
    with open(jsonpath,'r') as f:
        d = json.load(f)
        
    mejecta_blue = d['bns_generative']['models'][0]['realizations'][0]['parameters']['mejecta_blue']['value'] * float(a)
    
    print('mejecta_blue = %.2e Msun' %mejecta_blue)

    mejecta_red = d['bns_generative']['models'][0]['realizations'][0]['parameters']['mejecta_red']['value']

    print('mejecta_red = %.2e Msun' %mejecta_red)

    mejecta_purple = d['bns_generative']['models'][0]['realizations'][0]['parameters']['mejecta_purple']['value'] * float(disk)/0.1
    
    print('mejecta_purple = %.2e Msun' %mejecta_purple)


    vejecta_blue = d['bns_generative']['models'][0]['realizations'][0]['parameters']['vejecta_blue']['value']
    
    print('vejecta_blue = %.2e km/s' %vejecta_blue)

    vejecta_red = d['bns_generative']['models'][0]['realizations'][0]['parameters']['vejecta_red']['value']

    print('vejecta_red = %.2e km/s' %vejecta_red)

    vejecta_purple = d['bns_generative']['models'][0]['realizations'][0]['parameters']['vejecta_purple']['value']

    print('vejecta_purple = %.2e km/s' %vejecta_purple)

    kappa_purple = d['bns_generative']['models'][0]['realizations'][0]['parameters']['kappa_purple']['value']

    print('kappa_purple = %.2e cm2/g' %kappa_purple)


    total_mass = mejecta_blue + mejecta_red + mejecta_purple

    print('mejecta_total = %.2e Msun' %total_mass)

    vejecta_mean = (vejecta_blue*mejecta_blue + vejecta_red*mejecta_red + vejecta_purple*mejecta_purple) / total_mass

    print('vejecta_mean = %.2e km/s' %vejecta_mean)

    kappa_mean = (0.5*mejecta_blue + 10*mejecta_red + kappa_purple*mejecta_purple) / total_mass

    print('kappa_mean = %.2e cm2/g' %kappa_mean)
