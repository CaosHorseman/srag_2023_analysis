import streamlit as st
import pandas as pd
import joblib
import numpy as np

# === 1. Carregar modelo treinado ===
@st.cache_resource
def load_model():
    modelo = joblib.load("models/random_forest_srag_2023.pkl")
    return modelo

model = load_model()

st.title("Score de Risco de Óbito em SRAG - 2023 (Prova de Conceito)")

st.markdown(
    """
    Este app é uma prova de conceito que utiliza o modelo treinado 
    para estimar a probabilidade de óbito em casos de SRAG hospitalizados.
    """
)

# === 2. Inputs principais (exemplo; adapte para suas colunas reais) ===

st.subheader("Informações do paciente")

idade = st.number_input("Idade (anos)", min_value=0, max_value=120, value=65)

sexo = st.selectbox("Sexo", ["M - Masculino", "F - Feminino"])
raca = st.selectbox(
    "Raça/Cor (macro)",
    ["Branca", "Preta/Parda", "Outras (Amarela/Indígena)", "Ignorado/Missing"],
)

zona = st.selectbox("Zona", ["1 - Urbana", "2 - Rural", "3 - Periurbana", "Missing"])

regiao = st.selectbox("Região", ["N", "NE", "CO", "SE", "S"])
tipo_mun = st.selectbox("Tipo de município", ["capital", "interior"])

estacao = st.selectbox("Estação (sintomas)", ["verao", "outono", "inverno", "primavera"])

n_comorb = st.number_input("Número de comorbidades", min_value=0, max_value=10, value=2)

uti_flag = st.selectbox("Usou UTI?", ["Não", "Sim"])
suport_ven = st.selectbox(
    "Suporte ventilatório",
    [
        "3 - Não",
        "2 - Sim, não invasivo",
        "1 - Sim, invasivo",
        "9 - Ignorado",
    ],
)

dias_sin_interna = st.number_input(
    "Dias entre início dos sintomas e internação",
    min_value=0,
    max_value=60,
    value=3,
)

dias_sin_uti = st.number_input(
    "Dias entre início dos sintomas e entrada na UTI (se aplicável)",
    min_value=0,
    max_value=60,
    value=2,
)

# Comorbidades simples: aqui só HAS_COMORB como exemplo
has_comorb = 1 if n_comorb > 0 else 0

# === 3. Montar dataframe de uma linha com MESMAS COLUNAS de treino ===
# Aqui é só um exemplo; você deve alinhar com sua lista real de features.

if st.button("Calcular risco"):
    # Monta dicionário com todas as features usadas pelo modelo
    data = {
        "NU_IDADE_N": [idade],
        "N_COMORB": [n_comorb],
        "HAS_COMORB": [has_comorb],
        "SEVERIDADE_ESCALA": [np.nan],  # se não quiser usar, pode manter NaN
        "dias_sin_interna_cl": [dias_sin_interna],
        "dias_sin_uti_cl": [dias_sin_uti],
        "CS_SEXO_label": [sexo],
        "CS_RACA_macro": [raca],
        "CS_ZONA_label": [zona],
        "SG_UF_NOT": ["SP"],  # exemplo; você pode expor esse campo também
        "REGIAO": [regiao],
        "TIPO_MUN": [tipo_mun],
        "UTI_flag": [1 if uti_flag == "Sim" else 0],
        "SUPORT_VEN": [int(suport_ven.split(" ")[0])],
        "estacao": [estacao],
        # Exemplo: todas comorb_flags como 0 (você pode expor como checkboxes)
        "PUERPERA_flag": [0],
        "CARDIOPATI_flag": [0],
        "HEMATOLOGI_flag": [0],
        "SIND_DOWN_flag": [0],
        "HEPATICA_flag": [0],
        "ASMA_flag": [0],
        "DIABETES_flag": [0],
        "NEUROLOGIC_flag": [0],
        "PNEUMOPATI_flag": [0],
        "IMUNODEPRE_flag": [0],
        "RENAL_flag": [0],
        "OBESIDADE_flag": [0],
        "OUT_MORBI_flag": [0],
    }

    df_input = pd.DataFrame(data)

    # Predição
    proba = model.predict_proba(df_input)[:, 1][0]
    risco_pct = 100 * proba

    # Classificação simples em faixas
    if proba < 0.10:
        faixa = "Baixo risco"
        cor = "🟢"
    elif proba < 0.30:
        faixa = "Risco intermediário"
        cor = "🟡"
    else:
        faixa = "Alto risco"
        cor = "🔴"

    st.subheader("Resultado")
    st.write(f"Probabilidade estimada de óbito: **{risco_pct:.1f}%**")
    st.write(f"Faixa de risco: {cor} **{faixa}**")

    st.caption(
        "Modelo treinado com base em dados de SRAG 2023; uso ilustrativo, não substitui julgamento clínico."
    )
