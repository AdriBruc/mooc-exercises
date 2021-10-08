from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")  # write your function instead of this one
    x = int(shape[1]/10)
    y = int(shape[0]/10)
    res[5*y:, 3*x:5*x] = 1
    res[5*y:, 5*x:7*x] = -1
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")  # write your function instead of this one
    x = int(shape[1]/10)
    y = int(shape[0]/10)
    res[5*y:, 3*x:5*x] = -1
    res[5*y:, 5*x:7*x] = 1
    return res
