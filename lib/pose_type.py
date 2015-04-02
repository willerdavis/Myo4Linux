from enum import IntEnum

class PoseType(IntEnum):
    REST = 0
    FIST = 1
    WAVE_IN = 2
    WAVE_OUT = 3
    FINGERS_SPREAD = 4
    DOUBLE_TAP = 5
    UNKNOWN = 255