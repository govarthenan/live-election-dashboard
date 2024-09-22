import requests
from bs4 import BeautifulSoup
import plotly.graph_objs as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

def scrape_data(num_pairs=3):
    url = "https://www.results.elections.gov.lk/index.php"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    data = {}

    for i in range(1, num_pairs + 1):
        key_selector = f"#overview > div > div.col-lg-4.d-flex.flex-column > div.col-12.grid-margin.stretch-card > div > div > div > div > div.mt-3 > div:nth-child({i}) > div > div > div.wrapper.ms-3.w-100 > p"
        int_selector = f"#overview > div > div.col-lg-4.d-flex.flex-column > div.col-12.grid-margin.stretch-card > div > div > div > div > div.mt-3 > div:nth-child({i}) > div > div > div.wrapper.ms-3.w-100 > div.d-flex.justify-content-between.align-items-center.mt-1 > small:nth-child(1)"
        float_selector = f"#overview > div > div.col-lg-4.d-flex.flex-column > div.col-12.grid-margin.stretch-card > div > div > div > div > div.mt-3 > div:nth-child({i}) > div > div > div.wrapper.ms-3.w-100 > div.d-flex.justify-content-between.align-items-center.mt-1 > small:nth-child(2)"

        key_element = soup.select_one(key_selector)
        int_element = soup.select_one(int_selector)
        float_element = soup.select_one(float_selector)

        if key_element and int_element and float_element:
            key = key_element.text.strip().split()[0]
            int_value = int(int_element.text.replace(",", ""))
            float_value = float(float_element.text.strip("%"))
            data[key] = [int_value, float_value]
        else:
            break  # Stop if we can't find all elements for a pair

    return data

def create_bar_chart(data):
    keys = list(data.keys())
    int_values = [data[key][0] for key in keys]
    float_values = [data[key][1] for key in keys]

    # Extended color palette
    color_palette = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC', '#99CCFF', '#CCFF99', '#FFD700']

    trace = go.Bar(
        x=keys,
        y=int_values,
        text=[],
        textposition='inside',
        hoverinfo='text',
        marker=dict(color=color_palette[:len(keys)])  # Use colors from the palette
    )

    annotations = [
        dict(
            x=key,
            y=value,
            text=f"<b>{value:,}</b>",
            font=dict(family="Arial", size=14, color="black"),
            showarrow=False,
            yanchor='bottom',
            yshift=5
        ) for key, value in zip(keys, int_values)
    ]

    for key, int_value, float_value in zip(keys, int_values, float_values):
        annotations.append(
            dict(
                x=key,
                y=int_value / 2,
                text=f"<b>{float_value:.2f}%</b>",
                font=dict(family="Arial", size=14, color="white"),
                showarrow=False,
                yanchor='middle'
            )
        )

    layout = go.Layout(
        title=dict(
            text='<b>Election Results</b>',
            font=dict(size=24, family='Arial Black'),
            x=0.5
        ),
        xaxis=dict(
            title=dict(text='<b>Candidates</b>', font=dict(size=18, family='Arial Black')),
            tickfont=dict(size=14, family='Arial', weight='bold'),
            ticktext=[key.title() for key in keys],
            tickvals=keys
        ),
        yaxis=dict(title=dict(text='<b>Votes</b>', font=dict(size=18, family='Arial Black'))),
        template='plotly_white',
        annotations=annotations
    )

    return {'data': [trace], 'layout': layout}

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # 60 seconds
        n_intervals=0   
    )
])

@app.callback(Output('live-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph(n):
    data = scrape_data(num_pairs=5)  # Change this number to scrape more or fewer pairs
    return create_bar_chart(data)


def main():
    app.run_server(debug=True, host='localhost', port=8050)

if __name__ == '__main__':
    main()

