### Hexlet tests and linter status:
[![Actions Status](https://github.com/glebondri/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/glebondri/python-project-50/actions)
[![Actions Status](https://github.com/glebondri/python-project-50/actions/workflows/tests-and-linter.yml/badge.svg)](https://github.com/glebondri/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/52a1468053b6d4085b22/maintainability)](https://codeclimate.com/github/glebondri/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/52a1468053b6d4085b22/test_coverage)](https://codeclimate.com/github/glebondri/python-project-50/test_coverage)

# Comparison Tool
**A Python CLI tool to compare configuration files**


## Requirements:
 - Python (^3.10)
 - Poetry

## Installation [(Asciinema)](https://asciinema.org/a/cnOp2AfGR8YDGhaL0Crp1CzX9):
    $ git clone https://github.com/glebondri/python-project-50
    $ cd python-project-50
    $ make build
    $ make package-install
    
### To get help:
```
$ gendiff --help
```

### Comparing files:
> Both files can be either ***JSON*** or ***YAML***
```bash
$ gendiff --format=plain file_a.json file_b.json

Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
...
```
**"Stylish"** format outputs pretty-looking string with the use of **curly brackets & indentation**, like JSON
 
**"Plain"** format shows step-by-step what exactly changed in the **new** file relative to **original**
 
**"Json"** format outputs the "raw" comparison data as **JSON**


## Usage:
```python
from gendiff import generate_diff

generate_diff(first_file, second_file, out_format)
```

[![asciicast](https://asciinema.org/a/HRcVsZNZOmqJMi0ybYPJLL18u.svg)](https://asciinema.org/a/HRcVsZNZOmqJMi0ybYPJLL18u)
[![asciicast](https://asciinema.org/a/l5SMMDYxrgUKRgqsAcaReg2xt.svg)](https://asciinema.org/a/l5SMMDYxrgUKRgqsAcaReg2xt)
[![asciicast](https://asciinema.org/a/63GgLZBOdVVZJA7UWIMIn6NMb.svg)](https://asciinema.org/a/63GgLZBOdVVZJA7UWIMIn6NMb)
[![asciicast](https://asciinema.org/a/4C0UxyNVXttYX6FJ7LqhsyQbc.svg)](https://asciinema.org/a/4C0UxyNVXttYX6FJ7LqhsyQbc)
[![asciicast](https://asciinema.org/a/EhJ5kI5tMQOaXnYaY5dJHVwME.svg)](https://asciinema.org/a/EhJ5kI5tMQOaXnYaY5dJHVwME)