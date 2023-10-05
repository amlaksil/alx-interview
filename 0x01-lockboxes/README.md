# Lockboxes Module

The Lockboxes module provides a function for determining if all the boxes can be opened.

## Installation

1. Clone this github repository

```bash
git clone https://github.com/amlaksil/alx-interview.git 0x01-lockboxes
```

2. Navigate to project directory
```bash
cd 0x01-lockboxes
```

## Usage

Import the canUnlockAll function from the 0-lockboxes module:
```bash
from 0-lockboxes import canUnlockAll
```
Call the canUnlockAll function with a list of boxes to check if they can all be opened:
```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes)) # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes)) # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes)) # Output: False
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
