import numpy as np
counter = 0
arraynonnan = np.array([[np.nan, 4, np.nan, 6],  [4, 5, 6, 7], [1, 2, 3, 4]])
nrows = len(arraynonnan)
ncols = len(arraynonnan[0])
i = 0
while i <= nrows*ncols:
    for r in range(nrows):
        for c in range(ncols):
            if np.isnan(arraynonnan[r][c]):
                counter += 1
        i += 1
if counter != nrows*ncols:
    nrows = len(arraynonnan)
    ncols = len(arraynonnan[0])
    for r in range(nrows):
        for c in range(ncols):
            if np.isnan(arraynonnan[r][c]):
                arraynonnan[r][c] = np.nanmean(arraynonnan)
else:
    nrows = len(arraynonnan)
    ncols = len(arraynonnan[0])
    for r in range(nrows):
        for c in range(ncols):
            if np.isnan(arraynonnan[r][c]):
                arraynonnan[r][c] = 0
