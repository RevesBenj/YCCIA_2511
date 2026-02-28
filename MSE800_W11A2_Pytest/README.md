# Calculator + Pytest (Manual + Automated Testing)

## 1) Setup (Windows PowerShell example)
```powershell
# go inside project folder
cd pytest_demo

# create venv (optional but recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# install deps
pip install -r requirements.txt
```

## 2) Manual testing (quick run)
Open Python REPL:
```powershell
python
```

Run:
```python
from mypackage.calculator import add, subtract, multiply, divide

add(2, 3)          # expect 5
subtract(10, 5)    # expect 5
multiply(3, 4)     # expect 12
divide(10, 2)      # expect 5.0

divide(10, 0)      # expect ValueError: Cannot divide by zero
```

## 3) Automated testing
Run all tests in detailed:
```powershell
pytest -v
```

Run tests + coverage (terminal report):
```powershell
pytest --cov=mypackage --cov-report=term-missing
```

Generate HTML coverage report:
```powershell
pytest --cov=mypackage --cov-report=html
```

Open the report:
- `htmlcov/index.html`
