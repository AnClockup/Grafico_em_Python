import plotly.express as px
anos = ['2019', '2020', '2021', '2022']
matriculas = [310, 102, 220, 430]
fig = px.bar(x = anos, y = matriculas, color = anos, title= 'Matriculas x Anos da Academia', height = 400, width= 500 )
fig.update_xaxes(title = 'Anos', title_font_color = 'red', ticks='outside', tickfont_color ='green')
fig.update_yaxes(title = 'Matriculas', title_font_color = 'red', ticks='outside', tickfont_color ='green')
fig.update_traces(marker_line_color = 'rgb(8,48,107)', marker_line_width = 1.5)
fig.show()

anos = ['2019', '2020', '2021', '2022']
matriculas = [310, 102, 220, 430]
fig = px.bar(x = matriculas, y = anos, color = anos, title= 'Matriculas x Anos da Academia', height = 400, width= 500 )
fig.update_xaxes(title = 'Matriculas', title_font_color = 'red', ticks='outside', tickfont_color ='green')
fig.update_yaxes(title = 'Anos', title_font_color = 'red', ticks='outside', tickfont_color ='green')
fig.update_traces(marker_line_color = 'rgb(8,48,107)', marker_line_width = 1.5)
fig.show()