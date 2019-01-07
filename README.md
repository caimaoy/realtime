# realtime

[![Build Status](https://travis-ci.org/caimaoy/flask-realtime-import.svg?branch=master)](https://travis-ci.org/caimaoy/flask-realtime-import)
[![Coverage Status](https://coveralls.io/repos/github/caimaoy/realtime/badge.svg?branch=master)](https://coveralls.io/github/caimaoy/realtime?branch=master)

This is a toolbox for realtime.

## Installation

Installing is simple with pip:

```shell
pip install realtime
```

## Usage

Setting up the extension is simple:

```python
from realtime import realtime_import

@realtime_import
def foo():
    import PACKAGES
    return 42
```
