# tdd_demo
A simple demo for test driven development

In this demo, we will code a simple function using test driven development. In test driven development, you initially start with unittests and later work on the solution. This way you can ensure that your implementation is well-thought and it fulfills the requirements.

Consider you are assigned the ticket below:

----------
## Convert hz scale to cent scale
**One-line summary (optional)**: Implement a method which accepts an array of values in Hz and converts them to cents.

**Reason**: This is a common transformation we have to apply for many signal processing tasks.

**Design**: Create a method which has the inputs:
- hz_list: `Union[List[float], np.array]` list of hz values
- ref_hz: `Union[float, np.float]` reference freuency for conversion
- min_hz: Minimum freq value to convert. All values below this value will return a `np.nan`.

The output of the method is a `np.array` of cent values. The conversion formula is `np.log2(hz_track / ref_freq) * NUM_CENTS_IN_OCTAVE`, where `NUM_CENTS_IN_OCTAVE = 1200`.

**Acceptance Criteria**
- Unittests must pass
- Function implemented
- Optional: PEP8 violations vs unittests are checked via tox.
- Optional: Tests run automatically via travis.ci

**Outcome**
- Clarify the deliverables (code, process etc.) and documentation, where applicable.

**Don't forget to**
- Point the ticket
- Set priority as a label
- Assign to a person
- Link dependencies, if applicable

----------