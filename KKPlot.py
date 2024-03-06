#────────────────────────────────────────────────────────────────────────────────────────────────────────────
# TREND CON IQR
#────────────────────────────────────────────────────────────────────────────────────────────────────────────
def trend_with_IQR(data,
                   x_feature,
                   x_feature_type,
                   unique_x_labels,
                   y_feature,
                   thresholds,
                   x_axis_title,
                   y_axis_title,
                   y_axis_range,
                   title,
                   plot_size,
                   show_image,
                   save_image,
                   scale,
                   folder_path,
                   plot_name):
    fig = go.Figure()
    median = []
    upper_quartile = []
    lower_quartile = []
    
    if unique_x_labels == 'auto':
        unique_x_labels = data[x_feature].unique()
        
    for index, label in enumerate(unique_x_labels):   
        if x_feature_type == 'str':
            feature_label = "'"+str(label)+"'"
        elif x_feature_type == 'numeric':
            feature_label = str(label)
            
        lower_quartile.append(data.query(str(x_feature+'=='+feature_label))[y_feature].describe()['25%'])
        median.append(data.query(str(x_feature+'=='+feature_label))[y_feature].describe()['50%'])
        upper_quartile.append(data.query(str(x_feature+'=='+feature_label))[y_feature].describe()['75%'])

    # Add the uncertainty upper bound
    fig.add_trace(go.Scatter(x=unique_x_labels, y=upper_quartile,
                          mode='lines',
                          showlegend = False,
                          line = dict(color='gray', width=1, dash='solid'),
                          name='Variabilità'))

    # Add the uncertainty lower bound
    fig.add_trace(go.Scatter(x=unique_x_labels, y=lower_quartile,
                          mode='lines',
                          line = dict(color='gray', width=1, dash='solid'),
                          name='Variabilità',
                          fill='tonexty',
                          fillcolor='rgba(0,0,0,0.1)'))

    fig.add_trace(go.Scatter(x=unique_x_labels, 
                             y=median,
                             mode='markers+lines+text',
                             name = x_axis_title,
                             text = np.array(median).round(0),
                             textposition='top center',
                              line = dict(color='black', width=1),
                              marker=dict(size=14,
                                          color=median,
                                          cmax=max(median),
                                          cmin=5, #min(median),
                                          colorscale=["#356E97", "#851E2F"],
                                          symbol = 0,
                                          line=dict(width=1,color='Black')
                                          ),
                              ))

    if thresholds:
        thresholds_text = []
        thresholds_y = []
        thresholds_x = []
        for threshold in thresholds:
            fig.add_trace(go.Scatter(x=unique_x_labels, 
                                     y=[threshold['y']]*len(median),
                                      mode= 'lines' ,
                                      name = threshold['name'],
                                      showlegend = True,
                                      line = dict(color = threshold['line_color'], 
                                                  dash = threshold['line_dash'],
                                                  width = threshold['line_width']),
                                      ))
            thresholds_text.append(threshold['name'])
            thresholds_y.append(threshold['y'])
            thresholds_x.append(threshold['x'])

        fig.add_trace(go.Scatter(x = thresholds_x, 
                                 y = thresholds_y,
                                 mode='text',
                                 name = 'Values',
                                 showlegend = False,
                                 text = thresholds_text,
                                 textposition='middle center',
                                ))
    
    fig.update_yaxes(showline=False,
                  linecolor='rgba(21, 44, 60, 0.6)',
                  titlefont = dict(size = 17),
                  tickfont = dict(size = 14),
                  range = y_axis_range,
                  title_text = y_axis_title,)

    fig.update_xaxes(showline=False,
                  linecolor='rgba(21, 44, 60, 0.6)',
                  titlefont = dict(size = 17),
                  tickfont = dict(size = 14),
                  title_text = x_axis_title)

    fig.update_layout(title = "<b>"+title+"</b>",
                      template="plotly_white",
                      margin=dict(r = 40, l = 100),
                      width=plot_size[0],#dimensions[0],
                      height=plot_size[1],#dimensions[1],
                      uniformtext_minsize=12,
                      uniformtext_mode='hide',
                      showlegend=True,
                      legend=dict(
                          orientation="h",
                          yanchor="top",
                          y=-0.2,
                          xanchor="center",
                          x=0.5)
                      )
    if save_image:
        pio.write_image(fig, ''.join([folder_path, plot_name]), scale=scale)
    
    if show_image:
        fig.show()
        
    return fig
