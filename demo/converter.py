from typing import List, Union
import numpy as np


MIN_AUDIBLE_FREQUENCY = 20
MAX_AUDIBLE_FREQUENCY = 20000
NUM_CENTS_IN_OCTAVE = 1200

def hz_to_cent(hz_seq: Union[List[float], np.array],
               ref_hz: Union[float, np.float],
               min_hz: Union[float, np.float] = 20
               ) -> Union[List[float], np.array]:
    """Converts a sequence of frequency values in Hertz to cents.

    Arguments:
        hz_seq {Union[List[float], np.array]} -- A sequence of
            frequency values in Hertz
        ref_hz {Union[float, np.float]} -- Reference frequency in
            Hertz
        min_hz {Union[float, np.float]} -- Minimum frequency value
            in Hertz to convert. All values below this value will
            return a `np.nan`. (default: {20})

    Returns:
        Union[List[float], np.array] -- A sequence of frequency
            values in cents with respect to the input reference
            frequency
    """

    if isinstance(hz_seq, list):
        hz_seq = np.array(hz_seq)
    elif isinstance(hz_seq, np.ndarray):
        pass
    else:
        raise ValueError("hz_seq must be a List or numpy array "
                         "of numbers.")

    if any(hz_seq < MIN_AUDIBLE_FREQUENCY):
        raise ValueError("hz_seq cannot have values lower than %d "
                         "Hz." % MIN_AUDIBLE_FREQUENCY)
    elif any(hz_seq > MAX_AUDIBLE_FREQUENCY):
        raise ValueError("hz_seq cannot have values higher than "
                         "%d Hz." % MAX_AUDIBLE_FREQUENCY)

    if not isinstance(ref_hz, (int, float, np.int, np.float)):
        raise ValueError("ref_hz must be a number.")

    if ref_hz < MIN_AUDIBLE_FREQUENCY:
        raise ValueError("ref_hz must be higher than %d Hz."
                         % MIN_AUDIBLE_FREQUENCY)
    elif ref_hz > MAX_AUDIBLE_FREQUENCY:
        raise ValueError("ref_hz must be lower than %d Hz."
                         % MAX_AUDIBLE_FREQUENCY)

    if not isinstance(min_hz, (int, float, np.int, np.float)):
        raise ValueError("min_hz must be a number.")

    if min_hz < MIN_AUDIBLE_FREQUENCY:
        raise ValueError("min_hz must be higher than %d Hz."
                         % MIN_AUDIBLE_FREQUENCY)
    elif min_hz > MAX_AUDIBLE_FREQUENCY:
        raise ValueError("min_hz must be lower than %d Hz."
                         % MAX_AUDIBLE_FREQUENCY)

    if hz_seq.size == 0:  # empty sequence
        return hz_seq

    return np.log2(hz_seq / ref_hz) * NUM_CENTS_IN_OCTAVE
