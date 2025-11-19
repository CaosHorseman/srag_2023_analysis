# 🔬 Análise de SRAG (Síndrome Respiratória Aguda Grave) — 2023 
Projeto para o Desafio de Ciência de Dados NIM / AutoGlass

Este repositório reúne um pipeline completo de ciência de dados aplicado à base nacional de **SRAG (SIVEP-Gripe)** do *Open Data SUS*, cobrindo desde ingestão e tratamento dos dados até análises epidemiológicas e modelagem preditiva.

A estrutura do projeto foi construída a partir dos seguintes insumos:

- **Base SRAG 2023–2025** (`INFLUD23-26-06-2025.parquet`)  
- **Tabela complementar** (`srag_total.xlsx`)  
- **Dicionário oficial de variáveis SRAG** (`Dicionario_de_Dados_SRAG_Hospitalizado.pdf`)  
- **Descrição completa do desafio** (`Desafio - Ciência de Dados - NIM (2).docx`)  
- **Repositório**: https://github.com/CaosHorseman/srag_2023_analysis

O objetivo é transformar essas fontes em um ecossistema analítico claro, reprodutível e útil para decisões de saúde pública.

## 📁 Estrutura do Projeto

```
├── data/
│   ├── raw/
│   │   ├── INFLUD23-26-06-2025.parquet
│   │   ├── srag_total.xlsx
│   ├── docs/
│   │   ├── Dicionario_de_Dados_SRAG_Hospitalizado.pdf
│   │   ├── Desafio - Ciência de Dados - NIM (2).docx
│
├── notebooks/
│   ├── 00_Exploracao_Inicial.ipynb
│   ├── 01_Tratamento_Dados.ipynb
│   ├── 02_Analise_Descritiva.ipynb
│   ├── 03_Modelagem_Preditiva.ipynb
│   ├── 04_Insights_Recomendacoes.ipynb
│
├── src/
│   ├── load.py
│   ├── preprocess.py
│   ├── features.py
│   ├── analysis.py
│   ├── modeling.py
│   └── viz.py
│
└── README.md
```

## 🧬 Objetivos Analíticos

1. Tratamento da Base  
2. Análise Descritiva  
3. Modelagem Preditiva (Óbito vs Não Óbito)  
4. Insights Epidemiológicos  

## 🚀 Pipeline de Execução

```bash
pip install -r requirements.txt
python src/load.py
python src/preprocess.py
jupyter notebook
python src/modeling.py
```

## 📊 Principais Produtos Finais

- Dataset tratado  
- Painéis gráficos  
- Modelos preditivos  
- Documento de recomendações  

## 🔮 Próximos Passos

- Monitoramento em tempo real  
- Previsão de ondas  
- Detecção precoce de surtos  
- Classificação automatizada de risco individual  
