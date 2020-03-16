# libnamegen

Package containing various name generation methods. Originally on my [NameGenerator](https://github.com/BBaoVanC/NameGenerator) project.

## Features

* Easy to use
* Imported as module
* Always tested before release
* Supports latest three versions of Python 3

---

## How to Install

Run the command `pip install libnamegen`. If you want to specify a specific Python version to use for pip, use a command such as `pip3` or `pip3.8`.

libnamegen requires the package [libprogress](https://pypi.org/project/libprogress/), but it will automatically be installed by pip.

---

## Documentation

### API

Generate one classic name without debug:

``` python
from libnamegen import classic

# this uses the defaults which are one name, debug disabled, and classic generator
print(classic.gen())
```

Generate seven classic names with debug:

``` python
from libnamegen import classic

print(classic.gen(count=7, debug=True))
# print(classic.gen(7, True))  # also valid
```

Prompt the user for the amount of names, enable debug, and generate classic names:

``` python
from libnamegen import classic

amt = input("Amount of names to generate >> ")
count = int(amt)

names = classic.gen(count, true)
for name in names:
  print(name)
```

Generate one random name without debug:

``` python
from libnamegen import random

print(random.gen())
```

Generate one name using the random method 15 characters long:

``` python
from libnamegen import random

print(random.gen(length=15))
```

You can also import the entire libnamegen package, which will import all generation methods:

``` python
import libnamegen

print(libnamegen.classic.gen())
```

---

## License

_libnamegen_ is licensed under the GPLv3 license. For more information, please refer to [`LICENSE`](https://github.com/BBaoVanC/libnamegen/blob/master/LICENSE).
