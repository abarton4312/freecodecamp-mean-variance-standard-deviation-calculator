import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')
    
    arr = np.array(
        [lst[:3],
        lst[3:6],
        lst[6:]])

    calculations = {
        'mean': [list(arr.mean(axis=0)), list(arr.mean(axis=1)), np.mean(lst)],
        'variance': [list(arr.var(axis=0)), list(arr.var(axis=1)), np.var(lst)],
        'standard deviation': [list(arr.std(axis=0)), list(arr.std(axis=1)), np.std(lst)],
        'max': [list(arr.max(axis=0)), list(arr.max(axis=1)), max(lst)],
        'min': [list(arr.min(axis=0)), list(arr.min(axis=1)), min(lst)],
        'sum': [list(arr.sum(axis=0)), list(arr.sum(axis=1)), sum(lst)]
    }

    return calculations
