FROM mcr.microsoft.com/devcontainers/python:3.12

# Atualiza e instala dependências de sistema
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    python3-pip python3-cffi python3-brotli libpango-1.0-0 \
    libharfbuzz0b libpangoft2-1.0-0 libpangocairo-1.0-0 \
    libgdk-pixbuf-2.0-0 libffi-dev shared-mime-info

# Mantém o container limpo
RUN apt-get clean && rm -rf /var/lib/apt/lists/*