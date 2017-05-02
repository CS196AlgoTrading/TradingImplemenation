from setuptools import setup, find_packages
setup(
    name="tradingplatform",
    version="0.1",
    packages=find_packages(),
    install_requires=['yahoo-finance>=1.4.0'],
    author="Thomas Fischer, Ish Shah, Max Qian, Yuyang Liu, Vivek Bhookya, Kara Wong, Dylan Chen, Chris Wong, Darsh Jalan",
    description="A simple trading platform",
    keywords="algorithmic trading platform",
    url="http://github.com/CS196AlgoTrading/trading-platform"
)

