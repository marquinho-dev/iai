#!/bin/bash

# Diretório onde os scripts serão instalados
INSTALL_DIR="/usr/local/bin"

# Nome do repositório
REPO_NAME="iai"

# Nome do diretório temporário para clonar o repositório
TEMP_DIR="/tmp/$REPO_NAME"

# Função para clonar o repositório e instalar os scripts
install_scripts() {
    # Clonando o repositório no diretório temporário
    echo "Clonando o repositório..."
    git clone https://github.com/marquinho-dev/$REPO_NAME.git "$TEMP_DIR" || { echo "Falha ao clonar o repositório."; exit 1; }

    # Entrando no diretório clonado
    cd "$TEMP_DIR" || { echo "Falha ao entrar no diretório temporário."; exit 1; }

    # Verificando se o diretório 'scripts' existe
    if [ ! -d "scripts" ]; then
        echo "O diretório 'scripts' não existe. Verifique o repositório."
        exit 1
    fi

    # Copiando todos os scripts do diretório 'scripts' para o diretório de instalação
    echo "Copiando scripts para $INSTALL_DIR..."
    sudo cp scripts/* "$INSTALL_DIR" || { echo "Falha ao copiar scripts."; exit 1; }

    # Dando permissão de execução aos scripts
    sudo chmod +x "$INSTALL_DIR"/*

    # Criando um link simbólico para o script 'iai.py'
    if [ -f "$INSTALL_DIR/iai.py" ]; then
        sudo ln -sf "$INSTALL_DIR/iai.py" "$INSTALL_DIR/iai" || { echo "Falha ao criar link simbólico."; exit 1; }
        echo "Link simbólico criado: $INSTALL_DIR/iai -> $INSTALL_DIR/iai.py"
    else
        echo "O script 'iai.py' não foi encontrado no diretório de instalação."
        exit 1
    fi

    echo "Scripts instalados com sucesso em $INSTALL_DIR."

    # Limpando o diretório temporário
    rm -rf "$TEMP_DIR"
}

# Chamando a função de instalação
install_scripts
