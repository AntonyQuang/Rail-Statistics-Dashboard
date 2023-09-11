import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from data_manager import toc_list, table_sub_headings, data_tables
from graph_manager import explanations, graph_types, all_tocs_mean_graphs, graph_colours
import plotly.express as px
import plotly.io as pio


pio.templates.default = "simple_white"
px.defaults.template = "plotly_dark"

# Initialise dash app with Bootstrap

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.DARKLY],
                meta_tags=[
                    {
                        "name": "viewport",
                        "content": "width-device-width, initial-scale=1.0"
                    }
                ],
                title="Rail Statistics Dashboard"
                )


# Core components

# Buttons

headings_buttons = html.Div(
    [
        dbc.RadioItems(
            id="headings",
            class_name="btn-group",
            input_class_name="btn-check",
            label_class_name="btn btn-primary mb-2 d-grid gap-5",
            label_checked_class_name="active",
            options=[
                {"label": "Key statistics", "value": "Key statistics"},
                {"label": "Passenger rail usage", "value": "Passenger rail usage"},
                {"label": "Passenger rail performance", "value": "Passenger rail performance"},
                {"label": "Passenger rail delays", "value": "Passenger rail delays"},
                {"label": "Passenger experience", "value": "Passenger experience"},
            ],
            value="Key statistics",
            style={'display': 'inline-block'},
        ),
    ],
    className="radio-group",

)

# Dropdown Menu

dropdown = html.Div(
    [
        dcc.Dropdown(
            toc_list,
            id="dropdown-menu",
            value="All TOC's",
            clearable=False,
        ),
    ]
)

# Define app layout

app.layout = dbc.Container(
    [
        dbc.Row([
            html.H1("Rail Statistics Dashboard"),
        ], class_name="my-3"),
        dbc.Row([
            dbc.Col([
                dbc.Row([headings_buttons]),
                dbc.Row([html.Div("A dashboard that visualises data analysis made on the UK Rail Industry between 2017-2023 \n ")], class_name="my-3 px-4"),
                dbc.Row([html.A("Detailed Analysis", href="https://colab.research.google.com/drive/19ygzlsQqY0q2sYEHoKQsQTmWNLHB_qQn?usp=sharing", target="_blank")], class_name="px-4"),
                dbc.Row([html.A("Github", href="https://github.com/AntonyQuang/Rail-Statistics-Dashboard", target="_blank")], class_name="px-4"),
                dbc.Row([html.A("Portfolio", href="https://antonyquang.github.io/Portfolio-Website/", target="_blank")], class_name="px-4"),
                dbc.Row([html.Div("Copyright Antony Quang 2023")], class_name="my-3  px-4"),
            ], width={"size": 3}, class_name="my-3"),
            dbc.Col([
                dbc.Row([
                    dbc.Col(
                        children=[html.H2(id="heading")]
                    ),
                    dbc.Col([
                        dropdown
                    ]),
                ]),
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id="graph-1")
                    ], class_name="card p-2 me-3 card-bg"),
                    dbc.Col([
                        dcc.Graph(id="graph-2")
                    ], class_name="card p-2 me-3"),
                ], class_name="mb-4"),
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id="graph-3")
                    ], class_name="card p-2 me-3"),
                    dbc.Col([
                        html.H3("Explanation of Parameters"),
                        dcc.Markdown(children=[], id="explanation", className="")
                    ]),
                ]),

            ], width={"size": 9})
        ], class_name="my-3")
    ],
    className="mx-auto my-4")


# Callbacks

@app.callback([Output("graph-1", "figure"), Output("graph-2", "figure"), Output("graph-3", "figure"),
               Output("heading", "children"), Output("explanation", "children")],
              [Input("headings", "value"),
               Input("dropdown-menu", "value")])
def make_graphs(radio_value="Key statistics", dropdown_value="All TOC's"):
    toc = dropdown_value
    heading = radio_value
    subheadings = table_sub_headings[heading]
    explanation = explanations[heading]
    graphs = {}
    if toc == "All TOC's":
        callback_data = [data_tables[subheading].sum(axis=1) if subheading not in all_tocs_mean_graphs else data_tables[
            subheading].mean(axis=1) for subheading in subheadings]
    else:
        callback_data = [data_tables[subheading][toc] for subheading in subheadings]
    for i in range(len(callback_data)):
        if graph_types[subheadings[i]] == "bar":
            graphs[f"graph_{i}"] = px.bar(x=callback_data[i].index, y=callback_data[i].values,
                                          color=callback_data[i].values,
                                          color_continuous_scale=f"{graph_colours[subheadings[i]]}",
                                          text_auto=True,
                                          )
            graphs[f"graph_{i}"].update_coloraxes(showscale=False)

        elif graph_types[subheadings[i]] == "line":
            graphs[f"graph_{i}"] = px.line(x=callback_data[i].index, y=callback_data[i].values, markers=True)
            graphs[f"graph_{i}"].update_traces(line=dict(color=f"{graph_colours[subheadings[i]]}"))

        graphs[f"graph_{i}"].update_layout(title=subheadings[i], xaxis_title="Date", yaxis_title=subheadings[i],
                                           yaxis_range=[0.95 * min(callback_data[i].values),
                                                        1.02 * max(callback_data[i].values)])
        graphs[f"graph_{i}"].update_traces(
            hovertemplate='<b>Date</b>: ' + '%{x}' + '<br>' + f'<b>{subheadings[i]}</b>: ' + '%{y:.1f}')
    return graphs["graph_0"], graphs["graph_1"], graphs["graph_2"], heading, explanation


# Run app
if __name__ == "__main__":
    app.run_server()
