from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

PATH = './data/psr_LLM.parquet'
df_apolices = pd.read_parquet(PATH)

now = datetime.now()

prefix = f'''
O dataframe possui dados desde 2006 até 2023. Não se esqueça que estamos no mês {now.strftime('%m')} do ano de {now.strftime('%Y')}.

Aqui estão os valores possíveis para a coluna "cultura" em formato de lista:
<cultura>{df_apolices.cultura.unique()}</cultura>

Lembre-se que é importante separar a 1ª e 2ª safra do milho.

E aqui estão os valores possíveis para a coluna "evento_preponderante" (que representa o desastre climático que causou o sinistro) em formato de list:
<evento_preponderante>{df_apolices.evento_preponderante.unique()}</evento_preponderante>

Lembre-se que o se o "evento_preponderante" for "-", significa que não houve sinistro na apólice, ou seja, não ocorreu nenhum evento climático.

Nunca esqueça que o cálculo da sinistralidade (índice de sinistralidade) deve incluir qualquer valor da coluna "evento_preponderante", incluindo apólices em que o valor é "-".

Como um especialista em seguro rural você conhece todos os termos relevantes como índice de sinistralidade, taxa do prêmio, importância segurada, entre outros.

Não responda com exemplos, mas com informações estatísticas.

Sempre indique que a resposta tem como base dados do Programa de Subscriação do Seguro Rural (PSR) e exiba o link de acesso: https://dados.agricultura.gov.br/dataset/sisser3
'''

print('criando agente')
pandas_agent = create_pandas_dataframe_agent(
  llm=llm,
  df=df_apolices,
  prefix=prefix,
  allow_dangerous_code=True,
  agent_type=AgentType.OPENAI_FUNCTIONS,
  verbose=True
)