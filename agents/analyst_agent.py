from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from domain.chart import StreamlitChart
from agents.pandas_agent import pandas_agent

llm = ChatOpenAI(model='gpt-4o-mini')
structured_llm = llm.with_structured_output(StreamlitChart, method='function_calling')


def get_chart_parameters(query):
  data = pandas_agent.invoke({'input': query})
  prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are a professional data analyst specialized in creating charts. Given the data decide the apropriate chart type, data, columns, x and y to be used in a visualization framework.'),
    ('user', '{data}')
  ])

  chain = prompt | structured_llm
  print('gerando parametros para o gráfico')
  return chain.invoke({'data': data})