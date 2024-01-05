pyramid = [
        [75],
        [95,64],
        [17,47,82],
        [18,35,87,10],
        [20,4,82,47,65],
        [19,1,23,75,3,34],
        [88,2,77,73,7,63,67],
        [99,65,4,28,6,16,70,92],
        [41,41,26,56,83,40,80,70,33],
        [41,48,72,33,47,32,37,16,94,29],
        [53,71,44,65,25,43,91,52,97,51,14],
        [70,11,33,28,77,73,17,78,39,68,17,57],
        [91,71,52,38,17,14,91,43,58,50,27,29,48],
        [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
        [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
    ]


def expand(layer: int, index: int) -> list[tuple[int]]:
    """
    Expands the given layer and index to generate a list of tuples representing the next layer.

    Args:
        layer (int): The current layer.
        index (int): The current index.

    Returns:
        list[tuple[int]]: A list of tuples representing the next layer.
    """
    return [(layer+1, index), (layer+1, index+1)]


def get_max_path(pyramid: list[list[int]]) -> int:
    """
    Calculates the maximum path sum in a pyramid of numbers.

    Args:
        pyramid (list[list[int]]): The pyramid of numbers.

    Returns:
        int: The maximum path sum.

    """
    max_path = 0
    for i in range(2**len(pyramid)):
        path = 0
        index = 0
        for layer in range(len(pyramid)):
            path += pyramid[layer][index]
            if i % 2 == 0:
                index += 1
            i //= 2
        if path > max_path:
            max_path = path
    return max_path

print(get_max_path(pyramid))   