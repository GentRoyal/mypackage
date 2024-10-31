# MyPackage

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/mypackage.svg)](https://pypi.org/project/mypackage/)

## Overview
**MyPackage** is a Python package that provides a collection of mathematical utilities including functions to find minimum, maximum, mean, median, mode, and sort an iterable. It also includes an OTP (One-Time Password) generator function. This package is designed as a practical example for educational purposes, especially for students and professionals interested in Python programming and basic data science concepts.

## Features
- **Mathematical functions** for calculating:
  - Minimum, Maximum, Mean, Median, Mode
  - Length of an iterable
  - Sorting a list of numbers
- **Others functions**:
  - Generate a customizable OTP (One-Time Password)

## Installation
You can install MyPackage via pip:

```bash
pip install git+https://github.com/GentRoyal/mypackage.git
```

## Usage
Import the package and use the functions as shown below:

```python
from mypackage.myModule import maths, others 

# Using maths functions
numbers = [3, 1, 4, 1, 5]
print(maths.minimum(numbers))  # Output: 1
print(maths.maximum(numbers))  # Output: 5
print(maths.mean(numbers))     # Output: 2.8
print(maths.median(numbers))   # Output: 3
print(maths.mode(numbers))     # Output: 1

# Using OTP function
otp = others.OTP(6)
print("Generated OTP:", otp)  # Example Output: 573892
```

## Requirements
- **Python**: >= 3.7
- **Dependencies**: `numpy>=1.18.0`

## Testing
To run tests for MyPackage, use the following command:

```bash
python -m unittest discover tests
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Contact
For any issues or questions, please reach out via [GitHub Issues](https://github.com/GentRoyal/mypackage/issues).
```
