import pandas as pd
import plotly.express as pe
import csv
df=pd.read_csv("data_stu.csv")
mean = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
fig = pe.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()