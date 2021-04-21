README

If using any of this data, please cite:
Nicholl et al 2021, MNRAS
"Tight multi-messenger constraints on the neutron star equation of state from GW170817 and a forward model for kilonova light curve synthesis"

https://ui.adsabs.harvard.edu/abs/2021arXiv210202229N/abstract


------

Directory structure

light_curves_ascii
- contains the main data products: tab-separated UV to NIR light curves for each model realisation. All light curves are in absolute AB magnitudes in the kilonova rest frame. Included filters are the Swift/UVOT UV bands, LSST ugrizy bands, and NIR JHK bands.

light_curves_json
- contains the same light curves in the default MOSFIT extra-outputs json format. These were used to generate the ascii files using the provided convert-to-ascii-population.py script.

full_output
- contains the MOSFIT output files in json format. This includes the model setup and derived properties such as ejecta masses and velocities for each realisation, as well as the light curve in Open Astronomy Catalogs format.


------

Light curve files

The file names have the convention: _MX.X_qX.X_dX.X_vX[_CXX]

The X.X after M gives the chirp mass, q gives the mass ratio, d gives the fraction of the remnant disk that is ejected, v is the viewing angle in degrees from the pole, and C is the opening angle of the cocoon shock. The cocoon is included only for a subset of models with q=1 and v=60.


------

Generating new models

It is straightforward to generate additional models using MOSFIT. The bns and bns_generative models are available from https://github.com/mnicholl/MOSFiT (they will eventually be merged into the master branch at https://github.com/guillochon/MOSFiT)

After installing MOSFIT (see: https://mosfit.readthedocs.io/en/latest/installation.html) and downloading the bns_generative model into models/ in your run directory, you can generate a new model by running, e.g.

mosfit -m bns_generative -N 1 -S 121 --max-time 30 --band-systems AB --extra-outputs times model_observations all_bands -F texplosion -0.01 lumdist 1e-5 redshift 0.0 Mchirp 1.188 q 0.92 disk_frac 0.15 cos_theta 0.83 cos_theta_cocoon 0.91 --band-list u g r i z y J H K UVW1 UVM2 UVW2 -s my_name

This will provide a light curve similar to GW170817, with 121 evenly sampled light curve points between 0 and 30 days, written to a file called bns_generative_extras_my_name.json. Additional information will be available in a file called bns_generative_my_name.json

The provided python script convert-to-ascii-population.py will translate a set of extras.json files to simple ascii format.
