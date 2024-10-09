# IAI - AppImage Installer
O IAI (Install AppImage) é um script Python que automatiza a instalação de aplicativos no formato `.AppImage` em sistemas Linux. Ele move o arquivo `.AppImage` para um diretório especificado, cria um atalho no menu de aplicativos e associa um ícone ao aplicativo para facilitar o seu acesso.

# Requisitos
+ Python 3.6 ou superior
+ Permissão de sudo para copiar arquivos para /usr/share/applications
+ Git (para clonar o repositório)

# Instalação
1. Clone o repositório e execute o script `install.sh`:
+ `git clone https://github.com/marquinho-dev/iai.git && cd iai && ./install.sh`
2. O script `install.sh` irá configurar as permissões e preparar o ambiente para o script `iai`.

# Uso
1. O script `iai` deve ser chamado diretamente do terminal usando os seguintes argumentos:
+ `iai -l /caminho/para/seu/app.AppImage -i /caminho/para/seu/icon.png -d /opt`

# Argumentos
+ `-l`, `--location` (obrigatório): Especifica o caminho completo para o arquivo `.AppImage`
que será instalado. Exemplo: `/home/usuario/Downloads/app.AppImage`.
`-i`, `--icon` (obrigatório): Especifica o caminho completo para o ícone do aplicativo em
formato `.png` ou `.svg`. Exemplo: `/home/usuario/Downloads/app-icon.png`.
+ `-d`, `--destination` (opcional): Define o diretório onde o arquivo `.AppImage` será movido.
O padrão é `/opt`. Caso o diretório não exista, o script perguntará se você deseja criá-lo.
+ `-c`, `--categories` (opcional): Define a categoria do aplicativo para o menu. O padrão é `Utility`. Exemplo: `Development;Graphics`.

# Exemplo de Uso
`/home/user/Downloads/MyApp.AppImage -i /home/user/Downloads/MyApp-icon.png -d /opt`

# Explicação do Script
1. **Localização do Arquivo** (`-l` ou `--location`): O caminho completo para o arquivo `.AppImage`.
2. **Icone** (`-i` ou `--icon`): Caminho para o ícone do aplicativo.
3. **Destino** (`-d` ou `--destination`): Diretório para armazenar o `.AppImage`.
4. **Categoria** (`-c` ou `--categories`): Categoria para organização do aplicativo no menu.

O script move o arquivo `.AppImage` para o diretório especificado, cria um arquivo .desktop no diretório `/usr/share/applications` para que o aplicativo apareça no menu do sistema, e utiliza o ícone fornecido para facilitar a identificação visual do aplicativo.

# Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

# Licença
Este projeto está licenciado sob a > MIT > License.

