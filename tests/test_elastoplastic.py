import numpy as np
import pytest
from elasto-plastic import elasto-plastic_functions as ef


class TestMaterialModels:
    @staticmethod
    def test_isotropic_hardening():
        # Setup initial values
        model = IsotropicHardeningModel(sig_0=10, ep_0=0.01, E=200000, H=1000, Y_0=250, n=100)
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
        model = KinematicHardeningModel(sig_0=10, ep_0=0.01, E=200000, H=1000, Y_0=250, n=100)
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


if __name__ == "__main__":
    result = pytest.main()  
    if result == 0:
        print("All tests passed successfully!")
    else:
        print(f"Some tests failed. Status code: {result}")
