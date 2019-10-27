# tdd_demo
A simple demo for test driven development, automated testing, code style checking, and continous integration

In this demo, we implement a simple function using test driven development. Later, we show how to automate the tests, setup, and coding style in our local machine. Finally, we do the automation using continuous integration service.

Consider you are assigned the ticket below:

----------
## Convert hz scale to cent scale
**One-line summary (optional)**: Implement a method called `hz_to_cent` under the `demo` package in `converter.py`, which accepts an array of values in Hz and converts them to cents.

**Reason**: This is a common transformation we have to apply for many signal processing tasks.

**Design**: Create a method which has the inputs:
- hz_seq: `Union[List[float], np.array]` sequence of hz values
- ref_hz: `Union[float, np.float]` reference freuency for conversion
- min_hz: `Union[float, np.float]` minimum freq value to convert, defaults to 20 Hz. All values below this value returns a `np.nan`.

The output of the method is a `np.array` of cent values. The conversion formula is `np.log2(hz_seq / ref_hz) * NUM_CENTS_IN_OCTAVE`, where `NUM_CENTS_IN_OCTAVE = 1200`.

**Unittests**
- `hz_seq` is not a `List` or `np.array`; raises a `ValueError`
- At least one values in `hz_seq` is not between `20 Hz` and `20k Hz`; raises a `ValueError`
- `ref_hz` is not a `float` or `np.float`; raises a `ValueError`
- `ref_hz` is not between `20 Hz` and `20k Hz`; raises a `ValueError`
- `min_hz` is not a `float` or `np.float`; raises a `ValueError`
- `min_hz` is not between `20 Hz` and `20k Hz`; raises a `ValueError`
- `hz_seq` is `[]`; returns `np.array([])`
- `hz_seq` is `[ref_hz]`; returns `np.array([0.0])`
- `hz_seq` is `[ref_hz * 2]`; returns `np.array([1200.0])`
- `hz_seq` is `[ref_hz / 2]`; returns `np.array([-1200.0])`
- `hz_seq` is `[ref_hz, ref_hz * 2]`; returns `[0.0, 1200.0]`
- `hz_seq` is `[20]`, `ref_hz` is `20`, and `min_hz` is not given (default); returns `np.array([0.0])`
- `hz_seq` is `[20000]`, `ref_hz` is `20000`, and `min_hz` is not given (default); returns `np.array([0.0])`
- `hz_seq` is `[50]`, `ref_hz` is `100`, and `min_hz` is `50`; returns `np.array([-1200.0])`
- `hz_seq` is `[50]`, `ref_hz` is `25`, and `min_hz` is `50`; returns `np.array([1200.0])`
- `hz_seq` is `[50]`, `ref_hz` is `25`, and `min_hz` is `100`; returns `np.array([np.nan])`

**Acceptance Criteria**
- Unittests must pass
- Function implemented

**Extra Tasks**
- A docker image created with the `demo` package installed. Base the `Dockerfile` on the Python 3.7-slim-buster official Docker image
- Code styling, unittests, linting and setup checks automated by `tox`
- Tests, setup and Docker builds run automatically via Travis CI

**Outcome**
- Clarify the deliverables (code, process etc.) and documentation, where applicable.

**Don't forget to**
- Point the ticket
- Set priority as a label
- Assign to a person
- Link dependencies, if applicable

----------

## Unittests
In test driven development, you initially start with unittests and later work on the solution. This way you can ensure that your implementation is well-thought and it fulfills the requirements.

For unittests, we use [pytest](https://pytest.org/en/latest/), which is one of the most used unittest libraries for Python. Our tests live in a folder called `tests` under the repo. The modules are a mirror image of the `demo` package, with a prefix `test_` added to each module name. Having a parallel structure helps us to build small, incremental tests, and keep a track of what is being tested with ease.

First, create a `virtualenv` to isolate our development environment from the OS Python. Please follow the [instructions to install `pip` and `virtualenv`](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/), if you don't have them on your system. Once they are installed, you can create a virtual environment by:

```bash
cd /path/to/tdd_demo_repo
virtualenv -p python3 env
```

Above command creates a virtual environment called `env` on the folder of this repository. Next, activate the environment:

```bash
source env/bin/activate
```

Install `pytest`:

```
pip install pytest
```

Run the unittests:

```bash
pytest tests/    
```

You may also add additional options, e.g. to control verbosity. Please check the `pytest` documentation for information.

In TDD, you should implement the tests one-by-one, starting from the simplest, before you start coding the solution. You implement/build upon the solution after each test (or a meaningful set of similar tests) is implemented. This helps us to focus on a smaller step, and hence develop the solution easily and rapidly while closely following the requirements.

We use the so-called ["GIVEN, WHEN, THEN" pattern](https://pythontesting.net/strategy/given-when-then-2/) to write our tests. The unittests should not overlap as much as possible.

# Code coverage

Code coverage is identifying what and how much the unittests cover the codebase. Undoubtedly, the coverage should be as high as possible. Nevertheless, it is not necessarily a good idea to obsess over 100% coverage. Typically, there would be bit of code, which would be trivial, tedious or unsuitable to test. An example is bootstrapping functions, which may be changed in near future. Trying to cover everything would take an unreasonable amount of time and it will take away from precious development time.

We will use a `pytest` extension called `pytest-cov` to measure the coverage. 

**Important:** make sure that the virtual environment is activated.

Install `pytest-cov` by:

```bash
pip install pytest-cov
```

We can now run `pytest` with additional instructions to obtain the coverage:

```bash
pytest tests --cov=demo --cov-report term 
```

Above, we are pointing that we want the coverage for the package `demo` and we want to see the report per term. After running the output should be similar to:

    ========================================================================= test session starts ==========================================================================
    platform linux -- Python 3.5.2, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
    rootdir: /path/to/tdd_demo_repo
    plugins: cov-2.8.1
    collected 20 items                               

    tests/test_converter.py ....................                                                                                                                     [100%]

    ----------- coverage: platform linux, python 3.5.2-final-0 -----------
    Name                Stmts   Miss  Cover
    ---------------------------------------
    demo/__init__.py        1      0   100%
    demo/converter.py      32      0   100%
    ---------------------------------------
    TOTAL                  33      0   100%

For more options, please refer to the `pytest-cov` [documentation](https://pytest-cov.readthedocs.io/en/latest/).

# Code styling

When you are writing code, especially if it is going to be used/developed by others, it is important to follow a consistent style so that the code is readable and frustrations over subjective decisions are reduced.

There are several style guides for Python. The most popular is arguably **PEP 8**, which is the official guideline. We use `flake8`, which is a command line tool for checking PEP8 rules automatically.

**Important:** make sure that the virtual environment is activated.

Install `flake8` by:

```bash
pip install flake8
```

Run `flake8` by pointing to the main package:

```bash
flake8 demo
```

# Linting

Linters sniff out both stylistic amd syntatical problems (such as complex functions, unused variables, or unreachable code), which not only highlight unconventional coding practices but may also indicate potential errors in implementation. Therefore, [linting](https://en.wikipedia.org/wiki/Lint_%28software%29) takes code styling to one step further because it checks how the code is executed in addition to its appearance.

We use `pylint` for checking linting problems. 

**Important:** make sure that the virtual environment is activated.

Install `pylint` by:

```bash
pip install pylint
```

Run `pylint` by pointing to the main package:

```bash
pylint demo
```

You may not necessarily want to deal with all reported issues, e.g. *C0114: missing-module-docstring*, which checks if a [Python module](https://docs.python.org/3/tutorial/modules.html) has a docstring. We can disable this check by including the `disable` option:

```bash
pylint demo --disable=C0114
```

A more convenient option to supply the additional options is to save them in from a configuration. Please refer to `.pylintrc` in this repo for a simple example. For more options, please refer to the pylint documentation](http://pylint.pycqa.org/en/latest/user_guide/run.html#command-line-options).

# Create a Docker image
We use [Docker](https://www.docker.com/) for containarization. This way we can decouple the code from the hardware, and easily deploy it to anywhere.

For demonstration purposes, we create a simple Dockerfile, which has the `demo` package installed.

To build the Docker image, run:

```bash
docker build -t tdd-demo:0.1 .
```

Then run an interactive container by:

```bash
docker run -it tdd-demo:0.1
```

The entrypoint for the running image is the Python shell. 

TODO: create a script which import demo package automatically.

# Local automation

It will be too tedious to run all the steps above. Instead, we use [tox](https://tox.readthedocs.io/en/latest/) to automate.

**Important:** make sure that the virtual environment is activated.

Install `tox` by:

```bash
pip install tox
```

We created a `tox.ini` file to configure the automation, i.e. unittests, code styling, linting, Docker setup. We also make the checks on Python versions `3.5` to `3.7`.

Having set the `tox.ini` file, calling `tox` is trivial:

```bash
tox
```

# Continous integration

Finally, we replicate the local automation using tox to [Travis CI](https://travis-ci.org/), a continous integration service. Travis CI runs the steps above every time a change is made to the Github codebase.