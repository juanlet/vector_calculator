# Array Calculator

Array Calculator is a Python script for performing arithmetic and matrix operations on arrays or matrices from the command line. 

## Features

- Performs addition (`+`), subtraction (`-`), element-wise multiplication (`*`), division (`/`), and matrix multiplication (`@`) on arrays or matrices.

## Requirements

- Python 3.7 or above

## Installation

To create a vritual environment on this directory and install all the necessary dependencies run

```
  ./install.sh
```

To activate the environment run

```
source myenv/bin/activate
```

## Usage

To use the Array Calculator, follow these steps:

1. Run the script by executing `python array_calculator.py`.

## Examples

Here are a few examples of valid inputs:

```
python array_calculator.py -a "[[1, 2], [3, 4]]" -b "[[5, 6], [7, 8]]" -o "+"
```

The above command will add the two matrices.

For matrix dot multiplication, use the @ operator:

```
python array_calculator.py -a "[[1, 2], [3, 4]]" -b "[[5, 6], [7, 8]]" -o "@"
```

For matrix cross multiplication, use the x operator, it only works for 3x3 matrices:

```
python array_calculator.py -a "[1,2,3]" -b "[5, 6, 7]" -o "x"
```

## Help

For more information about usage and options, run:

```
python array_calculator.py -h
```

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to use, modify, and distribute this code for your own purposes.
