import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv

df = pd.read_csv(r'F:\Python Projects\Bell Curve\data.csv')
fig = ff.create_distplot([df["Avg Rating"].to_list()],["Avg Rating"],show_hist=False)
fig.show()