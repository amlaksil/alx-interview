# Pascal's Triangle Generator

This repository provides a Python function `pascal_triangle(n)` that generates Pascal's triangle up to the specified number of rows. Pascal's triangle is a triangular array of numbers where each number is the sum of the two numbers directly above it. It has various applications in combinatorics and number theory.

## Function Signature

```python
def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Each inner list represents a row of Pascal's triangle, containing the entries.

    Raises:
        None

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    ```

## Usage
You can use the pascal_triangle function in your Python projects to generate Pascal's triangle. Here's an example:
```
from 0-pascal_triangle import pascal_triangle

triangle = pascal_triangle(7)
for row in triangle:
    print(row)
```
Output:
```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
```
Installation
To use the pascal_triangle function in your project, you can follow these steps:
1. Clone this GitHub repository
```
$ git clone https://github.com/amlaksil/alx-interview.git/ 0x00-pascal_triangle
```

2. Navigate to project directory
```
$ cd 0x00-pascal_triangle 
```

3. Import the pascal_trianle function in your python code
```
from 0-pascal_triangle import pascal_triangle
```

4. Call the pascal_triangle function with the desired number of rows to generate Pascal's triangle.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
