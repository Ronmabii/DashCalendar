from dash import Dash, html, dcc
import pandas as pd
from pathlib import Path
import plotly.express as px


app = Dash()

csvPath = Path(__file__).parent.parent/'data'/'Mileage.csv'

df = pd.read_csv(csvPath)

df[["Date","Week (Monday)"]] = df[["Date","Week (Monday)"]].apply(pd.to_datetime) # needs this to be recognized as a continuous timeline, otherwise compressed(str to datetime)

weeklyMileageSum = (
    df.groupby("Week (Monday)", as_index=False)["Miles"] # without as_index wrong column entered into fig
      .sum()
)

fig = px.bar(
    weeklyMileageSum,
    x="Week (Monday)",
    y="Miles",
    labels={
        "Week (Monday)": "Weeks",
        "Miles": "Total Miles"
    },
    title="Weekly Running Mileage"
)

# fig = px.scatter(df,x='Date',y='Miles',title="Running Timeline") # daily dots

app.layout = html.Div(
    [
        html.H1("Big Head"),
        dcc.Graph(id='chart', figure = fig)
    ]
)



if __name__ == '__main__':
    app.run(debug=True)



# from dash import Dash, html, Input, Output, callback, ctx

# app = Dash()

# app.layout = html.Div(
#     [
#         html.Button("Button 1", id="btn-1"),
#         html.Button("Button 2", id="btn-2"),
#         html.Div(id="output-div"),
#     ]
# )


# @callback(
#     Output("output-div", "children"),
#     [
#         Input("btn-1", "n_clicks"),
#         Input("btn-2", "n_clicks"),
#     ],
# )
# def func(n_clicks_btn1, n_clicks_btn2):
#     button_id = ctx.triggered_id
#     message = f"You've clicked {button_id} last" if button_id else "No clicks yet"
#     return message


# if __name__ == "__main__":
#     app.run(debug=True)