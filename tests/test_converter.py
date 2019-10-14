import pytest
import numpy as np
from demo.converter import hz_to_cent


def test_hz_to_cent_wrong_hz_seq_type():
    # GIVEN
    hz_seq = "non_list_type"
    ref_hz = 440

    # WHEN; THEN
    with pytest.raises(ValueError) as excinfo:
        hz_to_cent(hz_seq, ref_hz)

    assert (str(excinfo.value) ==
            'hz_seq must be a List or numpy array of numbers.')


def test_hz_to_cent_hz_seq_lower_than_20():
    # GIVEN
    hz_seq = [19.99]
    ref_hz = 440

    # WHEN; THEN
    with pytest.raises(ValueError) as excinfo:
        hz_to_cent(hz_seq, ref_hz)

    assert (str(excinfo.value) ==
            'hz_seq cannot have values lower than 20 Hz.')


def test_hz_to_cent_hz_seq_lower_than_20000():
    # GIVEN
    hz_seq = [20000.1]
    ref_hz = 440

    # WHEN; THEN
    with pytest.raises(ValueError) as excinfo:
        hz_to_cent(hz_seq, ref_hz)

    assert (str(excinfo.value) ==
            'hz_seq cannot have values higher than 20000 Hz.')


def test_hz_to_cent_wrong_ref_hz_type():
    # GIVEN
    hz_seq = [440]
    ref_hz = "non_numeric"

    # WHEN; THEN
    with pytest.raises(ValueError) as excinfo:
        hz_to_cent(hz_seq, ref_hz)

    assert (str(excinfo.value) ==
            'ref_hz must be a number.')


def test_hz_to_cent_ref_hz_lower_than_20():
    # GIVEN
    hz_seq = [440]
    ref_hz = 19.99

    # WHEN; THEN
    with pytest.raises(ValueError) as excinfo:
        hz_to_cent(hz_seq, ref_hz)

    assert (str(excinfo.value) ==
            'ref_hz must be higher than 20 Hz.')


def test_hz_to_cent_ref_hz_lower_than_20000():
    # GIVEN
    hz_seq = [440]
    ref_hz = 20000.1

    # WHEN; THEN
    with pytest.raises(ValueError) as excinfo:
        hz_to_cent(hz_seq, ref_hz)

    assert (str(excinfo.value) ==
            'ref_hz must be lower than 20000 Hz.')


def test_hz_to_cent_wrong_min_hz_type():
    # GIVEN
    hz_seq = [440]
    ref_hz = 220
    min_hz = "non_numeric"

    # WHEN; THEN
    with pytest.raises(ValueError) as excinfo:
        hz_to_cent(hz_seq, ref_hz, min_hz)

    assert (str(excinfo.value) ==
            'min_hz must be a number.')


def test_hz_to_cent_min_hz_lower_than_20():
    # GIVEN
    hz_seq = [440]
    ref_hz = 220
    min_hz = 19.99

    # WHEN; THEN
    with pytest.raises(ValueError) as excinfo:
        hz_to_cent(hz_seq, ref_hz, min_hz)

    assert (str(excinfo.value) ==
            'min_hz must be higher than 20 Hz.')


def test_hz_to_cent_min_hz_lower_than_20000():
    # GIVEN
    hz_seq = [440]
    ref_hz = 220
    min_hz = 20000.1

    # WHEN; THEN
    with pytest.raises(ValueError) as excinfo:
        hz_to_cent(hz_seq, ref_hz, min_hz)

    assert (str(excinfo.value) ==
            'min_hz must be lower than 20000 Hz.')


def test_hz_to_cent_empty_hz_seq():
    # GIVEN
    hz_seq = []
    ref_hz = 220

    # WHEN
    result = hz_to_cent(hz_seq, ref_hz)

    # THEN
    expected = np.array([])
    assert np.array_equal(result, expected)


def test_hz_to_cent_hz_seq_ref_hz_same():
    # GIVEN
    hz_seq = [440]
    ref_hz = 440

    # WHEN
    result = hz_to_cent(hz_seq, ref_hz)

    # THEN
    expected = np.array([0])
    assert np.array_equal(result, expected)
