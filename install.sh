#!/bin/bash

# Defina o diretório de instalação (ajuste conforme necessário)
INSTALL_DIR="/usr/local/bin"

# Nome do repositório (ajuste conforme o nome do seu repositório no GitHub)
REPO_NAME="iai"

# Nome do diretório temporário
TEMP_DIR="/tmp/$REPO_NAME"

# Função para clonar o repositório e instalar
install_scripts() {
    # Clone o repositório no diretório temporário
    git clone https://github.com/marquinho-dev/$REPO_NAME.git "$TEMP_DIR"

    # Navegue até o diretório clonado
    cd "$TEMP_DIR" || exit 1

    # Copie todos os scripts do diretório 'scripts' para o diretório de instalação
    sudo cp scripts/* "$INSTALL_DIR"

    # Dê permissão de execução aos scripts
    sudo chmod +x "$INSTALL_DIR"/*

    echo "Scripts instalados com sucesso em $INSTALL_DIR."

    # Limpeza do diretório temporário
    rm -rf "$TEMP_DIR"
}

# Execute a função de instalação
install_scripts
