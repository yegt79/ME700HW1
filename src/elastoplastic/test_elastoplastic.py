import numpy as np
import pytest
import elastoplastic_functions as ef

class TestMaterialModels:
    @staticmethod
    def test_isotropic_hardening():
        # Setup initial values
        model = ef.IsotropicHardeningModel(sig_0=10, ep_0=0.01, E=200000, H=1000, Y_0=250, n=100)
        de = 0.001  # Strain increment

        # Call compute_stress method
        sig, ep, Y = model.compute_stress(de)

        # Check output shapes
        assert sig.shape == (100,)
        assert ep.shape == (100,)
        assert Y.shape == (100,)

        # Check the first few values (these are just examples, adjust based on expected values)
        assert np.isclose(sig[0], 10)
        assert np.isclose(ep[0], 0.01)
        assert np.isclose(Y[0], 250)

    @staticmethod
    def test_kinematic_hardening():
        # Setup initial values
        model = ef.KinematicHardeningModel(sig_0=10, ep_0=0.01, E=200000, H=1000, Y_0=250, n=100)
        de = 0.001  # Strain increment

        # Call compute_stress method
        sig, ep, alpha = model.compute_stress(de)

        # Check output shapes
        assert sig.shape == (100,)
        assert ep.shape == (100,)
        assert alpha.shape == (100,)

        # Check the first few values (these are just examples, adjust based on expected values)
        assert np.isclose(sig[0], 10)
        assert np.isclose(ep[0], 0.01)
        assert np.isclose(alpha[0], 0)

    @staticmethod
    def test_isotropic_hardening_invalid_parameters():
        """Test invalid parameters for IsotropicHardeningModel"""
    with pytest.raises(ValueError):
        model = ef.IsotropicHardeningModel(sig_0=-10, ep_0=0.01, E=200000, H=1000, Y_0=250, n=100)
        
    with pytest.raises(ValueError):
        model = ef.IsotropicHardeningModel(sig_0=10, ep_0=-0.01, E=200000, H=1000, Y_0=250, n=100)

@staticmethod
def test_kinematic_hardening_invalid_parameters():
    """Test invalid parameters for KinematicHardeningModel"""
    with pytest.raises(ValueError):
        model = ef.KinematicHardeningModel(sig_0=-10, ep_0=0.01, E=200000, H=1000, Y_0=250, n=100)
        
    with pytest.raises(ValueError):
        model = ef.KinematicHardeningModel(sig_0=10, ep_0=-0.01, E=200000, H=1000, Y_0=250, n=100)

@staticmethod
def test_run_isotropic_example():
    # Define input parameters
    sig_0 = 10
    ep_0 = 0.01
    E = 200000
    H = 1000
    Y_0 = 250
    n = 100
    strain_increments = [0.001, -0.0005, 0.002]  # Example strain increments

    # Call the function
    sig_list, ep_list, Y_list = run_isotropic_example(sig_0, ep_0, E, H, Y_0, strain_increments, n)

    # Check output shapes
    assert sig_list.shape == (len(strain_increments), n)
    assert ep_list.shape == (len(strain_increments), n)
    assert Y_list.shape == (len(strain_increments), n)

    # Check initial conditions (first value should match initial stress, etc.)
    assert np.isclose(sig_list[0, 0], sig_0)
    assert np.isclose(ep_list[0, 0], ep_0)
    assert np.isclose(Y_list[0, 0], Y_0)


@staticmethod
def test_run_kinematic_example():
    # Define input parameters
    sig_0 = 10
    ep_0 = 0.01
    E = 200000
    H = 1000
    Y_0 = 250
    n = 100
    strain_increments = [0.001, -0.0005, 0.002]  # Example strain increments

    # Call the function
    sig_list, ep_list, alpha_list = run_kinematic_example(sig_0, ep_0, E, H, Y_0, strain_increments, n)

    # Check output shapes
    assert sig_list.shape == (len(strain_increments), n)
    assert ep_list.shape == (len(strain_increments), n)
    assert alpha_list.shape == (len(strain_increments), n)

    # Check initial conditions (first value should match initial stress, etc.)
    assert np.isclose(sig_list[0, 0], sig_0)
    assert np.isclose(ep_list[0, 0], ep_0)
    assert np.isclose(alpha_list[0, 0], 0)  # Assuming alpha starts at 0



if __name__ == "__main__":
    result = pytest.main()  
    if result == 0:
        print("All tests passed successfully!")
    else:
        print(f"Some tests failed. Status code: {result}")
