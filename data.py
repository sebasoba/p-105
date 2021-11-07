import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

import pandas as pd
import plotly.express as px

df = pd.read_csv("class1.csv")

fig = px.scatter(df,    x="Student Number",
                        y="Marks"
            )
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= mean, y1= mean,
      x0= 0, x1= total_entries
    )
])

fig.update_yaxes(rangemode="tozero")

fig.show()