import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [10, 20, 30, 40], "B": [11, 22, 33, 44]})
print(df.A * df.B)
