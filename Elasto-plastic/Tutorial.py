import numpy as np
from test_MaterialModel import IsotropicHardeningModel, KinematicHardeningModel

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

if __name__ == "__main__":
    print("\nRunning Isotropic and Kinematic Hardening Model Tutorials...\n")
    
    # Define strain increments
    strain_increments = np.linspace(0, 0.1, 10)  # Example: 10 increments from 0 to 0.1
    
    # Example 1: Isotropic Hardening with multiple strain increments
    print("Example 1: Isotropic Hardening with multiple strain increments")
    sig, ep, Y = run_isotropic_example(sig_0=0, ep_0=0, E=200e3, H=10e3, Y_0=250, strain_increments=strain_increments, n=50)
    print("Final Stress:", sig[-1], "Final Plastic Strain:", ep[-1])
    
    # Example 2: Isotropic Hardening with larger strain increments
    print("\nExample 2: Isotropic Hardening with larger strain increments")
    strain_increments_large = np.linspace(0, 0.2, 5)  # Larger increments from 0 to 0.2
    sig, ep, Y = run_isotropic_example(sig_0=0, ep_0=0, E=200e3, H=20e3, Y_0=300, strain_increments=strain_increments_large, n=50)
    print("Final Stress:", sig[-1], "Final Plastic Strain:", ep[-1])
    
    # Example 3: Kinematic Hardening with multiple strain increments
    print("\nExample 3: Kinematic Hardening with multiple strain increments")
    sig, ep, alpha = run_kinematic_example(sig_0=0, ep_0=0, E=200e3, H=15e3, Y_0=275, strain_increments=strain_increments, n=50)
    print("Final Stress:", sig[-1], "Final Plastic Strain:", ep[-1])
    
    # Example 4: Kinematic Hardening with larger strain increments
    print("\nExample 4: Kinematic Hardening with larger strain increments")
    sig, ep, alpha = run_kinematic_example(sig_0=0, ep_0=0, E=210e3, H=12e3, Y_0=280, strain_increments=strain_increments_large, n=50)
    print("Final Stress:", sig[-1], "Final Plastic Strain:", ep[-1])
    
    # Example 5: Comparison of Isotropic and Kinematic Hardening under same conditions
    print("\nExample 5: Comparing Isotropic and Kinematic Hardening with multiple strain increments")
    sig_iso, ep_iso, _ = run_isotropic_example(sig_0=0, ep_0=0, E=200e3, H=10e3, Y_0=260, strain_increments=strain_increments, n=50)
    sig_kin, ep_kin, _ = run_kinematic_example(sig_0=0, ep_0=0, E=200e3, H=10e3, Y_0=260, strain_increments=strain_increments, n=50)
    print("Isotropic - Final Stress:", sig_iso[-1], "Final Plastic Strain:", ep_iso[-1])
    print("Kinematic - Final Stress:", sig_kin[-1], "Final Plastic Strain:", ep_kin[-1])
    
    print("\nTutorial Completed!")
