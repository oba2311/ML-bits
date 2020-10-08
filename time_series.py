# Select only variable = 'A' data

# Create mock time series data
import numpy as np
from pandas import DataFrame
import pandas._testing as tm

import matplotlib.pyplot as plt

#
# def unpivot(frame):
#     N, K = frame.shape
#     data = {'value' : frame.values.ravel('F'),
#             'variable' : np.asarray(frame.columns).repeat(N),
#             'date' : np.tile(np.asarray(frame.index), K)}
#     return DataFrame(data, columns=['date', 'variable', 'value'])
#
#
# df = unpivot(tm.makeTimeDataFrame(3))
# df.head()
#
# df[df.variable == 'A']

ts = tm.makeTimeDataFrame(10)

ts.A.plot()
plt.show()
