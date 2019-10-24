# tdd_demo
A simple demo for test driven development, and automation

In this demo, we will code a simple function using test driven development. Later, we will show how to automate the tests, setup, and coding style in our local machine. Finally, we will do the automation using continuous integration service.

Consider you are assigned the ticket below:

----------
## Convert hz scale to cent scale
**One-line summary (optional)**: Implement a method called `hz_to_cent` under the `demo` package in `converter.py`, which accepts an array of values in Hz and converts them to cents.

**Reason**: This is a common transformation we have to apply for many signal processing tasks.

**Design**: Create a method which has the inputs:
- hz_seq: `Union[List[float], np.array]` sequence of hz values
- ref_hz: `Union[float, np.float]` reference freuency for conversion
- min_hz: `Union[float, np.float]` minimum freq value to convert, defaults to 20 Hz. All values below this value will return a `np.nan`.

The output of the method is a `np.array` of cent values. The conversion formula is `np.log2(hz_seq / ref_hz) * NUM_CENTS_IN_OCTAVE`, where `NUM_CENTS_IN_OCTAVE = 1200`.

**Unittests**
- `hz_seq` is not a `List` or `np.array`; raises a `ValueError`
- At least one values in `hz_seq` is not between `20 Hz` and `20k Hz`; raises a `ValueError`
- `ref_hz` is not a `float` or `np.float`; raises a `ValueError`
- `ref_hz` is not between `20 Hz` and `20k Hz`; raises a `ValueError`
- `min_hz` is not a `float` or `np.float`; raises a `ValueError`
- `min_hz` is not between `20 Hz` and `20k Hz`; raises a `ValueError`
- `hz_seq` is `[]`; returns `np.array([])`
- `hz_seq` is `[np.nan]`; returns `np.array([np.nan])`
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
- A docker image created with the `demo` package installed. Base the `Dockerfile` on the Python 3.7-alpine official Docker image
- PEP8 violations and unittests are checked via tox.
- Tests, setup and Docker builds run automatically via Travis CI

**Outcome**
- Clarify the deliverables (code, process etc.) and documentation, where applicable.

**Don't forget to**
- Point the ticket
- Set priority as a label
- Assign to a person
- Link dependencies, if applicable

----------

# Unittests
In test driven development, you initially start with unittests and later work on the solution. This way you can ensure that your implementation is well-thought and it fulfills the requirements.

For unittests, we will use [pytest](https://pytest.org/en/latest/), which is one of the most used unittest libraries for Python. Our tests will live in a folder called `tests` under the repo. The modules will be a mirror image of the `demo` package, with a prefix `test_` added to each module name. Having a parallel structure helps us to build small, incremental tests, and keep a track of what is being tested with ease.

To run the unittests, (after installing the `pytest` library), run:

```bash
pytest tests/    
```

You may also add additional options, e.g. to control verbosity. Please check the `pytest` documentation for information.

In TDD, you should implement the tests one-by-one, starting from the simplest, before you start coding the solution. You implement/build upon the solution after each test (or a meaningful set of similar tests) is implemented. This helps us to focus on a smaller step, and hence develop the solution easily and rapidly while closely following the requirements.

We will use the so-called ["GIVEN, WHEN, THEN" pattern](https://pythontesting.net/strategy/given-when-then-2/) to write our tests. The unittests should not overlap as much as possible.

# Create a Docker image
We will create a simple Dockerfile, which will have the `demo` package installed. The entrypoint will be the Python shell, when the image is run.

# Local automation
Later, we will also introduce [tox](https://tox.readthedocs.io/en/latest/) an automation tool for Python. We will use tox to run the unittests, check the local setup & Docker builds, and check for PEP8 & linting problems in a single go in our local machine. 

# Continous integration
Finally, we replicate the local automation using tox to [Travis CI](https://travis-ci.org/), a continous integration service. Travis CI will run the steps above every time a change is made to the Github codebase.