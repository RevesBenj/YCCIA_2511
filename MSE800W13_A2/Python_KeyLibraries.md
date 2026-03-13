# Python Important Libraries - Description and Examples

## 1. OS 

Official Documentation:
https://docs.python.org/3/library/os.html

**Description:**\
The `os` library allows Python to interact with the operating system. It
can create folders, read files, check environment variables, and manage
file paths.

**Example 1: Get current working directory**

``` python
import os
print(os.getcwd())
```

**Example 2: Create a new folder**

``` python
import os
os.mkdir("new_folder")
```

------------------------------------------------------------------------

## 2. SYS

Official Documentation:
https://docs.python.org/3/library/sys.html

**Description:**\
The `sys` library provides access to system-specific parameters and
functions such as command line arguments and Python runtime information.

**Example 1: Read command line arguments**

``` python
import sys
print(sys.argv)
```

**Example 2: Exit a program**

``` python
import sys
print("Program stopping")
sys.exit()
```

------------------------------------------------------------------------

## 3. NUMPY

Official Documentation:
https://numpy.org/doc/

**Description:**\
`NumPy` is a powerful library used for numerical computing and working
with arrays and matrices.

**Example 1: Create an array**

``` python
import numpy as np
arr = np.array([1,2,3,4])
print(arr)
```

**Example 2: Matrix multiplication**

``` python
import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a @ b)
```

------------------------------------------------------------------------

## 4. pathlib

Official Documentation:
https://docs.python.org/3/library/pathlib.html

**Description:**\
`pathlib` is used to work with file system paths in an easier and more
readable way than traditional string paths.

**Example 1: Create a path**

``` python
from pathlib import Path
path = Path("data/file.txt")
print(path)
```

**Example 2: Check if file exists**

``` python
from pathlib import Path
file = Path("data.txt")
print(file.exists())
```

------------------------------------------------------------------------

## 5. datetime

Official Documentation:
https://docs.python.org/3/library/datetime.html

**Description:**\
The `datetime` library is used for working with dates and times.

**Example 1: Get current date**

``` python
from datetime import datetime
now = datetime.now()
print(now)
```

**Example 2: Format date**

``` python
from datetime import datetime
today = datetime.now()
print(today.strftime("%Y-%m-%d"))
```

------------------------------------------------------------------------

## 6. logging

Official Documentation:
https://docs.python.org/3/library/logging.html

**Description:**\
`logging` is used to record messages during program execution. It helps
developers debug and monitor applications.

**Example 1: Basic logging**

``` python
import logging
logging.warning("This is a warning message")
```

**Example 2: Log to file**

``` python
import logging
logging.basicConfig(filename='app.log', level=logging.INFO)
logging.info("Program started")
```

------------------------------------------------------------------------

## 7. Django

Official Documentation:
https://docs.djangoproject.com/

**Description:**\
`Django` is a Python web framework used to build large web applications
and data-driven websites.

**Example 1: Create a simple Django view**

``` python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django")
```

**Example 2: Define URL route**

``` python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
]
```

------------------------------------------------------------------------

## 8. Flask

Official Documentation:
https://flask.palletsprojects.com/

**Description:**\
`Flask` is a lightweight Python web framework used to build small web
applications and APIs.

**Example 1: Simple Flask app**

``` python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"
```

**Example 2: API endpoint**

``` python
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"
```

------------------------------------------------------------------------

## 9. FastAPI

Official Documentation:
https://fastapi.tiangolo.com/

**Description:**\
`FastAPI` is a modern Python framework for building fast APIs with
automatic Documentation:.

**Example 1: Simple API**

``` python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}
```

**Example 2: API with parameter**

``` python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

------------------------------------------------------------------------

## 10. bcrypt

Official Documentation:
https://pypi.org/project/bcrypt/

**Description:**\
`bcrypt` is used for hashing passwords securely.

**Example 1: Hash password**

``` python
import bcrypt

password = b"mypassword"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)
```

**Example 2: Verify password**

``` python
bcrypt.checkpw(b"mypassword", hashed)
```

------------------------------------------------------------------------

## 11. pytest

Official Documentation:
https://docs.pytest.org/

**Description:**\
`pytest` is a testing framework used to write and run automated tests
for Python programs.

**Example 1: Simple test**

``` python
def add(a,b):
    return a+b

def test_add():
    assert add(2,3) == 5
```

**Example 2: Run pytest**

``` bash
pytest test_file.py
```

------------------------------------------------------------------------

## 12. pylint

Official Documentation:
https://pylint.readthedocs.io/

**Description:**\
`pylint` is a tool used to analyze Python code for errors, coding
standards, and quality issues.

**Example 1: Run pylint**

``` bash
pylint my_script.py
```

**Example 2: Check code score**

``` bash
pylint app.py
```
