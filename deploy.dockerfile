FROM python:3.11-slim

# Evita problemas de buffer de log
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 1. Copia requirements e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copia o restante do código (incluindo models/)
COPY . .

# 3. Expõe porta padrão do Streamlit
EXPOSE 8501

# 4. Comando de execução
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
