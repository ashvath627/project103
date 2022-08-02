import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')
plot = px.scatter(df, x = 'date', y = 'cases', color ='country', title = 'Cases')
plot.show()