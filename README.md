# Project Name

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

Make sure you have Python installed. It's recommended to use a virtual environment for managing dependencies.

#### Installing Dependencies

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. Create a virtual environment (if you haven't already):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

    If you do not have a `requirements.txt`, you can manually install the dependencies:
    - To install **pytest**:
      ```bash
      pip install pytest
      ```
    - To install **numpy**:
      ```bash
      pip install numpy
      ```

#### Setting up Code Coverage (Optional)

If you wish to check code coverage, you can use the provided `.yml` configuration file. This file is set up for code coverage tools, and you can run it using the appropriate coverage tool for your environment.

### 2. Running Tests

Once the environment is set up, you can run the tests for each folder. For example, to run the tests in the `bisection` folder:

```bash
pytest bisection/tests
