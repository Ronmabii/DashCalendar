import dash
from dash import html, dcc, callback, Output,Input,ctx, register_page
import pandas as pd
from pathlib import Path
import plotly.express as px

dash.register_page(__name__,path='/') # Home Page

PROJECT_ROOT = Path(__file__).parents[2] # folder organization vs csv path name
csvPath = PROJECT_ROOT/ 'data'/'MILEAGE.csv' # files name caps matter more than you know
df = pd.read_csv(csvPath)

df[["Date","Week (Monday)"]] = df[["Date","Week (Monday)"]].apply(pd.to_datetime) # needs this to be recognized as a continuous timeline, otherwise compressed(str to datetime)

weeklyMileageSum = (
    df.groupby("Week (Monday)", as_index=False)["Miles"] # dff["Miles"].sum() without as_index wrong column entered into fig
      .sum()
)

dffHR = df[df["Average Heart Rate"] > 120] # super low ones might be walks

layout = html.Div(
    [
        html.Button("Overall Mileage", id="btn-overall"),
        html.Button("Weekly Mileage", id="btn-week"),
        html.Button("Heart Rate", id="btn-heart"),
        dcc.Graph(id="chart", figure = {}, style={"width": "100%", "height": "80vh"})
    ]
)

# callbacks run when page loaded
@callback(
    Output("chart", "figure"),
    [
        Input("btn-overall", "n_clicks"), 
        Input("btn-week", "n_clicks"),
        Input("btn-heart", "n_clicks"),
    ],
)
def func(n_clicks_btn1, n_clicks_btn2,n_clicks_btn3):
    button_id = ctx.triggered_id

    if button_id == "btn-week":
        fig = px.bar(weeklyMileageSum, x="Week (Monday)",y="Miles",labels={"Week (Monday)": "Weeks"},title="Weekly Running Mileage")
    elif button_id == "btn-heart":
        fig = px.scatter(dffHR, x='Date', y = 'Average Heart Rate',color="Activity Type")
    else:
        fig = px.scatter(df,x='Date',y='Miles',title="Running Timeline")

    return fig