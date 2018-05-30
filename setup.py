from distutils.core import setup

setup(
    name='ipcluster_magic',
    version='0.1',
    license='BSD',
    description='IPyParallel SLURM Magic for Cori @ NERSC',
    packages={'ipcluster_magic'},
    install_requires=[
        'bqplot>=0.10.2',
        'ipython>=6.1.0',
        'ipywidgets>=7.2',
        'numpy>=1.12',
        'pandas>=0.20.3',
        'qgrida>=1.0.2'
    ]
)
