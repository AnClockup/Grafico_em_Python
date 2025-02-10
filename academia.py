import plotly.express as px
import pandas as pd
anos = ['2019', '2020', '2021', '2022']
academia_a =[310, 105, 220, 430]
academia_b =[325, 159, 235, 360]
academia_c =[360, 180, 235, 500]

nomes_academias = ['Academia A', 'Academia B', 'Academia C']
df = pd.DataFrame({'Anos': anos, 'Academia A': academia_a, 'Academia B': academia_b, 'Academia C': academia_c})
cores_academias = {'Academia A': 'yellow', 'Academia B': 'blue', 'Academia C': 'red'}


fig = px.bar(df, x = anos, y = nomes_academias,
              title= 'Matriculas x Anos das Academias', height = 400, width= 500, labels = {'value': 'Valores', 'variable': 'Legenda:'},
                barmode = 'relative', color_discrete_map= cores_academias)

fig.update_xaxes(title = 'Anos', title_font_color = 'red', ticks='outside', tickfont_color ='green')
fig.update_yaxes(title = 'Matriculas', title_font_color = 'red', ticks='outside', tickfont_color ='green')
fig.update_traces(marker_line_color = 'rgb(8,48,107)', marker_line_width = 1.5)
fig.show()

anos = ['2019', '2020', '2021', '2022']
academia_a =[310, 105, 220, 430]
academia_b =[325, 159, 235, 360]
academia_c =[360, 180, 235, 500]

nomes_academias = ['Academia A', 'Academia B', 'Academia C']
df = pd.DataFrame({'Anos': anos, 'Academia A': academia_a, 'Academia B': academia_b, 'Academia C': academia_c})
cores_academias = {'Academia A': 'yellow', 'Academia B': 'blue', 'Academia C': 'red'}


fig = px.bar(df, x = nomes_academias, y = anos,
              title= 'Matriculas x Anos das Academias', height = 400, width= 500, labels = {'value': 'Valores', 'variable': 'Legenda:'},
                barmode = 'relative', color_discrete_map= cores_academias)

fig.update_xaxes(title = 'Matriculas', title_font_color = 'red', ticks='outside', tickfont_color ='green')
fig.update_yaxes(title = 'Anos', title_font_color = 'red', ticks='outside', tickfont_color ='green')
fig.update_traces(marker_line_color = 'rgb(8,48,107)', marker_line_width = 1.5)
fig.show()

anos = ['2019', '2020', '2021', '2022']
academia_a =[310, 105, 220, 430]
academia_b =[325, 159, 235, 360]
academia_c =[360, 180, 235, 500]

nomes_academias = ['Academia A', 'Academia B', 'Academia C']
df = pd.DataFrame({'Anos': anos, 'Academia A': academia_a, 'Academia B': academia_b, 'Academia C': academia_c})
cores_academias = {'Academia A': 'yellow', 'Academia B': 'blue', 'Academia C': 'red'}


fig = px.bar(df, x = anos, y = nomes_academias,
              title= 'Matriculas x Anos das Academias', height = 400, width= 500, labels = {'value': 'Valores', 'variable': 'Legenda:'},
                barmode = 'group', color_discrete_map= cores_academias)

fig.update_xaxes(title = 'Anos', title_font_color = 'red', ticks='outside', tickfont_color ='green')
fig.update_yaxes(title = 'Matriculas', title_font_color = 'red', ticks='outside', tickfont_color ='green')
fig.update_traces(marker_line_color = 'rgb(8,48,107)', marker_line_width = 1.5)
fig.show()