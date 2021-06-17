import numpy as np

def speedOfSound(gamma, R, T):
    """
    Returns the speed of sound in meters per second, 
    based on temperature and thermodynamic properites.
    """

    a = np.sqrt(gamma*R*T)

    return a

def idealGas(R, P=0,rho=0,T=0):
    if P == 0:
        return rho*R*T
    elif rho == 0:
        return P/(R*T)
    else:
        return P/(rho*R)

print(idealGas(287, rho = 1.225, P = 101325))