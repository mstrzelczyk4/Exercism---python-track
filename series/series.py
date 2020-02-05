def slices(series, length):
    if length < 1 or length > len(series):
        raise ValueError("Error")
    return [series[start:start+length] for start in range(len(series) - length + 1)]
