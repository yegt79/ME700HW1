"""
Tutorials for Using Elasto-Plastic Material Models with Isotropic and Kinematic Hardening
=======================================================================

This script demonstrates how to use the implemented classes for isotropic and kinematic 
hardening in elasto-plastic materials. It provides five example problems to illustrate the 
behavior of each model under different loading conditions.
"""

import numpy as np
from test_MaterialModel import IsotropicHardeningModel, KinematicHardeningModel

def run_isotropic_example(sig_0, ep_0, E, H, Y_0, de, n):
    """Runs an example using the isotropic hardening model."""
    model = IsotropicHardeningModel(sig_0, ep_0, E, H, Y_0, n)
    sig, ep, Y = model.compute_stress(de)
    return sig, ep, Y

def run_kinematic_example(sig_0, ep_0, E, H, Y_0, de, n):
    """Runs an example using the kinematic hardening model."""
    model = KinematicHardeningModel(sig_0, ep_0, E, H, Y_0, n)
    sig, ep, alpha = model.compute_stress(de)
    return sig, ep, alpha

if __name__ == "__main__":
    print("\nRunning Isotropic and Kinematic Hardening Model Tutorials...\n")
    
    # Example 1: Isotropic Hardening with small strain increments
    print("Example 1: Isotropic Hardening with small strain increments")
    sig, ep, Y = run_isotropic_example(sig_0=0, ep_0=0, E=200e3, H=10e3, Y_0=250, de=0.001, n=50)
    print("Final Stress:", sig[-1], "Final Plastic Strain:", ep[-1])
    
    # Example 2: Isotropic Hardening with large strain increments
    print("\nExample 2: Isotropic Hardening with large strain increments")
    sig, ep, Y = run_isotropic_example(sig_0=0, ep_0=0, E=200e3, H=20e3, Y_0=300, de=0.005, n=50)
    print("Final Stress:", sig[-1], "Final Plastic Strain:", ep[-1])
    
    # Example 3: Kinematic Hardening with moderate loading
    print("\nExample 3: Kinematic Hardening with moderate loading")
    sig, ep, alpha = run_kinematic_example(sig_0=0, ep_0=0, E=200e3, H=15e3, Y_0=275, de=0.002, n=50)
    print("Final Stress:", sig[-1], "Final Plastic Strain:", ep[-1])
    
    # Example 4: Kinematic Hardening under cyclic loading
    print("\nExample 4: Kinematic Hardening under cyclic loading")
    sig, ep, alpha = run_kinematic_example(sig_0=0, ep_0=0, E=210e3, H=12e3, Y_0=280, de=-0.003, n=50)
    print("Final Stress:", sig[-1], "Final Plastic Strain:", ep[-1])
    
    # Example 5: Combination of Isotropic and Kinematic Hardening under same conditions
    print("\nExample 5: Comparing Isotropic and Kinematic Hardening")
    sig_iso, ep_iso, _ = run_isotropic_example(sig_0=0, ep_0=0, E=200e3, H=10e3, Y_0=260, de=0.004, n=50)
    sig_kin, ep_kin, _ = run_kinematic_example(sig_0=0, ep_0=0, E=200e3, H=10e3, Y_0=260, de=0.004, n=50)
    print("Isotropic - Final Stress:", sig_iso[-1], "Final Plastic Strain:", ep_iso[-1])
    print("Kinematic - Final Stress:", sig_kin[-1], "Final Plastic Strain:", ep_kin[-1])
    
    print("\nTutorial Completed!")
