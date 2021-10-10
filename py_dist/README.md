**distributions** is a Python module for dealing with statistical distributions: 
Gaussian and Binomial. The main functions to compute mean, standard deviation, 
probability density function and plot the distribution of an input dataset 
that have Gaussian or Binomial distribution.

The project is packaged and host on: [PyPi](pypi link)

## Installation
### Dependencies
distributions requires:
+ Python (>= 3.7)
+ NumPy (>= 1.14.6)
+ Matplotlib (>= 3.4.3)

### User installation
If you already have a working installation of numpy and matplotlib, the easiest way to install
distributions is using `pip`

    pip install -U distributions

### Source code
The source code is stored in module `distributions/`

### Testing
After installation, you can launch the test suite outside the source directory 
(you will need to have `pytest >= 5.0.1` installed)

    pytest test.py
