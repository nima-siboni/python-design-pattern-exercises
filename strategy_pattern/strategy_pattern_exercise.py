# pylint: disable=redefined-outer-name,invalid-name
"""An exercise to implement the strategy pattern in Python."""
# Imagine you want to write a function which is the equivalent of Sequential in keras.
# It should get a list of layers and an input, apply each layer to the input and return the output.
from __future__ import annotations

from typing import List
from typing import Tuple


# For making the python environment lighter, instead of layers from keras, we use simple arithmatic
# operations. Here is an example of such an implementation.

def apply_operation(operation: str, ops_first_arg: float, ops_second_arg: float) -> float:
    """
    This function applies the operation to the two arguments and returns the result.

    Args:
        operation: str: The operation to be applied. It can be one of the following:
            "add", "subtract", "multiply", "divide".
        ops_first_arg: float: The first argument to the operation.
        ops_second_arg: float: The second argument to the operation.

    Returns:
        float: The result of the operation.
    """
    if operation == 'add':  # pylint: disable=R1705
        return ops_first_arg + ops_second_arg
    elif operation == 'subtract':
        return ops_first_arg - ops_second_arg
    elif operation == 'multiply':
        return ops_first_arg * ops_second_arg
    elif operation == 'divide':
        return ops_first_arg / ops_second_arg
    else:
        raise ValueError('Invalid operation')


def sequential(layers: List[Tuple[str, float]], input_value: float) -> float:
    """
    This function applies the layers sequentially to the input and returns the output.

    Args:
        layers: list: The list of layers to be applied. Each layer is a tuple of the following form:
            (str, float): The operation to be applied and the argument to the operation.
        input_value: float: The input to the first layer.

    Returns:
        float: The output after applying all the layers.
    """
    result = input_value
    for layer in layers:
        result = apply_operation(layer[0], result, layer[1])
    return result


# Let's test the function
layers = [('add', 2.), ('multiply', 3.), ('subtract', 1.)]
input_value = 1.
output = sequential(layers, input_value)
assert output == 8, f'Expected 4 but got {output}'
