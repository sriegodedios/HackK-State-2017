from pandas import Series
from matplotlib import pyplot


series = Series.from_csv('per_year.csv', header=0)
print(series.head())
series.plot()
pyplot.show()