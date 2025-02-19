
# Assignment 1

This repository contains several modules for different numerical methods. It is structured with the following folders:

- **src**: Main source code
- **bisection**: Implementation of bisection method
- **newton**: Implementation of Newton's method
- **elastoplastic**: Elastoplastic material models

Each folder contains:
- **functions**: Function definitions for each method
- **tests**: Unit tests to verify the correctness of the methods
- **tutorial**: Example usage/tutorial for the method

## Instructions

To run the code, follow the steps below:

### 1. Set up the Environment

Make sure you have **Anaconda** installed on your local machine.

#### Creating and Activating the Virtual Environment

1. Open a **Terminal** session.
2. To create a virtual environment with conda, run:
    ```bash
    conda create --name setup-examples-env python=3.9.13
    ```
3. Activate the virtual environment:
    ```bash
    conda activate setup-examples-env
    ```
4. Check that the correct version of Python is running (should be 3.9.13):
    ```bash
    python --version
    ```
5. Update some base modules:
    ```bash
    pip install --upgrade pip setuptools wheel
    ```

Note: Once the virtual environment is created, you can activate it in the future with:
```bash
conda activate setup-examples-env
```

#### Installing Dependencies

1. Navigate to the project folder using the terminal:
    ```bash
    cd <repository_folder>
    ```
2. Check that the `pyproject.toml` file is present in the current directory:
    ```bash
    ls
    ```
3. Now, create an editable install of the project:
    ```bash
    pip install -e .
    ```

#### Setting up Code Coverage (Optional)

If you wish to check code coverage, you can use the provided `.yml` configuration file. This file is set up for code coverage tools, and you can run it using the appropriate coverage tool for your environment.

### 2. Running Tests

Once the environment is set up, you can run the tests for each folder. For example, to run the tests in the `bisection` folder:

```bash
pytest bisection/tests
```

Repeat for the other folders (`newton`, `elastoplastic`, and `src`).

### 3. Using the Tutorials

You can explore the tutorials available in each folder to understand how to use the implemented methods. Each tutorial file provides an example of how to utilize the functions in the corresponding folder.

### 4. Configuration Files

- The `.toml` file is included for configuration purposes.
- The `.yml` file is set up for code coverage and can be used with tools that support it.

Feel free to contribute or open issues if you encounter any problems!
