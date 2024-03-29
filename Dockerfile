# app/Dockerfile
# FROM python:3.9-slim
FROM python:3.11.7-bookworm

WORKDIR /app

USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# RUN git clone https://github.com/streamlit/streamlit-example.git .
RUN git clone https://github.com/nshern/ft_gpt.git .

# RUN pip3 install -r requirements.txt
RUN pip3 install poetry 
RUN poetry config virtualenvs.create false
RUN poetry install 

RUN poetry run gsutil -m cp -r gs://tense-slate/storage .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

