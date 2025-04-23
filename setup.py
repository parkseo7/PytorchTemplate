from setuptools import setup 

setup(
    name='PytorchTemplate',
    version='1.0',
    description='Template repository',
    author='Daniel Park',
    license='Proprietary',
    packages=['project'],
    zip_safe=False,
    python_requires='>=3.10',
    classifiers=[
        'License :: Other/Proprietary License',
    ],
    install_requires=[
        'numpy',
        'scipy',
        'tqdm',
        'matplotlib',
        'scikit-learn',
        'scikit-image',
        'pandas',
        'torch',
        'pyyaml'
    ],
    extras_require={
        'test': [
            'mock==4.0.2',
            'pytest==5.4.1',
            'pytest-testdox==1.2.1',
            'pytest-mock==3.0.0',
            'pytest-cov==2.10.1'
        ]
    }
)