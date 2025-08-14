import pandas as pd
import pycountry
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# ---------------------------
# Load data
# ---------------------------
df = pd.read_csv("cleaned_jobs.csv")

# Function to classify job levels
def categorize_job_level(title):
    title_lower = title.lower()
    if any(word in title_lower for word in ["chief", "director", "vp", "vice president", "head", "ceo", "cto", "coo"]):
        return "Executive Level"
    elif any(word in title_lower for word in ["senior", "lead", "principal", "staff", "sr.", "manager"]):
        return "Senior Level"
    elif any(word in title_lower for word in ["junior", "associate", "intern", "graduate", "trainee", "fresher"]):
        return "Entry Level"
    else:
        return "Mid Level"

df["job_level"] = df["job_title"].apply(categorize_job_level)

# Convert country codes to full names
def country_full_name(code):
    try:
        return pycountry.countries.get(alpha_2=code).name
    except:
        return code

df["country_name"] = df["company_location"].apply(country_full_name)

# ---------------------------
# Dash App
# ---------------------------
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Job Trends Data Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.Label("Select Job Level"),
            dcc.Dropdown(
                id="level-dropdown",
                options=[{"label": lvl, "value": lvl} for lvl in sorted(df["job_level"].unique())],
                value="Mid Level",
                clearable=False
            )
        ], style={"width": "45%", "display": "inline-block", "padding": "10px"}),

        html.Div([
            html.Label("Select Country"),
            dcc.Dropdown(
                id="country-dropdown",
                options=[{"label": country, "value": country} for country in sorted(df["country_name"].unique())],
                value="India",
                clearable=False
            )
        ], style={"width": "45%", "display": "inline-block", "padding": "10px"})
    ]),

    html.Div([
        dcc.Graph(id="pie-chart", style={"display": "inline-block", "width": "49%"}),
        dcc.Graph(id="bar-chart", style={"display": "inline-block", "width": "49%"})
    ])
])

# ---------------------------
# Callbacks
# ---------------------------
@app.callback(
    [Output("pie-chart", "figure"), Output("bar-chart", "figure")],
    [Input("level-dropdown", "value"), Input("country-dropdown", "value")]
)
def update_charts(selected_level, selected_country):
    filtered_df = df[(df["job_level"] == selected_level) & (df["country_name"] == selected_country)]

    pie_fig = px.pie(
        filtered_df,
        names="job_title",
        title=f"Job Titles - {selected_level} in {selected_country}",
        hole=0.4
    )
    pie_fig.update_traces(textinfo="percent+label", textposition="inside")

    bar_fig = px.bar(
        filtered_df.groupby("job_title")["salary_in_usd"].mean().reset_index(),
        x="job_title",
        y="salary_in_usd",
        title=f"Average Salary by Job Title - {selected_level} in {selected_country}",
        text_auto=".2s"
    )
    bar_fig.update_layout(xaxis_tickangle=-45)

    return pie_fig, bar_fig

# ---------------------------
# Run
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)