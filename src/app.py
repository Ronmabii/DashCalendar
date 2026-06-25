from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd
from pathlib import Path
import plotly.express as px


app = Dash()

csvPath = Path(__file__).parent.parent/'data'/'Mileage.csv'

df = pd.read_csv(csvPath)

df["Date"] = pd.to_datetime(df["Date"]) # needs this to be recognized as a continuous timeline, otherwise compressed(str to datetime)


fig = px.scatter(df,x='Date',y='Miles',title="Running Timeline")

app.layout = html.Div(
    [
        # dag.AgGrid(
        # rowData=df.to_dict("records"),
        # columnDefs=[{"field":i} for i in df.columns]),
        fig.show()
    ]
)


if __name__ == '__main__':
    app.run(debug=True)

# app.layout = [html.Div(children="Heckoff",id="training-calendar-container")]

# app.layout = html.Div(
#     [
#         dag.AgGrid(
#             rowData=df.to_dict("records"),
#             columnDefs=[{"field":i} for i in df.columns]
#         )
#     ]
# )





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