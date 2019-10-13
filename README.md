# tdd_demo
A simple demo for test driven development, and automation

In this demo, we will code a simple function using test driven development. Later, we will show how to automate the tests, setup, and coding style in our local machine. Finally, we will do the automation using continuous integration service.

Consider you are assigned the ticket below:

----------
## Convert hz scale to cent scale
**One-line summary (optional)**: Implement a method called `hz_to_cent` under the `demo` package in `converter.py`, which accepts an array of values in Hz and converts them to cents.

**Reason**: This is a common transformation we have to apply for many signal processing tasks.

**Design**: Create a method which has the inputs:
- hz_list: `Union[List[float], np.array]` list of hz values
- ref_hz: `Union[float, np.float]` reference freuency for conversion
- min_hz: Minimum freq value to convert. All values below this value will return a `np.nan`.

The output of the method is a `np.array` of cent values. The conversion formula is `np.log2(hz_track / ref_freq) * NUM_CENTS_IN_OCTAVE`, where `NUM_CENTS_IN_OCTAVE = 1200`.

**Acceptance Criteria**
- Unittests must pass
- Function implemented

**Extra Tasks**
- A docker image created with the 
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

For unittests, we will use [pytest](https://pytest.org/en/latest/), which is one of the most used unittest libraries ifor Python.

# Create a Docker image
TODO

# Local automation
Later, we will also introduce [tox](https://tox.readthedocs.io/en/latest/) an automation tool for Python. We will use tox to run the unittests, check the local setup & Docker builds, and check for PEP8 & linting problems in a single go in our local machine. 

# Continous integration
Finally, we replicate the local automation using tox to [Travis CI](https://travis-ci.org/), a continous integration service. Travis CI will run the steps above every time a change is made to the Github codebase.