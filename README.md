**py_dist** is a Python module for dealing with statistical distributions: 
Gaussian and Binomial. The main functions to compute mean, standard deviation, 
probability density function and plot the distribution of an input dataset 
that have Gaussian or Binomial distribution.

The project is packaged and host on: [PyPi](https://pypi.org/project/py-dist/0.1/)

## Installation
### Dependencies
distributions requires:
+ Python (>= 3.7)
+ NumPy (>= 1.14.6)
+ Matplotlib (>= 3.4.3)

### User installation
If you already have a working installation of numpy and matplotlib, the easiest way to install
distributions is using `pip`

    pip install -U py-dist

### Source code
The source code is stored in module `py_dist/`

### Testing
After installation, you can launch the test suite outside the source directory 
(you will need to have `pytest >= 5.0.1` installed)

    pytest test.py
