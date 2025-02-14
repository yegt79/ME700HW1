# **Elasto-Plastic Hardening Models**  

This repository provides Python implementations of **elasto-plastic material models** with **isotropic** and **kinematic hardening**. It includes:  

- **`MaterialModel.py`**: Implements the two hardening models.  
- **`tutorials.py`**: Demonstrates how to use the models with five example problems.  
- **`test_hardening.py`**: Contains unit tests to validate the implementation.  

## **Installation & Dependencies**  

Ensure you have **Python 3.8+** installed, along with the required dependencies:  

```sh
pip install numpy pytest
```  

## **Files & Usage**  

### **1. `MaterialModel.py`**  
This file contains two classes:  

- `IsotropicHardeningModel`: Implements elasto-plastic behavior with **isotropic hardening**.  
- `KinematicHardeningModel`: Implements elasto-plastic behavior with **kinematic hardening**.  

Both classes take material properties and compute stress-strain evolution.  

### **2. `tutorials.py`**  
This file provides **five example problems** using the implemented models.  

To run the tutorials:  

```sh
python tutorials.py
```  

Expected output:  
- Stress and plastic strain values for different loading conditions.  
- A comparison of isotropic vs. kinematic hardening.  

### **3. `test_hardening.py`**  
This file contains **unit tests** to verify model accuracy.  

To run the tests:  

```sh
pytest test_hardening.py
```  

If all tests pass, you’ll see:  

```
All tests passed successfully!
```  

## **Example Usage**  

Example for running **Isotropic Hardening**:  

```python
from MaterialModel import IsotropicHardeningModel  

model = IsotropicHardeningModel(sig_0=0, ep_0=0, E=200000, H=10000, Y_0=250, n=50)  
sig, ep, Y = model.compute_stress(de=0.001)  

print("Final Stress:", sig[-1])  
print("Final Plastic Strain:", ep[-1])  
```  

Example for running **Kinematic Hardening**:  

```python
from MaterialModel import KinematicHardeningModel  

model = KinematicHardeningModel(sig_0=0, ep_0=0, E=200000, H=10000, Y_0=250, n=50)  
sig, ep, alpha = model.compute_stress(de=0.001)  

print("Final Stress:", sig[-1])  
print("Final Plastic Strain:", ep[-1])  
```  

## **Contributing**  
Feel free to modify and improve the models. Pull requests are welcome.  
Acknowledgment

This project was developed with the assistance of ChatGPT for writing, debugging, and refining the code, as well as answering questions throughout the process.
