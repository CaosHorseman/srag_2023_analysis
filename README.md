## 🔬 Análise Epidemiológica e Modelagem Preditiva de SRAG – Brasil 2023

Este repositório conduz uma investigação completa do comportamento de casos de SRAG hospitalizados no Brasil em 2023, integrando:

1. **Saneamento e engenharia de dados**  
2. **EDA estruturada por blocos epidemiológicos**  
3. **Modelos de ML para predição de óbito**  
4. **Protótipo de aplicação para score de risco**

---

## 1. Dados e Fontes

### Fontes principais:
- SRAG 2023 (SIVEP-Gripe — Open Data SUS)  
- Dicionário SRAG oficial  
- Arquivo do desafio NIM (AutoGlass)  
- Bases auxiliares (`srag_total`, dicionário refinado, parquet/csv tipado)

### Estrutura de dados:
- `data/raw/`
- `data/processed/`
- `docs/` (documentos oficiais)
- `reports/` (gráficos)
- `models/` (modelos salvos)

---

## 2. Engenharia de Dados

Criamos variáveis derivadas robustas:

### Grupos de risco
- Idade (`NU_IDADE_N`)  
- Nº de comorbidades (`N_COMORB`)  
- Flag `HAS_COMORB`  
- Flags individuais (diabetes, cardiopatia, renal, hepática etc.)

### Gravidade
- `UTI_flag`  
- `SUPORT_VEN`  
- Escala de severidade (0 sem suporte → 3 ventilação invasiva)

### Tempo
- `dias_sin_interna_cl`  
- `dias_sin_uti_cl`  
- Datas limpas (0–60 dias)

### Geografia e contexto social
- UF  
- Região  
- Zona urbana/rural  
- Capital/interior  
- Macro-raça  
- Estação do ano (a partir da data de sintomas)

---

## 3. EDA — Principais Resultados

### Grupos de risco
- Idosos e pacientes com múltiplas comorbidades concentram os óbitos.  
- Diferenças por raça/cor são reais, mas moduladas pelo território.

### Gravidade
- Ventilação invasiva ≈ 50% de mortalidade.  
- Escala de severidade cresce de forma monotônica com risco.

### Tempo / Sazonalidade
- Sintomas → internação: ~2–3 dias  
- Sintomas → UTI: ~3 dias  
- Sintomas → desfecho: ~9–10 dias  
- Letalidade sobe na primavera/verão sem aumento proporcional de UTI.

### Geografia
- Sudeste concentra casos.  
- UF e tipo de município revelam hotspots de letalidade.  
- Zona rural/periurbana pode ter maior risco em alguns recortes.

---

## 4. Modelagem (Óbito vs Não Óbito)

### Alvo
`EVOLUCAO_BIN` (0 = não óbito, 1 = óbito)

### Models
- **Regressão Logística**  
- **Random Forest**

### Desempenho (teste)
- ROC-AUC ≈ 0,89–0,90  
- PR-AUC ≈ 0,56–0,58  
- Recall (óbito) ≈ 0,83–0,84  
- F1 ≈ 0,50–0,51  

### Interpretação
- Bons ranqueadores de risco, coerentes com achados epidemiológicos.  
- Recall alto → útil para triagem.  
- Calibração pode ser refinada.

---

## 5. Produto (Streamlit + Docker)

App permite:
- Entrada dos dados do paciente  
- Estimativa da probabilidade de óbito  
- Faixa de risco gerada pelo modelo  

Deploy em Docker:

```bash
docker build -t srag-risk-app .
docker run -p 8501:8501 srag-risk-app
```

---

## 6. Conclusões

- Idade, comorbidades e severidade são determinantes centrais.  
- O sistema opera em patamar alto de gravidade durante todo o ano.  
- Letalidade tardia sugere efeitos de mix viral e pressão sistêmica.  
- Modelos oferecem suporte real para triagem e vigilância.

---

## 7. Recomendações

- Adoção de score de risco na admissão.  
- Painéis de inequidade contínuos.  
- Melhoria da qualidade de preenchimento (datas, raça, comorbidades).  
- Validações adicionais (temporal, externa).  

---

## 8. Licença

MIT License.
