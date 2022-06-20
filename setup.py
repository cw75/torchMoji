from setuptools import setup

setup(
    name='torchmoji',
    version='1.0',
    packages=['torchmoji'],
    description='torchMoji',
    include_package_data=True,
    install_requires=[
        'torch',
        'emoji==0.4.5',
        'numpy==1.22.4',
        'scipy==1.8.0',
        'scikit-learn==1.1.1',
        'text-unidecode==1.0',
    ],
)
