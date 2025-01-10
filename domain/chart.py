from pydantic import BaseModel, Field
from typing_extensions import List, Any, Union

class StreamlitChart(BaseModel):
  chart_type: str = Field(description='Chart type that best fits the data. One of "line" or "bar"')
  chart_title: str = Field(description='Concise and clear title that best fits the visualization.')
  data: List[List[Any]] = Field(description='Data to be plotted.')
  columns: List[str] = Field(description='List of columns from the data.')
  x: str = Field(description='Column name associated to the x-axis data.')
  y: Union[str, List[str]] = Field(description='One or more column names associated to the y-axis data.')