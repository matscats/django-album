FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do sistema incluindo Node.js e npm
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev \
        nodejs \
        npm \
    && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install poetry

# Configura o diretório de trabalho
WORKDIR /app

# Copia arquivos de dependências do Poetry
COPY poetry.lock pyproject.toml /app/

# Desativa a criação de virtualenvs pelo Poetry
RUN poetry config virtualenvs.create false

# Instala as dependências do projeto
RUN poetry install --no-interaction

# Copia os arquivos do projeto
COPY . /app/

# Instala dependências do Node para o tema Tailwind
WORKDIR /app/app/theme/static_src
RUN npm install

# Volta para o diretório principal
WORKDIR /app

# Copia o script de entrada e define permissões de execução
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]