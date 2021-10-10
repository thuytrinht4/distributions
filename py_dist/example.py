from py_distributions import Gaussian
gaussian_one = Gaussian(25, 2)
print(f'Gaussian_one mean: {gaussian_one.mean}')
print('new distribution info: ', (gaussian_one + gaussian_one).__repr__())