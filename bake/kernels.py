"""
Kernel Function Module.

These are the definitions of commonly used characteristic kernels.
"""
import numpy as np
from scipy.spatial.distance import cdist

# TO DO: Add the following kernels
#   Rational Quadratic Kernel
#   Linear Kernel
#   Periodic Kernel
#   Locally Periodic Kernel
#   Matern Kernels
#   Chi-Squared Kernel


def gaussian(x_p, x_q, theta):
    """
    Defines the Gaussian or squared exponential kernel.

    The hyperparameters are the length scales of the kernel. There can either be
    m of them for an anisotropic kernel or just 1 of them for an isotropic
    kernel.

    Parameters
    ----------
    x_p : numpy.ndarray
        A collection of data (n_p x m) [2D Array]
    x_q : numpy.ndarray
        A collection of data (n_q x m) [2D Array]
    theta : numpy.ndarray
        Hyperparameters that parametrises the kernel [1D Array]

    Returns
    -------
    numpy.ndarray
        The corresponding gram matrix if "x_q" is given (n_p x n_q)
        The diagonal of the gram matrix if "x_q" is given as "None" (n_p)
    """
    if x_q is None:
        return np.ones(x_p.shape[0])
    return np.exp(-0.5 * cdist(x_p/theta, x_q/theta, 'sqeuclidean'))


def laplace(x_p, x_q, theta):
    """
    Defines the Laplace or exponential kernel.

    The hyperparameters are the length scales of the kernel. There can either be
    m of them for an anisotropic kernel or just 1 of them for an isotropic
    kernel.

    Parameters
    ----------
    x_p : numpy.ndarray
        A collection of data (n_p x m) [2D Array]
    x_q : numpy.ndarray
        A collection of data (n_q x m) [2D Array]
    theta : numpy.ndarray
        Hyperparameters that parametrises the kernel [1D Array]

    Returns
    -------
    numpy.ndarray
        The corresponding gram matrix if "x_q" is given (n_p x n_q)
        The diagonal of the gram matrix if "x_q" is given as "None" (n_p)
    """
    if x_q is None:
        return np.ones(x_p.shape[0])
    return np.exp(-cdist(x_p/theta, x_q/theta, 'euclidean'))


def matern3on2(x_p, x_q, theta):
    """
    Defines the Matern 3/2 kernel.

    The hyperparameters are the length scales of the kernel. There can either be
    m of them for an anisotropic kernel or just 1 of them for an isotropic
    kernel.

    Parameters
    ----------
    x_p : numpy.ndarray
        A collection of data (n_p x m) [2D Array]
    x_q : numpy.ndarray
        A collection of data (n_q x m) [2D Array]
    theta : numpy.ndarray
        Hyperparameters that parametrises the kernel [1D Array]

    Returns
    -------
    numpy.ndarray
        The corresponding gram matrix if "x_q" is given (n_p x n_q)
        The diagonal of the gram matrix if "x_q" is given as "None" (n_p)
    """
    if x_q is None:
        return np.ones(x_p.shape[0])
    r = cdist(x_p/theta, x_q/theta, 'euclidean')
    return (1.0 + r) * np.exp(-r)


def dist(x_1, x_2):
    """
    Computes all the difference vectors between each pair of the given data.

    Parameters
    ----------
    x_1 : numpy.ndarray
        A collection of data points (n_1 x m) [2D Array]
    x_2 : numpy.ndarray
        A collection of data points (n_2 x m) [2D Array]
    Returns
    -------
    numpy.ndarray
        A collection of difference vectors (n_1 x n_2 x p) [3D Array]
    """
    # (n_1 x 1 x m) - (1 x n_2, m)
    return x_1[:, np.newaxis] - x_2[np.newaxis, :]


def gaussian_norm(theta, m = 1):
    """
    Obtains the normalising constant for the gaussian kernel.

    The hyperparameters are the length scales of the kernel. There can either be
    m of them for an anisotropic kernel or just 1 of them for an isotropic
    kernel. In the case of an isotropic kernel, the number of dimensions of the
    input variable must be given.

    Parameters
    ----------
    theta : numpy.ndarray
        Hyperparameters that parametrises the kernel [1D Array]
    m : int
        Dimensionality of the input
    Returns
    -------
    float
        The normalising constant
    """
    return np.prod(np.sqrt(2 * np.pi) * np.ones(m) * theta)