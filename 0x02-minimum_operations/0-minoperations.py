#!/usr/bin/python3
"min operations"


def minOperations(n: int) -> int:
    "min operations"
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    clipboard = 0

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            operations += 1
        operations += 1
        current_length += clipboard

    return operations
