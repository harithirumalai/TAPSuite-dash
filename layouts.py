# -*- coding: utf-8 -*-

import dash_html_components as html
import dash_core_components as dcc


# App Layout
def app_layout():
    return html.Div([html.Div(children = [

        # Top span with the title of the app and associated settings
        html.H1('TAPSuite : TAP-1 Pulse Response Analysis',
                style = {'color': 'White',
                         'backgroundColor':'#c8102e',
                         'textAlign': 'center',
                         'font-size': 32,
                         'height': '80px',
                         'margin': '5px',
                         'borderRadius': '10px',
                         'lineHeight': '80px'})]),


                     # Main Tab core-component with associated style and color settings.
                     dcc.Tabs(id="tabs", children=[

                         
                         # Tab 1: Uploads all TAP pulse response files to the app for further analysis.
                         #       Displays a 3D scatter plot of 25 random pulses for simple visualization
                         #       of all uploaded files.
                         dcc.Tab(label='Upload Pulse Files', value=1, children=tab1()),

    
                         # Tab 2: Loads data from hidden html.Divs in Tab 1 and provides options for
                         # baseline correction, smoothing and inert normalization
                         dcc.Tab(label='Pre-processing of Pulse Data', value=2, children=tab2()),

                         dcc.Tab(label='Moments Based Analysis', value=3, children=[])],

    
                              # Style settings for Tab titles
                              style={'color': '#c8102e', 'font-size': 18},

                              colors={'border': 'white',
                                      'primary': '#c8102e',
                                      'background': 'mistyrose'}),
                       
                     html.Div(id='tab-layout')
    ])

# Layout for Tab 1
def tab1():
    return [

        # Titles
        html.H1('Upload Pulse Response Files',
                style = {'textAlign': 'center',
                         'font-size': 24,
                         'height': '60px',
                         'margin': '5px',
                         'lineHeight': '80px'}),

        # Upload button
        dcc.Upload(id='upload-files',
                   children=html.Div(['Drag and Drop or ',
                                      html.A('Select Files')]),
               
                   style={'width': '99%',
                          'height': '60px',
                          'lineHeight': '60px',
                          'borderWidth': '1px',
                          'borderStyle': 'dashed',
                          'borderRadius': '5px',
                          'textAlign': 'center',
                          'margin': '10px'},
               
                   # Allow multiple files to be uploaded
                   multiple=True),

        html.Hr(),

        # Second section showing 3D scatter plots of all uploaded files
        html.Div(id='3d-pulse-figs'),
        
        html.Div(id='data-tab1', style={'display': 'none'}),

        html.Div(dcc.Store(id='condensed-data-tab1'))

    ]


# Layout for Tab 2
def tab2():
    return [html.Div([

        # Titles
        html.H1('Pre-processing of Pulse Responses',
                style = {'textAlign': 'center',
                         'font-size': 24,
                         'height': '60px',
                         'margin': '5px',
                         'lineHeight': '80px'}),
    
        html.H2('Baseline Correction, Pulse Smoothing and Inert Normalization',
                style={'textAlign': 'center',
                       'font-size': 20}),

        html.Hr(),
        
        html.Div([
        
            html.Div([

                # Left half of page showing choice of AMU and its average pulse
                html.Div([

                    html.H2('Average Pulse Response for chosen AMU',
                            style={'font-size': 20}),
                    
                    html.Label('Select AMU', style={'font-weight': 'bold'}),

                    html.Div(id='amu-dropdown-container'),

                    html.Br(),
                    
                    html.Label('Average Pulse', style={'font-weight': 'bold'}),
    
                    html.Div(id='avg-fig-tab2'),

                    html.Div(id='temp-data', style={'display': 'none'}),

                    html.Div(dcc.Store(id='full-temp-data')),

#                    html.Div(id='data-tab2', style={'display': 'none'}),

                    html.Div(dcc.Store(id='data-tab2')),

                    html.Div(dcc.Store(id='condensed-data-tab2')),

                    html.Hr()],
                     
                         className='six columns'),


                # Right half of page with pre-processing operations   
                html.Div([

                    html.H2('Preprocessing Operations for chosen AMU',
                            style={'font-size': 20}),
                
                    html.Div(children=[

                        html.Label('Baseline Correction', style={'font-weight': 'bold'}),

                        dcc.RadioItems(id='baseline-corr-radioitems',
                                       options=[
                                           {'label': 'Enabled', 'value': True},
                                           {'label': 'Disabled', 'value': False}],
                                       value=False)
                    ]),

                    html.Div(id='baseline-corr-slider'),

                    html.Br(),

                    html.Hr(),

                    html.Div(children=[

                        html.Label('Savitzky-Golay Pulse Smoothing',
                                   style={'font-weight': 'bold'}),

                        dcc.RadioItems(id='sg-radioitems',
                                       options=[
                                           {'label': 'Enabled', 'value': True},
                                           {'label': 'Disabled', 'value': False}],
                                       value=False)
                    ]),
                                        
                    html.Div(id='sg-order-container',
                             children=[
                                 html.Label('Order'),

                                 dcc.Slider(id='sg-order-slider',
                                            min=1,
                                            max=5,
                                            step=1,
                                            value=1,
                                            marks={i: '{0}'.format(i) for i in range(1, 6)}),
                    
                                 html.Br(),

                                 html.Div(id='sg-window-size-container')],
                             
                             style={'width': '49%',
                                    'display': 'inline-block',
                                    'lineHeight': '40px',
                                    'margin': '0px',
                                    'height': '40px'}),

                    html.Br(),
                    
                    html.Div(id='button-container',
                             children=[html.A(html.Button('Download',
                                                          id='download-button-1'),
                                              id='download-link-1',
                                              target='_blank')],
                             
                             style={'width': '49%',
                                    'display': 'inline-block',
                                    'lineHeight': '200px',
                                    'height': '140px'}),

                   
                    html.Hr(),

                    html.Div(children=[

                        html.Label('Apply Corrections to All Data',
                                   style={'font-weight': 'bold'}),

                        dcc.RadioItems(id='all-corr-radioitems',
                                       options=[
                                           {'label': 'Enabled', 'value': True},
                                           {'label': 'Disabled', 'value': False}],
                                       value=False)
                    ]),

                    html.Div(id='apply-all', style={'color': '#c8102e'}),

                    html.Hr(),

                    html.Label('Inert Normalization',
                                   style={'font-weight': 'bold'}),

                    html.Label('Select the inert species AMU'),

                    html.Div(id='inert-dropdown-container', 
                             style={'width': '25%',
                                    'display': 'inline-block'}),

                    html.Div(id='inert-output', style={'color': '#c8102e'}),

                    html.Div(children=[html.A(html.Button('Download', id='download-button-2'),
                                              id='download-link-2',
                                              target='_blank')],
                             style={'width': '49%',
                                    'display': 'inline-block',
                                    'lineHeight': '90px',
                                    'height': '60px'}),                
                ],

                         className='six columns')],

                     className="row")])
        
    ])]


# Layout for creating the baseline correction RangeSlider in Tab 2
def baseline_corr_slider(dataset, disable=False):
    times = dataset['times']
    tmin = min(times)
    tmax = max(times)
    
    return [html.Div([dcc.RangeSlider(id='time-range-slider',
                                      min=tmin,
                                      max=tmax,
                                      step=0.05,
                                      value=[1, 1],
                                      disabled=disable,
                                      marks={tmin: '{0:0.1f}'.format(tmin),
                                             tmax: '{0:0.1f}'.format(tmax)}),
                      html.Br(),
                      html.Div(id='slider-output', style={'color': '#c8102e'})],
                     style={'width': '49%',
                            'display': 'inline-block',
                            'margin': '10px',
                            'lineHeight': '30px',
                            'height': '60px'})]

# Layout for the Savitzky-Golay window size based on input order by user
def sg_window_size_slider(order):

    if order % 2 == 0:
        ws_min = order + 3
    else:
        ws_min = order + 2

    ws_max = ws_min + 21
    children = [
        html.Label('Window Size'),
        
        dcc.Slider(id='sg-window-size-slider',
                   min=ws_min,
                   max=ws_max,
                   step=4,
                   value=ws_min+2,
                   disabled=True,
                   marks={i: '{0}'.format(i) for i in range(ws_min, ws_max, 2)})]

    return children

