# Preload

Python programs often seem to "hang" in the beginning. This is due to
heavy modules being imported. This package lets the user know what is
happening, to avoid this impression:

![A console showing the output of the program under "Usage"](https://raw.githubusercontent.com/tfiers/preload/master/example.gif)


## Installation

```
pip install preload
```
This will get you the
[![Latest version on PyPI](https://img.shields.io/pypi/v/preload.svg?label=latest%20version%20on%20PyPI:)](https://pypi.python.org/pypi/preload/)

## Usage

```python
from preload import preload
preload(["matplotlib.pyplot", "scipy.signal"])

# Rest of your imports and code, such as:
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

print("Hello")
```
