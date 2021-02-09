# import-checker

An experiment using the python [ast](https://docs.python.org/3/library/ast.html#module-ast) library to parse the `setup.py` `setup()` function in order to find the contents of the `install_requires` arg.

## run tests

```bash
virtualenv env -p python3
source env/bin/activate
pip install pytest
pytest
```
