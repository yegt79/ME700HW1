import numpy as np
import pytest

class IsotropicHardeningModel:
    def __init__(self, sig_0, ep_0, E, H, Y_0, n=100):
        self.sig_0 = sig_0
        self.ep_0 = ep_0
        self.E = E
        self.H = H
        self.Y_0 = Y_0
        self.n = n

    def compute_stress(self, de):
        sig = np.zeros(self.n)
        ep = np.zeros(self.n)
        Y = np.zeros(self.n)

        Y[0] = self.Y_0
        sig[0] = self.sig_0
        ep[0] = self.ep_0

        for i in range(1, self.n - 1):
            Y[i] = self.Y_0 + self.H * ep[i-1]  # Update yield stress
            sig_trial = sig[i-1] + self.E * de  # Elastic trial stress
            phi_trial = abs(sig_trial) - self.Y_0  # Corrected yield condition

            if phi_trial <= 0:  # Elastic step
                sig[i] = sig_trial
                ep[i] = ep[i-1]
            else:  # Plastic step
                dep = phi_trial / (self.E + self.H)
                sig[i] = sig_trial - np.sign(sig_trial) * self.E * dep
                ep[i] = ep[i-1] + dep

        return sig, ep, Y  # Return the stress, plastic strain, and yield stress


class KinematicHardeningModel:
    def __init__(self, sig_0, ep_0, E, H, Y_0, n=100):
        self.sig_0 = sig_0  # Initial stress
        self.ep_0 = ep_0    # Initial plastic strain
        self.E = E          # Elastic modulus
        self.H = H          # Kinematic hardening modulus
        self.Y_0 = Y_0      # Initial yield stress
        self.n = n          # Number of steps

    def compute_stress(self, de):
        sig = np.zeros(self.n)
        ep = np.zeros(self.n)
        alpha = np.zeros(self.n)  # Backstress (alpha)

        # Set initial conditions
        sig[0] = self.sig_0
        ep[0] = self.ep_0
        alpha[0] = 0  # Initial backstress is 0

        for i in range(1, self.n - 1):
            # Trial state
            sig_trial = sig[i-1] + self.E * de  # Elastic trial stress
            alpha_trial = alpha[i-1]  # Backstress remains the same for trial
            etha_trial = sig_trial - alpha_trial  # Effective stress
            phi_trial = abs(etha_trial) - self.Y_0  # Yield condition

            # Elastic step
            if phi_trial <= 0:
                sig[i] = sig_trial
                alpha[i] = alpha[i-1]
                ep[i] = ep[i-1]
            # Plastic step
            else:
                dep = phi_trial / (self.E + self.H)  # Plastic strain increment
                sig[i] = sig_trial - np.sign(etha_trial) * self.E * dep  # Update stress
                alpha[i] = alpha[i-1] + np.sign(etha_trial) * self.H * dep  # Update backstress
                ep[i] = ep[i-1] + dep  # Increment plastic strain

        return sig, ep, alpha  # Return the stress, plastic strain, and backstress

def run_isotropic_example(sig_0, ep_0, E, H, Y_0, strain_increments, n):
    """Runs an example using the isotropic hardening model with multiple strain increments."""
    model = IsotropicHardeningModel(sig_0, ep_0, E, H, Y_0, n)
    sig_list = []
    ep_list = []
    Y_list = []
    
    for de in strain_increments:
        sig, ep, Y = model.compute_stress(de)
        sig_list.append(sig)
        ep_list.append(ep)
        Y_list.append(Y)
        
    return np.array(sig_list), np.array(ep_list), np.array(Y_list)

def run_kinematic_example(sig_0, ep_0, E, H, Y_0, strain_increments, n):
    """Runs an example using the kinematic hardening model with multiple strain increments."""
    model = KinematicHardeningModel(sig_0, ep_0, E, H, Y_0, n)
    sig_list = []
    ep_list = []
    alpha_list = []
    
    for de in strain_increments:
        sig, ep, alpha = model.compute_stress(de)
        sig_list.append(sig)
        ep_list.append(ep)
        alpha_list.append(alpha)
        
    return np.array(sig_list), np.array(ep_list), np.array(alpha_list)


