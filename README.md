# tdd_demo

[![Build Status](https://travis-ci.com/sertansenturk/tdd_demo.svg?branch=master)](https://travis-ci.com/sertansenturk/tdd_demo) [![codecov](https://codecov.io/gh/sertansenturk/tdd_demo/branch/master/graph/badge.svg)](https://codecov.io/gh/sertansenturk/tdd_demo) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple demo for test-driven development, automated testing, code style checking, and continuous integration

In this demo, we implement a simple function using test-driven development. Later, we show how to automate the tests, setup, and coding style in our local machine. Finally, we do the automation using continuous integration service.

Consider you are assigned the ticket below:

----------

## Convert Hz scale to cent scale

**One-line summary (optional)**: Implement a method called `hz_to_cent` under the `demo` package in `converter.py`, which accepts an array of values in Hz and converts them to cents.

**Reason**: This is a common transformation we have to apply in many signal processing tasks.

**Design**: Create a method which has the inputs:

- hz_seq: `Union[List[float], np.array]` sequence of hz values
- ref_hz: `Union[float, np.float]` reference freuency for conversion
- min_hz: `Union[float, np.float]` minimum freq value to convert, defaults to 20 Hz. All values below this value returns a `np.nan`.

The output of the method is a `np.array` of cent values. The conversion formula is `np.log2(hz_seq / ref_hz) * NUM_CENTS_IN_OCTAVE`, where `NUM_CENTS_IN_OCTAVE = 1200`.

**Unit tests**

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

- Unit tests must pass
- Function implemented

**Extra Tasks**

- A docker image created with the `demo` package installed. Base the `Dockerfile` on the Python 3.7-slim-buster official Docker image
- Code styling, unit tests, linting, setup and Docker build automatically validated by `tox`
- Tests, setup and Docker builds run automatically via Travis CI

**Outcome**

- Clarify the deliverables (code, process etc.) and documentation, where applicable.

**Don't forget to**

- Point the ticket
- Set priority as a label
- Assign to a person
- Link dependencies, if applicable

----------

## Good development practices

*We assume that you are using [git](https://en.wikipedia.org/wiki/Git), and you are familiar with the terminology and the commands. If you are not using `git` yet, start already!!*

As a good practice, never do development on your `master` branch, unless you are working on a `hot-fix`. You should open a new branch for each ticket/task. Once you are finished, create a `pull request` (PR) to merge your branch, instead of merging directly. PRs are quite useful for reviewing your code & getting approval/suggestions from others.

If many people use your code, you should care for the stability. For this reason, you should properly version the code as you do further development. It is a good idea to follow the `MAJOR.MINOR.PATCH` pattern of [semantic versioning](https://semver.org/). Another complementary approach is to have a `development` branch, where your PRs are merged instead of `master`. Once the `dev` branch has a meaningful amount of changes and it tested thoroughly, you can increment the package version, and merge `dev` to `master` with another PR.

While merging `dev` to `master`, it is typically useful to add a *git tag*. In addition, many `git` services such as *Github*, allow you to create a *release* with a tag. For instance, refer to the [v1.0.0 release](https://github.com/sertansenturk/tdd_demo/releases/tag/v1.0.0) for the first stable version of this repo.

## Unit tests

In test-driven development, you initially start with unit tests and later work on the solution. This way, you can ensure that your implementation is well-thought, and it fulfils the requirements.

For unit tests, we use [pytest](https://pytest.org/en/latest/), which is one of the most used unit test libraries for Python. Our tests live in a folder called `tests` under the repo. The modules are a mirror image of the `demo` package, with a prefix `test_` added to each module name. Having a parallel structure helps us to build small, incremental tests, and keep track of what is being tested with ease.

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

```bash
pip install pytest
```

Run the unit tests:

```bash
pytest tests/
```

You may also add additional options, e.g. to control verbosity. Please check the `pytest` documentation for information.

In TDD, you should implement the tests one-by-one, starting from the simplest, before you start coding the solution. You implement/build upon the solution after each test (or a meaningful set of similar tests) is implemented. This stepwise approach makes us implement small increments, and hence develop a solution easily and rapidly while closely following the requirements.

We use the so-called ["GIVEN, WHEN, THEN" pattern](https://pythontesting.net/strategy/given-when-then-2/) to write our tests. The unit tests should not overlap as much as possible.

## Code coverage

Code coverage is identifying what and how much the unit tests cover the codebase. Undoubtedly, the coverage should be as high as possible. Nevertheless, it is not necessarily a good idea to obsess over 100% coverage. Typically, there would be a bit of code, which would be trivial, tedious or unsuitable for testing. An example is bootstrapping functions, which may be changed shortly. Trying to cover everything would take an unreasonable amount of time, and hence take away from precious development time.

We use a `pytest` extension called `pytest-cov` to measure the coverage.

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

```bash
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
```

For more options, please refer to the `pytest-cov` [documentation](https://pytest-cov.readthedocs.io/en/latest/).

## Code styling

When you are writing code, especially if it is going to be used/developed by others, it is important to follow a consistent style so that the code is readable and frustrations over subjective decisions are reduced.

There are several style guides for Python. The most popular is arguably **PEP 8**, which is the official guideline. We use `flake8`, which is a command-line tool for checking [PEP8](https://www.python.org/dev/peps/pep-0008/) rules automatically.

**Important:** make sure that the virtual environment is activated.

Install `flake8` by:

```bash
pip install flake8
```

Run `flake8` by pointing to the main package:

```bash
flake8 demo
```

## Linting

Linters sniff out both stylistic and syntactical problems (such as complex functions, unused variables, or unreachable code), which not only highlight unconventional coding practices but may also indicate potential errors in implementation. Therefore, [linting](https://en.wikipedia.org/wiki/Lint_%28software%29) takes code styling to one step further because it checks how the code is executed in addition to its appearance.

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

A more convenient option is to supply the the additional options from a configuration file. Please refer to [`.pylintrc` file](.pylintrc) in this repo for a simple example. For more options, please refer to the [pylint documentation](http://pylint.pycqa.org/en/latest/user_guide/run.html#command-line-options).

## Create a Docker image

We use [Docker](https://www.docker.com/) for containerization. This way, we can decouple the code from the platform, and deploy it to anywhere with ease.

For demonstration purposes, we create a simple Dockerfile, which has the `demo` package installed.

To build the Docker image, run:

```bash
docker build -t tdd-demo:0.1 .
```

Then run an interactive container by:

```bash
docker run -it tdd-demo:0.1
```

The entry point for the running image is the Python shell.

## Local automation

During development, it would be too tedious to run all the steps above. Instead, we use [tox](https://tox.readthedocs.io/en/latest/) to automate.

**Important:** make sure that the virtual environment is activated.

Install `tox` by:

```bash
pip install tox
```

We created a [`tox.ini` file](tox.ini) to configure the automation, i.e. unit tests, code styling, linting, Docker setup. We make the checks on whichever Python versions installed locally from `3.5` to `3.7`.

Having set the `tox.ini` file, calling `tox` is trivial:

```bash
tox
```

After running `tox`, a coverage report will be created in the folder `htmlcov`. You can inspect the report in the browser of your choice.

## Continuous integration

While `tox` helps us substantially when we want to make sure everything works locally, it does not bring any protection against forgetfulness: we should not be allowed to merge code to *remote* if there are problems.

We replicate the local `tox` automation by activating the [Travis CI](https://travis-ci.org/), a [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) service. Travis CI runs the steps above each time a change is made to the Github codebase.

To use Travis CI, you should first authorize the service to integrate with Github. Then you need to enable the repository. Please follow the [official tutorial](https://docs.travis-ci.com/user/tutorial/) to complete these steps.

To configure the CI, we need to add a file to the repo, called [.travis.yml](.travis.yml). If you inspect the file, you will realize that we reuse the [tox.ini](tox.ini) configuration, where we had already automated the checks for *code styling, unit tests, linting, local setup* and *Docker build*.

Whenever there is a change in the git repo such as a push to *remote*, a new *pull request*, a branch merge, or a new tag, Travis CI runs automatically. You can inspect the run [in real-time](https://travis-ci.com/sertansenturk/tdd_demo). Moreover, you may configure Travis CI to send an e-mail and/or Slack notification, if something goes wrong.

In Github, Travis CI (and *codecov*) reports are conveniently attached to the PRs. You may also configure the repo such that these checks have to be passed for merging, and therefore mitigate the risk to distribute defective code.

## Next steps

There is still a lot to cover, e.g. extending the style checks and linting (import order, docstring tests etc.), [mocking](https://stackoverflow.com/a/2666006), [smoke tests](https://en.wikipedia.org/wiki/Smoke_testing_(software)), [integration tests](https://en.wikipedia.org/wiki/Integration_testing), [regression tests](https://en.wikipedia.org/wiki/Regression_testing), [continous delivery/deployment](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment). We may cover these in this repo in the future, if there is some demand. ;)

## References

[1] Şentürk, Sertan. (2017, January). Why Reproducibility Matters? A Personal Experience. Zenodo. http://doi.org/10.5281/zenodo.255537