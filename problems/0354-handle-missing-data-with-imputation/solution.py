import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    # Your code here
    for j in range(len(data[0])):
        a = []
        c = 0
        s = 0
        d = {}
        for i in range(len(data)):
            if not np.isnan(data[i][j]):
                if strategy == "mean":
                    s += data[i][j]
                    c += 1
                elif strategy == "median":
                    c += 1
                    a.append(data[i][j])
                else:
                    c += 1
                    if float(data[i][j]) in d:
                        d[float(data[i][j])] += 1
                    else:
                        d[float(data[i][j])] = 1
        
        if c == 0: continue

        if strategy == "median":
            a.sort()
            if c % 2 == 1: m = a[c // 2]
            else: m = (a[c // 2 - 1] + a[c // 2]) / 2
        elif strategy == "mode":
            d = sorted(d.items(), key=lambda item: (-item[1], item[0]))

        for i in range(len(data)):
            if np.isnan(data[i][j]):
                if strategy == "mean":
                    data[i][j] = s / c
                elif strategy == "median":
                    data[i][j] = m
                else:
                    data[i][j] = d[0][0]

    return data 
