import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server

# Define the layout
app.layout = html.Div([
    html.H1("Cloud Services Dashboard", style={'textAlign': 'center', 'marginBottom': '30px'}),
    
    dcc.Tabs([
        # IaaS Tab
        dcc.Tab(label='IaaS Metrics', children=[
            html.Div([
                dcc.Graph(id='iaas-metrics'),
                dcc.Interval(
                    id='iaas-update',
                    interval=5000,  # 5 seconds
                    n_intervals=0
                ),
                html.Div([
                    html.P("Infrastructure as a Service (IaaS) provides virtualized computing resources over the internet.",
                           style={'marginTop': '20px', 'padding': '10px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px'}),
                    html.P("Monitors usage of fundamental computing resources: CPU, Memory, Storage, and Network.",
                           style={'padding': '10px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px'})
                ])
            ])
        ]),
        
        # PaaS Tab
        dcc.Tab(label='PaaS Metrics', children=[
            html.Div([
                dcc.Graph(id='paas-metrics'),
                dcc.Interval(
                    id='paas-update',
                    interval=5000,
                    n_intervals=0
                ),
                 html.Div([
                    html.P("Platform as a Service (PaaS) provides a platform allowing customers to develop, run, and manage applications.",
                           style={'marginTop': '20px', 'padding': '10px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px'}),
                    html.P("Tracks application performance metrics: request rates and response times for deployed services.",
                           style={'padding': '10px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px'})
                ])
            ])
        ]),
        
        # SaaS Tab
        dcc.Tab(label='SaaS Metrics', children=[
            html.Div([
                dcc.Graph(id='saas-metrics'),
                dcc.Interval(
                    id='saas-update',
                    interval=5000,
                    n_intervals=0
                ),
                html.Div([
                    html.P("Software as a Service (SaaS) delivers software applications over the internet, on a subscription basis.",
                           style={'marginTop': '20px', 'padding': '10px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px'}),
                    html.P("Monitors user engagement across different subscription tiers: Basic, Professional, and Enterprise.",
                           style={'padding': '10px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px'})
                ])
            ])
        ])
    ])
])

# Callback for IaaS metrics
@app.callback(
    Output('iaas-metrics', 'figure'),
    Input('iaas-update', 'n_intervals')
)
def update_iaas_metrics(n):
    # Simulate IaaS metrics
    resources = ['CPU', 'Memory', 'Storage', 'Network']
    usage = np.random.uniform(20, 95, len(resources))
    
    df = pd.DataFrame({
        'Resource': resources,
        'Usage (%)': usage
    })
    
    fig = px.bar(df, 
                 x='Resource', 
                 y='Usage (%)',
                 title='IaaS Resource Usage',
                 color='Resource',
                 range_y=[0, 100])
    return fig

# Callback for PaaS metrics
@app.callback(
    Output('paas-metrics', 'figure'),
    Input('paas-update', 'n_intervals')
)
def update_paas_metrics(n):
    # Simulate PaaS metrics
    time_points = [datetime.now() - timedelta(minutes=i) for i in range(10)]
    requests = np.random.randint(100, 1000, 10)
    response_times = np.random.uniform(50, 200, 10)
    
    df = pd.DataFrame({
        'Time': time_points,
        'Requests/min': requests,
        'Response Time (ms)': response_times
    })
    
    fig = px.line(df, 
                  x='Time', 
                  y=['Requests/min', 'Response Time (ms)'],
                  title='PaaS Performance Metrics')
    return fig

# Callback for SaaS metrics
@app.callback(
    Output('saas-metrics', 'figure'),
    Input('saas-update', 'n_intervals')
)
def update_saas_metrics(n):
    # Simulate SaaS metrics
    subscription_types = ['Basic', 'Professional', 'Enterprise']
    users = np.random.randint(100, 1000, len(subscription_types))
    
    df = pd.DataFrame({
        'Subscription': subscription_types,
        'Users': users
    })
    
    fig = px.pie(df, 
                 names='Subscription', 
                 values='Users',
                 title='SaaS User Distribution')
    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')