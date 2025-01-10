from agents.analyst_agent import get_chart_parameters
from domain.chart import StreamlitChart
import streamlit as st
import pandas as pd

st.set_page_config(layout='centered')

def generate_chart(query):
  with st.spinner('Gerando gráfico...'):
    chart_parameters: StreamlitChart = get_chart_parameters(query)

  df = pd.DataFrame(data=chart_parameters.data, columns=chart_parameters.columns)

  st.title(chart_parameters.chart_title)
  if chart_parameters.chart_type == 'line':
    st.line_chart(data=df, x=chart_parameters.x, y=chart_parameters.y, use_container_width=True)
  elif chart_parameters.chart_type == 'bar':
    st.bar_chart(data=df, x=chart_parameters.x, y=chart_parameters.y, use_container_width=True)


with st.form("chart_form"):
  query = st.text_input('Pergunta')

  submitted = st.form_submit_button("Gerar")
  if submitted:
    generate_chart(query)