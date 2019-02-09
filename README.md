# demo_flake8_config_issue
Reproduction of issue https://github.com/tholo/pytest-flake8/issues/28

The demonstration can be invoked by:
```
> python setup.py test
```

The file mean.py contains two errors which are detect by the pytest-flake8 module.
One of them will be ignored and the other causes an error when invoking the test.
