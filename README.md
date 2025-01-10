# LLM Charts

A streamlit app that uses langchain to query pandas dataframes and generate charts.

## Installation

Create a virtual environment: `python -m venv .venv`

Activate the virtual enrironment:

-   Windows: `.venv/Scripts/activate`

-   Linux and macOS: `source .venv/bin/activate`

Install the required packages: `pip install -r requirements.txt`

Also, don't forget to rename the `.env.example` file to `.env` and change the `OPENAI_API_KEY=` environment variable to your own api key.

## Running the application

With your virtual environment activated, run `streamlit run app` to start the application. You can access it at: http://localhost:8501

Query examples for generating charts:

-   **Para cada ano, calcule o número de apólices do Paraná**
-   **Qual o índice de sinistralidade de soja no paraná para cada um dos anos entre 2013 e 2023?**
