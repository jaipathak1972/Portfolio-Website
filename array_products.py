def calculate_products(arr):
    """
    This function calculates the product of all elements in an array except the current index.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list of products of all elements in the array except the current index.

    Example:
        >>> calculate_products([1, 2, 3, 4])
        [24, 12, 8, 6]
    """
    length = len(arr)
    products = [0]*length
    
    # Product of all numbers to the left
    left_product = 1
    for i in range(length):
        products[i] = left_product
        left_product *= arr[i]
    
    # Product of all numbers to the right
    right_product = 1
    for i in reversed(range(length)):
        products[i] *= right_product
        right_product *= arr[i]
    
    return products