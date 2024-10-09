# IAI - AppImage Installer
O IAI (Install AppImage) é um script Python que automatiza a instalação de aplicativos no formato `.AppImage` em sistemas Linux. Ele move o arquivo `.AppImage` para um diretório especificado, cria um atalho no menu de aplicativos e associa um ícone ao aplicativo para facilitar o seu acesso.

# Requisitos
+ Python 3.6 ou superior
+ Permissão de sudo para copiar arquivos para /usr/share/applications
+ Git (para clonar o repositório)

# Instalação
1. Clone o repositório e execute o script install.sh:
+ `git clone https://github.com/marquinho-dev/iai.git && cd iai && ./install.sh`
