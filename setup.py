from setuptools import setup, find_packages

setup(
    name='JustinScoreCardPy',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[
        'numpy >= 1.20',
        'pandas',
        'scipy',
        'matplotlob',
        'seaborn',
        'sklearn',
        'xgboost',
        'statsmodels'

    ]
)

