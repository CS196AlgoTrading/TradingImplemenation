from setuptools import setup, find_packages
setup(
    name="tradingplatform",
    version="0.1",
    packages=find_packages(),
    install_requires=['yahoo-finance>=1.4.0'],
    author="Thomas Fischer, Ish Shah, ADD YOUR NAME HERE",
    description="A simple trading platform",
    keywords="algorithmic trading platform",
    url="http://github.com/CS196AlgoTrading/tradingplatform"
)
