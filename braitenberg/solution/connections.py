from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")  # write your function instead of this one
    x_mid = int(shape[1]/2)
    y_mid = int(shape[0]/2)
    res[:y_mid, :x_mid] = 1
    res[y_mid:, :x_mid] = 5
    res[:y_mid, x_mid:] = -1
    res[y_mid:, x_mid:] = -5
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")  # write your function instead of this one
    x_mid = int(shape[1]/2)
    y_mid = int(shape[0]/2)
    res[:y_mid, :x_mid] = -1
    res[y_mid:, :x_mid] = -5
    res[:y_mid, x_mid:] = 1
    res[y_mid:, x_mid:] = 5
    return res
