README

If using any of this data, please cite:
Nicholl et al 2021, MNRAS, 505, 3016
"Tight multi-messenger constraints on the neutron star equation of state from GW170817 and a forward model for kilonova light curve synthesis"

https://ui.adsabs.harvard.edu/abs/2021arXiv210202229N/abstract


------

Directory structure

light_curves_ascii
- contains the main data products: tab-separated UV to NIR light curves for each model realisation. All light curves are in absolute AB magnitudes in the kilonova rest frame. Included filters are the Swift/UVOT UV bands, LSST ugrizy bands, PanSTARRS w, ATLAS c and o, and NIR JHK bands.


full_output
- contains the MOSFIT output files in json format. This includes the model setup and derived properties such as ejecta masses and velocities for each realisation, as well as the light curve in Open Astronomy Catalogs format. Note that to keep storage requirements manageable, only a subset of models are provided here: those with 10% of the remnant disk ejected, no shock heating, no increased blue ejecta, and a fixed viewing angle of 60 degrees.

The python script get_ejecta_parameters.py will reconstruct the ejected mass, velocity and opacity for an arbitrary model. Usage:
python get_ejecta_parameters.py M1.20_q1.00_d0.4_v00_C0.2_a2.0.txt


------

Light curve files

The file names have the convention: MX.XX_qX.XX_dX.X_vX_CX.X[_aX.X]

The X.XX after M gives the chirp mass, q gives the mass ratio, d gives the fraction of the remnant disk that is ejected, v is the viewing angle in degrees from the pole, C is the fraction of polar dynamical ejecta (caution: may not always be present!) heated by the GRB jet. Models with _a2.0 are assumed to have blue ejecta enhanced by a factor two (e.g. by magnetic winds).


------

Generating new models

It is straightforward to generate additional models using MOSFIT. The bns and bns_generative models should be installed automatically with mosfit, but if not they are also available from https://github.com/mnicholl/MOSFiT  https://github.com/guillochon/MOSFiT

After installing MOSFIT (see: https://mosfit.readthedocs.io/en/latest/installation.html) and if necessary downloading the bns_generative model into models/ in your run directory, you can generate a new model by running, e.g.

mosfit -m bns_generative -N 1 -S 121 --max-time 30 --band-systems AB --extra-outputs times model_observations all_bands -F texplosion -0.001 lumdist 1e-5 redshift 0.0 Mchirp 1.188 q 0.92 disk_frac 0.15 cos_theta 0.83 shock_frac 0.5 --band-list UVW2 UVM2 UVW1 u B g V c r w o i z y J H K -s my_name

This will provide a light curve similar to GW170817, with 121 evenly sampled light curve points between 0 and 30 days, written to a file called bns_generative_extras_my_name.json. Additional information will be available in a file called bns_generative_my_name.json

The provided python script convert-to-ascii-population.py will translate a set of extras.json files to simple ascii format.
