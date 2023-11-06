import pandas as pd
import numpy as np

"""

a = ["Ade", "Bolu", "Cynthia", "Dessy", "Esther"]
myvar = pd.Series(a)
print(myvar)

myList =["HP", "DELL", "ASUS", "TOSHIBA", "LENOVO"]

myvad= pd.Series(myList, index= ["A", "B", "C", "D", "E"])
# print(myvad)
# print(myvad["C"])

mydict = {1: "panda", 2: "numpy", 3: "scikitlearn", 4: "seaborne", 5: "mathpy"}
myselSeries = pd.Series(mydict, index=[1, 2, 5])
# print(myselSeries)
myseries = pd.Series(mydict)
# print(myseries)
# print(myseries[5])

my2dList = [[420, 380, 360], [50, 40, 45]]
my2dSeries = pd.Series(my2dList, index=["calories", "duration"])
my2dArr = np.array(my2dList)
# print(my2dArr)
# print(my2dSeries)

mydf = pd.DataFrame(my2dSeries)
print(mydf)
"""
"""
df = pd.read_csv("./pandas_csv_1.csv")

max_pd_rows = pd.options.display.max_rows
max_pd_cols = pd.options.display.max_columns
# print(df)
# print(df.to_string)
print(max_pd_cols)
print(max_pd_rows)
"""


