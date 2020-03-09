def saddle_points(matrix):
    if len(set([len(row) for row in matrix])) > 1:
        raise ValueError("Irregular matrices are not supported.")

    result_points = []
    row_maxs = [max(x) for x in matrix]
    col_mins = [min(x) for x in zip(*matrix)]

    for r, row_max in enumerate(row_maxs):
        for c, col_min in enumerate(col_mins):
            if row_max == col_min:
                result_points.append({"row": r + 1, "column": c + 1})

    return result_points
