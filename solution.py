import pandas as pd
import numpy as np


chat_id = 469801461 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    import scipy.stats as sps
    alpha = 0.03
    return sps.ttest_ind(x, y)[1] <= alpha
    
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
