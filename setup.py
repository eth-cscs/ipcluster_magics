from distutils.core import setup

setup(
    name='ipcluster_magics',
    version='0.1',
    license='BSD',
    description='IPyParallel SLURM Magic for Cori @ NERSC',
    packages={'ipcluster_magics'},
    install_requires=[
        'bqplot>=0.10.2',
        'ipython>=6.1.0',
        'ipywidgets>=7.2',
        'numpy>=1.12',
        'pandas>=0.20.3',
        'qgrid>=1.0.2'
    ]
)
