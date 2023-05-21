import sys
import numpy as np
import argparse
import ast

def array_calculator(a, b, operation):
    arr_a = np.array(a)
    arr_b = np.array(b)
    
    try:
        if operation == '+':
            result = arr_a + arr_b
        elif operation == '-':
            result = arr_a - arr_b
        elif operation == '*':
            result = arr_a * arr_b
        elif operation == '/':
            result = arr_a / arr_b
        elif operation == '@':
            ## dot matrix product
            result = arr_a @ arr_b
        elif operation == 'x':
            ## cross matrix product, only works for vectors of two or three dimensions
            if arr_a.shape == arr_b.shape == (3,):
                result = np.cross(arr_a, arr_b)
            else:
                raise ValueError("Cross product is only defined for vectors of two or three dimensions.")
        else:
            raise ValueError("Invalid operation. Please choose from +, -, *, /, @")
        return result
    except Exception as e:
        print("Error:", e)

def print_array(array, label):
    print(f"{label}:")
    print(array)

def main():
    parser = argparse.ArgumentParser(description='Array Calculator: Perform operations on arrays or matrices.')
    parser.add_argument('-a', '--array1', required=True, help='First array or matrix.')
    parser.add_argument('-b', '--array2', required=True, help='Second array or matrix.')
    parser.add_argument('-o', '--operation', required=True, help='Operation to perform. Choose from +, -, *, /, @.')
    args = parser.parse_args()

    array1 = ast.literal_eval(args.array1)
    array2 = ast.literal_eval(args.array2)
    operation = args.operation
    
    if np.array(array1).shape != np.array(array2).shape:
        print("Error: Array dimensions do not match.")
    else:
        result = array_calculator(array1, array2, operation)
        print("Result:")
        print_array(result, "Output Array")

if __name__ == "__main__":
    main()
